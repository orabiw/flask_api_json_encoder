""" JSON encoder. """
import datetime
import decimal
import enum
import typing as t

import flask.json


class JSONEncoder(flask.json.provider.DefaultJSONProvider):
    """A JSON encoder for common types for flask"""

    types: t.Dict[t.Type, t.Callable[[t.Any], t.Any]] = {
        datetime.datetime: lambda obj: obj.isoformat(timespec="milliseconds"),
        datetime.date: lambda obj: obj.isoformat(),
        decimal.Decimal: float,
        enum.Enum: lambda obj: obj.value,
        set: list,
    }

    # a simple cache to reduce the number of look ups
    cache: t.Dict[t.Type, t.Callable[[t.Any], t.Any]] = {}

    @classmethod
    def default(cls, o: t.Any) -> t.Any:  # pylint:disable=invalid-name
        """Encode an object to JSON"""
        obj_type = type(o)

        if obj_type in cls.cache:
            return cls.cache[obj_type](o)

        for data_type, encoder in cls.types.items():
            if isinstance(o, data_type):
                cls.cache[obj_type] = encoder
                return encoder(o)

        cls.cache[obj_type] = str
        return str(o)

    def dumps(self, obj: t.Any, **kwargs: t.Any) -> str:
        return super().dumps(obj, default=JSONEncoder.default, **kwargs)
