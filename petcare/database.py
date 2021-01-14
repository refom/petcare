import sqlite3

# Kelas Database
class Database(object):

	# Class Variable | Nama Databasenya
	__db = 'petcare.db'


	# Class Method biar hanya bisa diakses oleh Kelas, bukan Objek
	@classmethod
	def create_tb_user(cls):
		with sqlite3.connect(cls.__db) as conn:
			c = conn.cursor()
			c.execute("""
				CREATE TABLE IF NOT EXISTS user (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					name TEXT NOT NULL,
					phone TEXT NOT NULL,
					alamat TEXT NOT NULL,
					birthday TEXT NOT NULL,
					email TEXT NOT NULL UNIQUE,
					password TEXT NOT NULL,
					role TEXT NOT NULL
					)
			""")
			conn.commit()
	
	@classmethod
	def insert_tb_user(cls, user_data):
		with sqlite3.connect(cls.__db) as conn:
			c = conn.cursor()
			c.execute("""
				INSERT INTO user(name, phone, alamat, birthday, email, password, role) VALUES (?, ?, ?, ?, ?, ?, ?)
				""",
				[(data) for data in user_data]
			)
			conn.commit()

	@classmethod
	def compare_user(cls, email, password):
		with sqlite3.connect(cls.__db) as conn:
			c = conn.cursor()
			c.execute("""
				SELECT id, name, email, phone, alamat, birthday, role FROM user WHERE email=? AND password=?
			""", [(email), (password)]
			)
			return c.fetchall()
	
	@classmethod
	def get_all_dokter(cls):
		with sqlite3.connect(cls.__db) as conn:
			c = conn.cursor()
			c.execute("""
				SELECT id, name, email, phone, alamat, birthday FROM user WHERE role=2
			""")
			return c.fetchall()



