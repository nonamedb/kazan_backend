# coding: utf-8


from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey, DateTime, Text, Date, Table
from sqlalchemy.orm import relationship
from .base import BaseModel, db


volunteer_event_table = Table('volunteer_event',
                              db.metadata,
                              Column('volunteer_id', Integer, ForeignKey('volunteer.id')),
                              Column('event_id', Integer, ForeignKey('event.id'))
                              )


class Volunteer(BaseModel):
    __tablename__ = 'volunteer'

    id = Column(Integer, Sequence('volunteer_id_seq'), primary_key=True)
    vk_id = Column(String(50), nullable=False)
    volunteer_events = relationship("Event",
                                    secondary=volunteer_event_table,
                                    back_populates='volunteers'
                                    )

    def marshall(self):
        return dict(
            id=self.id,
            vk_id=self.vk_id,
            events=[event.marshall() for event in self.volunteer_events]
        )


__all__ = [Volunteer]
