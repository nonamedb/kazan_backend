# coding: utf-8


import logging
from flask import Blueprint, jsonify, abort, g
from backend.business.volunteers import VolunteerDomain
from backend.business.exceptions import DataNotFoundException


logger = logging.getLogger(__name__)
blueprint = Blueprint('Volunteer', __name__)


@blueprint.route('/<string:vk_id>/join/<int:event_id>', strict_slashes=False)
def join_event(vk_id: str, event_id: int):
    logger.info(f'Volunteer {vk_id} join {event_id}')
    try:
        res = VolunteerDomain.join_event(vk_id=vk_id, event_id=event_id)
        logger.info(res)
        return jsonify(res)
    except DataNotFoundException:
        return abort(404)
    except:
        return abort(500)


@blueprint.route('/<string:vk_id>/', strict_slashes=False)
def volunteer_detail(vk_id: int):
    logger.info('Volunteer. Get ll')
    try:
        volunteer = VolunteerDomain.get_detail(key=vk_id)
        return jsonify(volunteer)
    except DataNotFoundException as exc:
        abort(404)
    except:
        abort(500)
