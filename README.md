# common_flask_json_encoder

A JSON encoder that extends `FlaskJSONEncoder` and supports common data types


```
from common_flask_json_encoder import Encoder as JSONEncoder


def create_app() -> Flask:
    """ In your facotry function """
    app = Flask(__name__)

    app.json_encoder = JSONEncoder

    return app

```
