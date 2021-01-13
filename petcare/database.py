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
					id INT PRIMARY KEY,
					name TEXT NOT NULL,
					email TEXT NOT NULL UNIQUE,
					password TEXT NOT NULL,
					phone TEXT NOT NULL,
					alamat TEXT NOT NULL,
					birthday TEXT NOT NULL
					)
			""")
			conn.commit()
	
	def insert_tb_user(self, nama, email, password, phone, alamat, birthday):
		with sqlite3.connect(self.db) as conn:
			c = conn.cursor()
			c.execute(""" INSERT INTO user(name, email, password, phone, alamat, birthday) VALUES (?, ?, ?, ?, ?, ?) """,
				[(nama), (email), (password), (phone), (alamat), (birthday)]
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
	
	def __str__(self):
		return self.db
	



