# coding: utf-8


import logging
from flask import Blueprint, jsonify, abort, g
from backend.business.events import EventDomain


logger = logging.getLogger(__name__)
blueprint = Blueprint('Organizer', __name__)


@blueprint.route('/', strict_slashes=False)
def get_all():
    res = EventDomain.get_detail(key=1)
    return jsonify(dict(results=res))
