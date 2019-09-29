# coding: utf-8


from views.events import blueprint as events
from views.volunteers import blueprint as volunteers
from views.organizers import blueprint as organizers


def route(app):
    app.register_blueprint(events, url_prefix='/event')
    app.register_blueprint(volunteers, url_prefix='/volunteer')
    app.register_blueprint(organizers, url_prefix='/organizer')
