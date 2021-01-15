# petcare/__init__.py

# import Modul Flask dan Database
from flask import Flask
from petcare.database import Database

# Membuat objek Flask sebagai app
app = Flask(__name__)
app.config['SECRET_KEY'] = '45270fd9edf1d068cf42565bc04cbd01'

# Pembuatan Database
Database.create_tb_user()

from petcare import views
