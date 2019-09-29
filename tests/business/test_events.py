# coding: utf-8


import pytest
from faker import Faker
import random
from backend.models import Event
from backend.business.events import EventDomain, Volunteer
from backend.business.exceptions import DataNotFoundException
from .factories import Factory
from .confixtures import database, session


fake = Faker()


@pytest.mark.run(order=1)
def test__event__register(session):
    event_subject = Factory.event_subject()
    event = EventDomain.register(
        org_vk_id=random.choice(range(1000000, 1000050)),
        name=fake.name(),
        description=fake.text(),
        community_id=random.choice(range(10,100)),
        volunteer_count=random.choice(range(10,100)),
        reward=random.choice(range(100, 10000)),
        event_subject=event_subject.name)
    assert session.query(Event).filter(Event.id == event['id']).count() == 1


@pytest.mark.skip
@pytest.mark.run(2)
def test__event__list(session):
    [Factory.event() for _ in range(20)]
    assert session.query(Event).all()


@pytest.mark.skip
@pytest.mark.run(3)
def test__event__get_detail():
    event = Factory.event()
    assert event.id == EventDomain.get_detail(key=event.id)['id']


@pytest.mark.skip
@pytest.mark.run(4)
def test__event__get_volunteers():
    event = Factory.event()
    assert event.id == EventDomain.get_detail(key=event.id)['id']



