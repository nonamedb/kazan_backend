# coding: utf-8


import logging
from flask import Blueprint, jsonify, abort, g
from backend.business.organizers import OrganizerDomain
from backend.business.exceptions import DataNotFoundException


logger = logging.getLogger(__name__)
blueprint = Blueprint('Organizer', __name__)


@blueprint.route('/<string:vk_id>/', strict_slashes=False)
def organizer_detail(vk_id: int):
    logger.info('Organizer. Get ll')
    try:
        organizer = OrganizerDomain.get_detail(key=vk_id)
        return jsonify(organizer)
    except DataNotFoundException as exc:
        abort(404)
    except:
        abort(500)
