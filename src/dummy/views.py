from flask import Blueprint, current_app

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index():
    current_app.logger.debug("A debug message")
    current_app.logger.info("An info message")
    current_app.logger.warning("A warning message")
    current_app.logger.error("An error message")
    current_app.logger.critical("A critical message")

    return {"status": "OK"}
