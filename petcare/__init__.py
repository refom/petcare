# petcare/__init__.py

# import Modul Flask dan Database
from flask import Flask
from petcare.database import Database

# Membuat objek Flask sebagai app
app = Flask(__name__)

# Pembuatan Database
Database.create_tb_user()

from petcare import views
