""" JSON encoder. """
import datetime
import decimal
import enum
import typing as t

import flask.json


class JSONEncoder(flask.json.provider.DefaultJSONProvider):
    """A JSON encoder for common types for flask"""

    types: t.Dict[t.Type, t.Callable[[t.Any], t.Any]] = {
        datetime.datetime: lambda o: o.isoformat(timespec="milliseconds"),
        datetime.date: lambda o: o.isoformat(),
        decimal.Decimal: float,
        enum.Enum: lambda o: o.value,
        set: list,
    }

    @classmethod
    def default(cls, o: t.Any) -> t.Any:  # pylint:disable=invalid-name
        """Encode an object to JSON"""
        for data_type, encoder in cls.types.items():
            if isinstance(o, data_type):
                return encoder(o)

        return str(o)

    def dumps(self, obj: t.Any, **kwargs: t.Any) -> str:
        return super().dumps(obj, default=JSONEncoder.default, **kwargs)
