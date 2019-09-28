# coding: utf-8


import logging
from flask import Blueprint, jsonify, abort, g
from backend.business.events import EventDomain


logger = logging.getLogger(__name__)
blueprint = Blueprint('Event', __name__)


# @blueprint.route('/', strict_slashes=False)
# def get_all():
#     res = EventDomain.get_detail(key=1)
#     return jsonify(res)


@blueprint.route('/list/', strict_slashes=False)
def event_list():
    logger.info('Events. Get ll')
    return jsonify(EventDomain.list()[:5])


