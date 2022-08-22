""" JSON encoder. """
from __future__ import annotations

import datetime
import decimal
import enum
import typing as t

import flask.json


class JSONEncoder(flask.json.provider.DefaultJSONProvider):
    """A JSON encoder for common types for flask"""

    def dumps(self, obj: t.Any, **kwargs: t.Any) -> str:
        return super().dumps(obj, default=_default, **kwargs)


def _default(o: t.Any) -> t.Any:  # pylint:disable=invalid-name
    """Encode an object to JSON"""
    if isinstance(o, datetime.datetime):
        return o.isoformat(timespec="milliseconds")

    if isinstance(o, datetime.date):
        return o.isoformat()

    if isinstance(o, decimal.Decimal):
        return float(o)

    if isinstance(o, enum.Enum):
        return o.value

    if isinstance(o, set):
        return list(o)

    return str(o)
