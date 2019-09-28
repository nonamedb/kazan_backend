# coding: utf-8


import pytest
from faker import Faker
import random
from backend.models import Volunteer
from backend.business.volunteers import VolunteerDomain
from backend.business.exceptions import DataNotFoundException
from .factories import Factory
from .confixtures import session, database


fake = Faker()


@pytest.mark.run(order=1)
def test__volunteer__join_event(session):
    event = Factory.event()
    volunteer = VolunteerDomain.join_event(vk_id=random.choice(range(1000, 2000)), event_id=event.id)
    assert session.query(Volunteer).filter(Volunteer.id == volunteer['id']).count() == 1


@pytest.mark.run(2)
def test__volunteer__get_detail():
    volunteer = Factory.volunteer()
    assert volunteer.id == VolunteerDomain.get_detail(key=volunteer.vk_id)['id']
