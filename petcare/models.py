


# USER OBJEK
class User(object):
	def __init__(self, id, nama, phone, alamat, ttl, email, role):
		self.id = id
		self.nama = nama
		self.alamat = alamat
		self.phone = phone
		self.ttl = ttl
		self.__email = email
		self.__role = role
	
	def set_email(self, email):
		self.__email = email

	def get_email(self):
		return self.__email
	
	def __str__(self):
		return self.nama

	def set_role(self, role):
		self.__role = role
	
	def get_role(self):
		return self.__role











