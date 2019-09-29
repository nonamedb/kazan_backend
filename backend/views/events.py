# coding: utf-8


import logging
from flask import Blueprint, jsonify, abort, g, request
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
def event_add():
    content = request.json
    logger.info(content)
    try:
        EventDomain.register(org_vk_id=content['org_vk_id'],
                             name=content['name'],
                             description=content['description'],
                             community_id=content['community_id'],
                             volunteer_count=content['volunteer_count'],
                             reward=content['reward'],
                             event_subject=content['event_subject'],
                             img=content['img'])
        return jsonify([True])
    except DataNotFoundException as exc:
        abort(500)
