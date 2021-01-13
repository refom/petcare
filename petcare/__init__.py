from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '45270fd9edf1d068cf42565bc04cbd01'
# Max 16 MB upload
app.config['MAX_CONTENT_LENGTH'] = 160 * 1024 * 1024

from petcare import views
