import sqlite3

class Database(object):
	def __init__(self):
		self.db = 'petcare.db'
		self.create_tb_user()
	
	def create_tb_user(self):
		with sqlite3.connect(self.db) as conn:
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
	
	def insert_tb_user(self, user_data):
		with sqlite3.connect(self.db) as conn:
			c = conn.cursor()
			c.execute(""" INSERT INTO user(name, phone, alamat, birthday, email, password, role) VALUES (?, ?, ?, ?, ?, ?, ?) """,
				[(user_data[0]), (user_data[1]), (user_data[2]), (user_data[3]), (user_data[4]), (user_data[5]), (user_data[6])]
			)
			conn.commit()

	def compare_user(self, email, password):
		with sqlite3.connect(self.db) as conn:
			c = conn.cursor()
			c.execute("""
				SELECT * FROM user WHERE email=? AND password=?
			""", [(email), (password)]
			)
			return c.fetchall()
	
	def get_dokter(self):
		with sqlite3.connect(self.db) as conn:
			c = conn.cursor()
			c.execute("""
				SELECT * FROM user WHERE role=2
			""")
			return c.fetchall()

	def __str__(self):
		return self.db
	



