# petcare/views.py

# Import Flask
from flask import render_template, url_for, request, redirect, flash

# Import app petcare
from petcare import app
from petcare.models import LoginForm, RegisForm, LoginSession, ChatForm

login_session = LoginSession()

# ============================= Sebelum Login
# Halaman Login dan Halaman Default/Utama
@app.route("/")
def index():

	# Periksa apakah sudah masuk atau belum
	if login_session.check():
		return render_template('login.html')
	return redirect(url_for('Menu'))


# Jika user mencoba Login
@app.route("/", methods=['POST'])
def Login():

	login_form = LoginForm(request.form)

	if login_form.validasi():
		# Membuat objek user
		user = login_form.make_obj()

		# Menyimpan sesi login
		login_session.set_user(user)
		return redirect(url_for('Menu'))

	# Jika ada error atau gagal login, akan tetap berada di halaman saat itu
	return redirect(request.url)


# Halaman Register
@app.route("/regis")
def RegisPage():
	return render_template('register.html')


# Jika user mencoba Register
@app.route("/regis", methods=['POST'])
def Register():

	regis_form = RegisForm(request.form)

	# Register validasi
	if regis_form.validasi():
		return render_template('regis_success.html')
	return redirect(request.url)


# ============================= Setelah Login

# Halaman Menu/Feature
@app.route("/menu")
def Menu():
	# Kalau user belum login, akan kembali ke Halaman default/login
	if login_session.check():
		return redirect(url_for('index'))
	user = login_session.get_user()

	return render_template('menu.html', user=user)


# Halaman untuk keluar
@app.route("/logout")
def Logout():
	if not login_session.check():
		login_session.set_user(None)
	return redirect(url_for('index'))


# Halaman menu chat | Menampilkan list dokter yang ada
@app.route("/chat")
def ChatMenu():
	# Kalau user belum login, akan kembali ke Halaman default/login
	if login_session.check():
		return redirect(url_for('index'))

	# Mencari semua dokter lalu menyimpannya dalam class
	ChatForm.find_all()

	# Mengambil list dokter
	list_dokter = ChatForm.get_list_dokter()

	return render_template('chat_menu.html', list_dokter=list_dokter)

# Halaman chat | Terjadinya chat antara pelanggan dengan dokter
@app.route("/chat/<idDokter>")
def Chat(idDokter):
	# Kalau user belum login, akan kembali ke Halaman default/login
	if login_session.check():
		return redirect(url_for('index'))

	# Ambil objek dokter berdasarkan id
	dokter = ChatForm.get_dokter_by_id(idDokter)

	if dokter:
		return render_template('chat.html', dokter=dokter)
	return redirect(url_for('ChatMenu'))


