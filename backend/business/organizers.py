

import logging
from sqlalchemy.orm import Session
from backend.utils.database import use_session
from backend.models import Volunteer, Event
from backend.business.exceptions import DataNotFoundException, UnknownParameterException


logger = logging.getLogger(__name__)


class OrganizerDomain:

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
        logger.info(f'Volunteer {vk_id} {event_id}')
        volunteer_obj = session.query(Volunteer).filter(Volunteer.vk_id == vk_id).one_or_none()
        if not volunteer_obj:
            volunteer_obj = Volunteer(vk_id=vk_id)
            session.add(volunteer_obj)
        volunteer_obj.events.append(event)
        logger.info(f'Volunteer add to session')
        session.commit()
        return volunteer_obj.marshall()

    @classmethod
    @use_session
    def get_detail(cls, session, key: int) -> dict:
        volunteer = session.query(Volunteer).filter(Volunteer.vk_id == key).one_or_none()
        if not volunteer:
            raise DataNotFoundException()
        return volunteer.marshall()
