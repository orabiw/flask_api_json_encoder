""" test extension """
import flask

from flask_api_json_encoder import extension


def test_extension():
    """test extension"""
    app = flask.Flask(__name__)
    assert extension.APIJsonEncoder(app)


def test_extension_no_app():
    """test extension without an app"""
    assert extension.APIJsonEncoder()
