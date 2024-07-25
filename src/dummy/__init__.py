VERSION = "0.0.1"

from logging.config import dictConfig

from flask import Flask

from dummy.views import index_page

dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "stream": "ext://sys.stdout",  # https://docs.python.org/3/library/logging.config.html#access-to-external-objects
            },
        },
        "loggers": {
            "gunicorn.error": {
                "handlers": ["wsgi"],
                "level": "INFO",
                "propagate": False,
            },
            "gunicorn.access": {
                "handlers": ["wsgi"],
                "level": "INFO",
                "propagate": False,
            },
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

app = Flask(__name__)
app.register_blueprint(index_page)
