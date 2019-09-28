# coding: utf-8


from sqlalchemy import Column, Integer, String, Sequence, Boolean, ForeignKey, DateTime, Text, Date, Table
from sqlalchemy.orm import relationship
from .base import BaseModel, db


organizer_event_table = Table('organizer_event',
                              db.metadata,
                              Column('organizer_id', Integer, ForeignKey('organizer.id')),
                              Column('event_id', Integer, ForeignKey('event.id'))
                              )


class Organizer(BaseModel):
    __tablename__ = 'organizer'

    id = Column(Integer, Sequence('organizer_id_seq'), primary_key=True)
    vk_id = Column(String(50), nullable=False)
    events = relationship("Event",
                          secondary=organizer_event_table,
                          back_populates="organizers"
                          )

    def marshall(self):
        return dict(
            id=self.id,
            vk_id=self.vk_id
        )


__all__ = [Organizer]
