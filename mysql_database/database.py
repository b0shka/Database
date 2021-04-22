#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pymysql.cursors

try:
	db = pymysql.connect(host='localhost',
	                     user='',
	                     password='',
	                     database='server',
	                     charset='utf8mb4',
	                     cursorclass=pymysql.cursors.DictCursor)
	sql = db.cursor()

	mode_table = ''
	def create_new_table(name_table):
		sql.execute(f"""CREATE TABLE IF NOT EXISTS {name_table} (
		id INTEGER PRIMARY KEY NOT NULL,
		name VARCHAR(30) NOT NULL,
		last_name VARCHAR(50),
		middle_name VARCHAR(50),
		age VARCHAR(10),
		birth VARCHAR(20),
		city VARCHAR(50),
		address TEXT,
		user_index VARCHAR(10),
		place_work TEXT,
		education TEXT,
		home_phone VARCHAR(15),
		car TEXT,
		email VARCHAR(100),
		vk VARCHAR(100),
		instagram VARCHAR(100),
		other_social TEXT,
		number_phone VARCHAR(20),
		pasport TEXT,
		snils VARCHAR(30),
		hobby TEXT,
		telegram VARCHAR(50),
		relative TEXT,
		other_info TEXT);""")
		db.commit()

	sql.execute('SHOW TABLES;')
	if len(sql.fetchall()) == 0:
		create_new_table('users')
except pymysql.err.OperationalError:
	print('Сервер MySQL не запущен')

# Получение названия таблиц
def get_table():
	sql.execute('SHOW TABLES;')
	mode_table = sql.fetchall()[0]['Tables_in_server']
	return mode_table

def get_name_all_table():
	sql.execute('SHOW TABLES;')
	name_tables = sql.fetchall()
	return name_tables

# Получение основной информации из базы данных для вывода в listwidget
def get_main_data_users(name_table):
	request = f'SELECT id, name, last_name, middle_name FROM {name_table};'
	sql.execute(request)
	list_name_person = sql.fetchall()
	return list_name_person

# Получение данных при поиске по id
def get_info_search_id(name_table, user_id):
	request = f'SELECT id, name, last_name, middle_name FROM {name_table} WHERE id = {user_id};'
	sql.execute(request)
	list_user = sql.fetchall()
	return list_user

# Получение данных при поиске словами
def get_info_search(name_table):
	request = f"SELECT id, name, last_name, middle_name FROM {name_table};"
	sql.execute(request)
	list_user = sql.fetchall()
	return list_user

# Получение данных для вывода в listwidget
def get_info_search_listwidget(name_table, data):
	request = f'SELECT id, name, last_name, middle_name FROM {name_table} WHERE id = {data["id"]};'
	sql.execute(request)
	list_user = sql.fetchall()
	return list_user

# Удаление таблицы из БД
def delete_table(name_table):
	request = f"DROP TABLE {name_table};"
	sql.execute(request)
	db.commit()

# Определение наименьшего id
def generate_id(name_table):
	user_id = 1
	request = f"SELECT id FROM {name_table};"
	sql.execute(request)
	id_users = sql.fetchall()
	for i in id_users:
		if int(i['id']) == user_id:
			user_id += 1
		else:
			break
	return user_id

# Добавление пользователя в БД
def add_user_to_server(name_table, user_id, name, last_name, middle_name, age, birth, city, address, user_index, place_work, education, home_phone, car, email, vk, instagram, other_social, number_phone, pasport, snils, hobby, telegram, relative, other_info):
	request = f"INSERT INTO {name_table} (id, name, last_name, middle_name, age, birth, city, address, user_index, place_work, education, home_phone, car, email, vk, instagram, other_social, number_phone, pasport, snils, hobby, telegram, relative, other_info) VALUES ({user_id}, '{name}', '{last_name}', '{middle_name}', '{age}', '{birth}', '{city}', '{address}', '{user_index}', '{place_work}', '{education}', '{home_phone}', '{car}', '{email}', '{vk}', '{instagram}', '{other_social}', '{number_phone}', '{pasport}', '{snils}', '{hobby}', '{telegram}', '{relative}', '{other_info}');"
	sql.execute(request)
	db.commit()

# Получение информации для вывода в окне информации о пользователе
def get_info_for_window_info_person(name_table, user_id):
	request = f"SELECT name, last_name, middle_name, age, birth, city, address, user_index, place_work, education, home_phone, car, email, vk, instagram, other_social, number_phone, pasport, snils, hobby, telegram, relative, other_info FROM {name_table} WHERE id = {user_id};"
	sql.execute(request)
	list_info = sql.fetchone()
	return list_info

# Перемещение пользователя в другую таблицу
def move_user_to_other_table(title_people, mode_table, name_table, user_id, name, last_name, middle_name, age, birth, city, address, user_index, place_work, education, home_phone, car, email, vk, instagram, other_social, number_phone, pasport, snils, hobby, telegram, relative, other_info):
	request = f"INSERT INTO {name_table} (id, name, last_name, middle_name, age, birth, city, address, user_index, place_work, education, home_phone, car, email, vk, instagram, other_social, number_phone, pasport, snils, hobby, telegram, relative, other_info) VALUES ('{user_id}', '{name}', '{last_name}', '{middle_name}', '{age}', '{birth}', '{city}', '{address}', '{user_index}', '{place_work}', '{education}', '{home_phone}', '{car}', '{email}', '{vk}', '{instagram}', '{other_social}', '{number_phone}', '{pasport}', '{snils}', '{hobby}', '{telegram}', '{relative}', '{other_info}');"
	sql.execute(request)
	db.commit()
	request = f"DELETE FROM {mode_table} WHERE id = '{title_people[0]}';"
	sql.execute(request)
	db.commit()

# Сохранение изменений
def save_user(name_table, title_people, name, last_name, middle_name, age, birth, city, address, user_index, place_work, education, home_phone, car, email, vk, instagram, other_social, number_phone, pasport, snils, hobby, telegram, relative, other_info):
	request = f"UPDATE {name_table} SET name = '{name}', last_name = '{last_name}', middle_name = '{middle_name}', age = '{age}', birth = '{birth}', city = '{city}', address = '{address}', user_index = '{user_index}', place_work = '{place_work}', education = '{education}', home_phone = '{home_phone}', car = '{car}', email = '{email}', vk = '{vk}', instagram = '{instagram}', other_social = '{other_social}', number_phone = '{number_phone}', pasport = '{pasport}', snils = '{snils}', hobby = '{hobby}', telegram = '{telegram}', relative = '{relative}', other_info = '{other_info}' WHERE id = '{title_people[0]}'"
	sql.execute(request)
	db.commit()

# Удаление пользователя
def delete_user(name_table, title_people):
	request = f"DELETE FROM {name_table} WHERE id = '{title_people[0]}';"
	sql.execute(request)
	db.commit()