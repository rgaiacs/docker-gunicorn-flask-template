VERSION = "0.0.1"

from flask import Flask
from dummy.views import index_page

app = Flask(__name__)
app.register_blueprint(index_page)
