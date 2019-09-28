# coding: utf-8


import logging
from sqlalchemy.orm import Session
from backend.utils.database import use_session
from backend.models import Volunteer, Event
from backend.business.exceptions import DataNotFoundException, UnknownParameterException


logger = logging.getLogger(__name__)


class VolunteerDomain:

    @classmethod
    @use_session
    def join_event(cls,
                   session: Session,
                   vk_id: int,
                   event_id: int) -> dict:
        event = session.query(Event).filter(Event.id == event_id).one_or_none()
        if not event:
            logger.info(f'Volunteer {vk_id} not join {event_id}')
            raise DataNotFoundException()
        volunteer_obj = session.query(Volunteer).filter(Volunteer.vk_id == vk_id).one_or_none()
        if not volunteer_obj:
            volunteer_obj = Volunteer(vk_id=vk_id)
        volunteer_obj.events.append(event)
        session.add(volunteer_obj)
        session.commit()
        return volunteer_obj.marshall()

    @classmethod
    @use_session
    def get_detail(cls, session, key: int) -> dict:

        # event = session.query(Event).filter(Event.id == event_id).one_or_none()
        event = session.query(Event).filter(Event.id == key).one_or_none()
        if not event:
            raise DataNotFoundException()
        return event.marshall()

    @classmethod
    @use_session
    def list(cls, session, ) -> list:
        _events = session.query(Event).order_by(Event.event_date).all() or []
        return [event.marshall() for event in _events]
