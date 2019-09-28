# coding: utf-8


import logging
from flask import Blueprint, jsonify, abort, g
from backend.business.events import EventDomain
from backend.business.exceptions import DataNotFoundException


logger = logging.getLogger(__name__)
blueprint = Blueprint('Event', __name__)


@blueprint.route('/<int:event_id>', strict_slashes=False)
def get_all(event_id: int):
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
