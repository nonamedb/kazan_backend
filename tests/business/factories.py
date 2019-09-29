# coding: utf-8


import factory
import random
from datetime import datetime
import random
import string
from faker import Faker
from backend import models
from backend.utils.database import get_session


session = get_session()


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        obj = model_class(*args, **kwargs)
        session.add(obj)
        session.commit()
        return obj


faker = Faker()


def date_between(start, end):
    return factory.LazyFunction(
        lambda: faker.date_between(start_date=start, end_date=end))


def int_between(start, end):
    return factory.LazyFunction(lambda: random.randint(start, end))


def strand(length=40):
    return factory.LazyFunction(
        lambda: ''.join(
            random.choice(string.ascii_lowercase) for _ in range(length)
        ))


class EventSubjectFactory(BaseFactory):

    class Meta:
        model = models.EventSubject

    name = factory.Faker('name')
    abbr = strand(10)


class EventFactory(BaseFactory):

    class Meta:
        model = models.Event

    name = factory.Faker('name')
    description = factory.Faker('text')
    community_id = random.choice(range(10000,10050))
    volunteer_count = random.choice(range(1, 100))
    bot = random.choice([True, False])
    reward = random.choice(range(1000, 10000, 10))
    event_subject = factory.SubFactory(EventSubjectFactory)


class VolunteerFactory(BaseFactory):

    class Meta:
        model = models.Volunteer

    vk_id = random.choice(range(1000000, 1000050))


class Factory:

    event_subject = EventSubjectFactory
    event = EventFactory
    volunteer = VolunteerFactory
