from flask import Flask

app = Flask(__name__)

from petcare import views
