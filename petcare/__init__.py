from flask import Flask
from petcare.database import Database

app = Flask(__name__)

# Pembuatan Database
Database.create_tb_user()

from petcare import views
