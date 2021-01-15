# petcare/models.py

# Import Database dan Kelas user
from petcare.database import Database
from petcare.user import Pelanggan, Dokter

# Import Abstrak Class
from abc import ABC, abstractmethod

# ================================== INTERFACE

# Kelas Abstrak | Blueprint untuk Login dan Register
class Form(ABC):

	def __init__(self, req):
		self.req = req

	@abstractmethod
	def validasi(self):
		pass

	# Property untuk membuat atribut menjadi seperti method
	@property
	@abstractmethod
	def req(self):
		pass


# Login
class LoginForm(Form):

	@Form.req.getter
	def req(self):
		return self.__req

	@req.setter
	def req(self, input):
		self.__req = input

	def validasi(self):
		# Mengambil data yang di input user
		email = self.req['email']
		password = self.req['password']

		try:
			# Mencari apakah user ada di database dan data yg di input sama
			user_data = Database.compare_user(email, password)[0]
		except:
			return False
		# Jika user ada, simpan data sementara
		self.user = user_data
		return True

	def make_obj(self):
		# Pembuatan objek Pelanggan jika user adalah Pelanggan
		if self.user[-1] == "1":
			return Pelanggan(self.user[0], self.user[1], self.user[2], self.user[3], self.user[4], self.user[5])
		
		# Pembuatan objek Dokter jika user adalah Dokter
		elif self.user[-1] == "2":
			return Dokter(self.user[0], self.user[1], self.user[2], self.user[3], self.user[4], self.user[5])


# Register
class RegisForm(Form):

	@Form.req.getter
	def req(self):
		return self.__req

	@req.setter
	def req(self, input):
		self.__req = input

	def validasi(self):
		# Mengambil data yang di input user
		user_data = []
		for nama in self.req:
			user_data.append(self.req[nama])

		try:
			# Insert ke database
			Database.insert_tb_user(user_data)
		except:
			return False
		return True


# Kelas Sesi
class LoginSession(object):
	
	def __init__(self):
		self.__user = None


	# Enkapsulasi
	def set_user(self, input):
		self.__user = input
	
	def get_user(self):
		return self.__user

	# Cek apakah ada yang login atau tidak
	def check(self):
		if self.__user == None:
			return True
		return False


# Chat Menu
class ChatForm(object):
	list_dokter = {}

	@classmethod
	def find_all(cls):
		all_dokter = Database.get_all_dokter()

		for data_dokter in all_dokter:
			dokter = Dokter(data_dokter[0], data_dokter[1], data_dokter[2], data_dokter[3], data_dokter[4], data_dokter[5])
			cls.list_dokter[dokter.id] = dokter

	@classmethod
	def get_list_dokter(cls):
		return cls.list_dokter

	@classmethod
	def get_dokter_by_id(cls, idDokter):
		try:
			dokter = cls.list_dokter[int(idDokter)]
		except:
			return None
		return dokter


# Profile
class ProfileForm(object):
	
	def __init__(self, req):
		self.req = req
	
	def update(self, user):
		nama = self.req['nama']
		phone = self.req['phone']
		alamat = self.req['alamat']
		id = user.id

		user.name = nama
		user.phone = phone
		user.alamat = alamat

		try:
			Database.update_user((nama, phone, alamat, id))
		except:
			return False
		return True











