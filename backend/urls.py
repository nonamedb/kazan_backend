# coding: utf-8


from views.organizer import blueprint as organizer


def route(app):
    app.register_blueprint(organizer, url_prefix='/organizer')
