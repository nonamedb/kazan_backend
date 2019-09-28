# coding: utf-8


import logging
from flask import Blueprint, jsonify, abort, g
from backend.business.volunteers import VolunteerDomain
from backend.business.exceptions import DataNotFoundException


logger = logging.getLogger(__name__)
blueprint = Blueprint('Volunteer', __name__)


@blueprint.route('/<int:vk_id>/join/<int:event_id>', strict_slashes=False)
def join_event(vk_id: int, event_id: int):
    logger.info(f'Volunteer {vk_id} join {event_id}')
    try:
        return jsonify(VolunteerDomain.join_event(vk_id=vk_id, event_id=event_id))
    except DataNotFoundException:
        return abort(404)
    except:
        return abort(500)


@blueprint.route('/list/', strict_slashes=False)
def event_list():
    logger.info('Events. Get ll')
    return jsonify(EventDomain.list()[:5])
