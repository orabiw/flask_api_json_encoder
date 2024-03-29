""" APIJsonEncoder extension class """
import typing as t

import flask

import flask_api_json_encoder


class APIJsonEncoder:  # pylint:disable=too-few-public-methods
    """APIJsonEncoder extension class"""

    def __init__(self, app: t.Optional[flask.Flask] = None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app: flask.Flask) -> None:
        """initialize the app with the extension"""
        app.json = flask_api_json_encoder.JSONEncoder(app)
