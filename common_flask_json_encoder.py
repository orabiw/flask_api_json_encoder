""" JSON encoder. """
from typing import Any

import datetime
import enum
from decimal import Decimal
from flask.json import JSONEncoder as FlaskJSONEncoder


class Encoder(FlaskJSONEncoder):
    """ A JSON encoder for common types for flask """
    # pylint:disable=too-few-public-methods

    def default(self, obj: Any) -> str:
        """ Encode an object to JSON """
        # pylint: disable=method-hidden,arguments-differ
        if isinstance(obj, datetime.datetime):
            return obj.isoformat(timespec='milliseconds')

        if isinstance(obj, datetime.date):
            return obj.isoformat()

        if isinstance(obj, Decimal):
            return float(obj)

        if isinstance(obj, enum.Enum):
            return obj.value

        if isinstance(obj, set):
            return list(obj)

        return super(Encoder, self).default(obj)
