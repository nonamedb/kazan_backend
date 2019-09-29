# coding: utf-8


from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey, DateTime, Text, Date
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship, backref
from .organizers import organizer_event_table
from .volunteers import volunteer_event_table
from .base import BaseModel


class Event(BaseModel):
    __tablename__ = 'event'

    id = Column(Integer, Sequence('event_id_seq'), primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(Text(), nullable=True)
    community_id = Column(Integer(), nullable=False)
    volunteer_count = Column(Integer(), nullable=False)
    reward = Column(Integer(), nullable=True)
    img = Column(String(250), nullable=True)
    event_date = Column(Date(), default=(datetime.today() + timedelta(days=5)), nullable=False)

    event_subject_id = Column(Integer(), ForeignKey('event_subject.id'))
    event_subject = relationship('EventSubject', lazy='joined')

    organizers = relationship(
        "Organizer",
        secondary=organizer_event_table,
        back_populates="organizer_events")

    volunteers = relationship(
        "Volunteer",
        secondary=volunteer_event_table,
        back_populates="volunteer_events")

    def marshall(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            community_id=self.community_id,
            volunteer_count=self.volunteer_count,
            reward=self.reward,
            img=self.img,
            event_date=self.event_date,
            organizers=[org.id for org in self.organizers],
            volunteers=[vol.id for vol in self.volunteers],
        )


class EventSubject(BaseModel):
    __tablename__ = 'event_subject'

    id = Column(Integer, Sequence('event_subject_id_seq'), primary_key=True)
    name = Column(String(250), nullable=False)
    abbr = Column(String(250), nullable=False)

    def marshall(self):
        return dict(
            id=self.id,
            name=self.name,
            abbr=self.abbr
        )


__all__ = [Event, EventSubject]
