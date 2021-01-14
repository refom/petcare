# petcare/user.py


# Kelas Parent | Orang
class Orang(object):
	def __init__(self, id, name, email, phone, alamat, birthday):
		self.__id = id
		self.name = name
		self.__email = email
		self.phone = phone
		self.alamat = alamat
		self.birthday = birthday

	@property
	def id(self):
		pass

	@id.getter
	def id(self):
		return self.__id

	def __str__(self):
		return f"{self.name} is Default"

# ================================= INHERITANCE

# Kelas Anak | Dokter
class Dokter(Orang):
	def __init__(self, id, name, email, phone, alamat, birthday):
		super().__init__(id, name, email, phone, alamat, birthday)
		self.__role = "Dokter"
		self.jam_online = "00.00"

	def __str__(self):
		return f"{self.name} is {self.__role}"


# Kelas Anak | Pelanggan
class Pelanggan(Orang):

	def __init__(self, id, name, email, phone, alamat, birthday):
		super().__init__(id, name, email, phone, alamat, birthday)
		self.__role = "Pelanggan"
		self.__pet = []

	def __str__(self):
		return f"{self.name} is {self.__role}"

	@property
	def pet(self):
		pass
	
	@pet.getter
	def pet(self):
		return self.pet
	
	@pet.setter
	def pet(self, input):
		self.__pet.append(input)
