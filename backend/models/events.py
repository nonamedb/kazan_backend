# coding: utf-8


from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship, backref
from .base import BaseModel


class Event(BaseModel):
    __tablename__ = 'event'

    id = Column(Integer, Sequence('event_id_seq'), primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(Text(), nullable=True)
    community_id = Column(Integer(), nullable=False)
    volunteer_count = Column(Integer(), nullable=False)
    bot = Column(Integer(), nullable=True)
    reward = Column(Integer(), nullable=True)

    event_subject_id = Column(Integer(), ForeignKey('event_subject.id'))
    event_subject = relationship('EventSubject', lazy='joined')

    def marshall(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            community_id=self.community_id,
            volunteer_count=self.volunteer_count,
            bot=self.bot,
            reward=self.reward
        )


class EventSubject(BaseModel):
    __tablename__ = 'event_subject'

    id = Column(Integer, Sequence('event_subject_id_seq'), primary_key=True)
    name = Column(String(250), nullable=False)

    def marshall(self):
        return dict(
            id=self.id,
        )


__all__ = [Event, EventSubject]
