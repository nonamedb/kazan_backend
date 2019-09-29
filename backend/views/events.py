# coding: utf-8


import logging
from flask import Blueprint, jsonify, abort, g
from backend.business.events import EventDomain
from backend.business.exceptions import DataNotFoundException


logger = logging.getLogger(__name__)
blueprint = Blueprint('Event', __name__)


@blueprint.route('/<int:event_id>', strict_slashes=False)
def event_detail(event_id: int):
    logger.info(f'Events. Get {event_id}')
    try:
        return jsonify(EventDomain.get_detail(key=event_id))
    except DataNotFoundException:
        return abort(404)
    except:
        return abort(500)


@blueprint.route('/list/', strict_slashes=False)
def event_list():
    logger.info('Events. Get ll')
    return jsonify(EventDomain.list()[:5])


@blueprint.route('/add/', methods=['POST'], strict_slashes=False)
def event_add(org_vk_id: str,
              name: str,
              description: str,
              community_id: int,
              volunteer_count: int,
              reward: int,
              event_subject: str):
    logger.info(f'{name}{description}{event_subject}{community_id}{volunteer_count}{reward}')
    try:
        EventDomain.register(org_vk_id=org_vk_id,
                             name=name,
                             description=description,
                             community_id=community_id,
                             volunteer_count=volunteer_count,
                             reward=reward,
                             event_subject=event_subject)
        return jsonify([True])
    except DataNotFoundException as exc:
        abort(500)
