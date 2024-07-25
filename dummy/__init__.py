VERSION = "0.1.0"

from flask import Flask
from dummy.index_page import index_page

app = Flask(__name__)
app.register_blueprint(index_page)