from flask import render_template, url_for, request, redirect, flash
from petcare import app
from petcare.database import Database
from petcare.models import User

db = Database()
user_login = []

@app.route("/")
def index():
	if user_login:
		return redirect(url_for('Menu'))
	return render_template('login.html')

@app.route("/", methods=['POST'])
def Login():
	# NGAMBIL DATA
	email = request.form['email']
	password = request.form['password']

	try:
		# CARI APAKAH ADA USERNYA
		user_data = db.compare_user(email, password)[0]
		user = User(user_data[1], user_data[4], user_data[5], user_data[6], user_data[2])
		
		# KALAU SUDAH ADA YG LOGIN, PAKSA KELUAR TRUS LOGIN YG BARU
		if user_login:
			user_login.clear()
		user_login.append(user)

	# KLO ADA ERROR YA GAK DIKASI MASUK
	except:
		print("gagal dapetin user")
		return redirect(request.url)

	return redirect(url_for('Menu'))

@app.route("/regis")
def RegisPage():
	return render_template('register.html')

@app.route("/regis", methods=['POST'])
def Register():
	try:
		nama = request.form['i_nama']
		phone = request.form['i_tel']
		alamat = request.form['i_alamat']
		birthday = request.form['i_birthday']
		email = request.form['i_email']
		password = request.form['i_password']

		# Insert ke database
		db.insert_tb_user(nama, email, password, phone, alamat, birthday)
	except:
		return redirect(request.url)

	return render_template('regis_success.html')


@app.route("/menu")
def Menu():
	if not user_login:
		return redirect(url_for('index'))
	user = user_login[0]
	return render_template('menu.html', user=user)

@app.route("/logout")
def Logout():
	if user_login:
		user_login.clear()
	return redirect(url_for('index'))



