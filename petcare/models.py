


# USER OBJEK
class User(object):
	def __init__(self, nama, phone, alamat, ttl, email):
		self.nama = nama
		self.alamat = alamat
		self.phone = phone
		self.ttl = ttl
		self.__email = email
	
	def set_email(self, email):
		self.__email = email

	def get_email(self):
		return self.__email
	
	def __str__(self):
		return self.nama









