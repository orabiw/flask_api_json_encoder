""" json_encoder tests """
import datetime
import decimal
import enum
import json

import flask

from api_json_encoder import json_encoder


class DummyEnum(enum.Enum):
    """dummy enum"""

    A = "A"


class DummyClass:  # pylint:disable=too-few-public-methods,invalid-name
    """dummy class"""

    def __init__(self):
        self.a = "a"


def test_dumps() -> None:
    """test `dumps`"""
    app = flask.Flask(__name__)
    encoder = json_encoder.JSONEncoder(app)

    obj_ = DummyClass()
    today = datetime.date.today()
    now = datetime.datetime.now()
    enum_ = DummyEnum("A")
    decimal_ = decimal.Decimal(3.14)
    set_ = {"1", "2", 3}

    obj = {
        "date": today,
        "time": now,
        "something": None,
        "enum": enum_,
        "pi": decimal_,
        "set": set_,
        "obj_": obj_,
    }

    result = json.loads(encoder.dumps(obj))

    assert result != {}

    assert result.pop("date") == today.isoformat()
    assert result.pop("time") == now.isoformat(timespec="milliseconds")
    assert result.pop("something") is None
    assert result.pop("enum") == enum_.value
    assert result.pop("pi") == float(decimal_)
    assert result.pop("set") == list(set_)
    assert result.pop("obj_") == str(obj_)

    assert result == {}
