# coding: utf-8


from sqlalchemy.orm import Session
from backend.utils.database import use_session
from backend.models import *
from backend.business.exceptions import DataNotFoundException, UnknownParameterException


"""
description = Column(Text(), nullable=True)
    community_id = Column(Integer(), nullable=False)
    volunteer_count = Column(Integer(), nullable=False)
    bot = Column(Boolean(), nullable=True)
    reward = Column(Integer(), nullable=False)

    event_subject_id = Column(Integer(), ForeignKey('event_subject.id'))
    event_subject

"""


class EventDomain:

    def __init__(self,
                 name: str,
                 description: str,
                 community_id: int,
                 volunteer_count: int,
                 bot: bool,
                 reward: int) -> None:
        self.name: str = name
        self.description: str = description
        self.community_id: int = community_id
        self.volunteer_count: int = volunteer_count
        self.bot: bool = bot
        self.reward: int = reward

    @classmethod
    @use_session
    def register(cls,
                 session: Session,
                 org_vk_id: str,
                 name: str,
                 description: str,
                 event_subject: str,
                 community_id: int,
                 volunteer_count: int,
                 reward: int,
                 img: str) -> dict:
        event_subject = session.query(EventSubject).filter(EventSubject.abbr == event_subject).one_or_none()
        if not event_subject:
            raise DataNotFoundException()
        organizer = session.query(Organizer).filter(Organizer.vk_id == org_vk_id).one_or_none()
        if not organizer:
            organizer = Organizer(vk_id=org_vk_id)
        event_obj = Event(name=name,
                          description=description,
                          event_subject_id=event_subject.id,
                          community_id=community_id,
                          volunteer_count=volunteer_count,
                          reward=reward,
                          img=img,
                          )
        event_obj.organizers.append(organizer)
        session.add(event_obj)
        session.commit()
        return event_obj.marshall()

    @classmethod
    @use_session
    def get_detail(cls, session, key: int) -> dict:
        event = session.query(Event).filter(Event.id == key).one_or_none()
        if not event:
            raise DataNotFoundException()
        return event.marshall()

    @classmethod
    @use_session
    def list(cls, session, ) -> list:
        _events = session.query(Event).order_by(Event.event_date).all() or []
        return [event.marshall() for event in _events]
