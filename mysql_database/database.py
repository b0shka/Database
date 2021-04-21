#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pymysql.cursors

db = pymysql.connect(host='localhost',
                     user='',
                     password='',
                     database='server',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)
sql = db.cursor()
mode_table = ''

def create_new_table():
	sql.execute(f"""CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY NOT NULL,
	name VARCHAR(50) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	middle_name VARCHAR(100),
	age INT,
	birth DATE,
	city VARCHAR(50),
	address TEXT,
	user_index INT,
	place_work TEXT,
	education TEXT,
	home_phone INT,
	car TEXT,
	email VARCHAR(100),
	vk VARCHAR(100),
	instagram VARCHAR(100),
	other_social TEXT,
	number_phone INT,
	pasport TEXT,
	snils INT,
	hobby TEXT,
	telegram INT,
	relative TEXT,
	other_info TEXT);""")
	db.commit()

sql.execute('SHOW TABLES;')
if len(sql.fetchall()) == 0:
	create_new_table()

# Получение названия таблиц
def get_table():
	global mode_table
	sql.execute('SHOW TABLES;')
	mode_table = sql.fetchall()[0]['Tables_in_server']
	return mode_table

def get_name_all_table():
	sql.execute('SHOW TABLES;')
	name_tables = sql.fetchall()
	return name_tables

# Получение основной информации из базы данных для вывода в listwidget
def get_main_data_users():
	request = f'SELECT id, name, last_name, middle_name FROM {mode_table};'
	sql.execute(request)
	list_name_person = sql.fetchall()
	return list_name_person

# Получение данных при поиске по id
def get_info_search_id(user_id):
	request = f'SELECT id, name, last_name, middle_name FROM {mode_table} WHERE id = {user_id};'
	sql.execute(request)
	list_user = sql.fetchall()
	return list_user

# Получение данных при поиске словами
def get_info_search():
	request = f"SELECT id, name, last_name, middle_name FROM {mode_table};"
	sql.execute(request)
	list_user = sql.fetchall()
	return list_user

# Получение данных для вывода в listwidget
def get_info_search_listwidget(data):
	request = f'SELECT id, name, last_name, middle_name FROM {mode_table} WHERE id = {data["id"]};'
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
def add_user(name_table, user_id, name, last_name, middle_name, age, birth, city, address, user_index, place_work, education, home_phone, car, email, vk, instagram, other_social, number_phone, pasport, snils, hobby, telegram, relative, other_info):
	#request = f"INSERT INTO {name_table} SET id={user_id}, name='{name}', last_name='{last_name}', middle_name='{middle_name}', age='{age}', birth='{birth}', city='{city}', address='{address}', user_index='{user_index}', place_work='{place_work}', education='{education}', home_phone='{home_phone}', car='{car}', email='{email}', vk='{vk}', instagram='{instagram}', other_social='{other_social}', number_phone='{number_phone}', pasport='{pasport}', snils='{snils}', hobby='{hobby}', telegram='{telegram}', relative='{relative}', other_info='{other_info}';"
	if last_name == '':
		last_name = 'null'
	if middle_name == '':
		middle_name = 'null'
	if age == '':
		age = 'null'
	if birth == '':
		birth = 'null'
	if city == '':
		city = 'null'
	if address == '':
		address = 'null'
	if user_index == '':
		user_index = 'null'
	if place_work == '':
		place_work = 'null'
	if education == '':
		education = 'null'
	if home_phone == '':
		home_phone = 'null'
	if car == '':
		car = 'null'
	if email == '':
		email = 'null'
	if vk == '':
		vk = 'null'
	if instagram == '':
		instagram = 'null'
	if other_social == '':
		other_social = 'null'
	if number_phone == '':
		number_phone = 'null'
	if pasport == '':
		pasport = 'null'
	if snils == '':
		snils = 'null'
	if hobby == '':
		hobby = 'null'
	if telegram == '':
		telegram = 'null'
	if relative == '':
		relative = 'null'
	if other_info == '':
		other_info = 'null'
	request = f"INSERT INTO {name_table} (id, name, last_name, middle_name, age, birth, city, address, user_index, place_work, education, home_phone, car, email, vk, instagram, other_social, number_phone, pasport, snils, hobby, telegram, relative, other_info) VALUES ({user_id}, {name}, {last_name}, {middle_name}, {age}, {birth}, {city}, {address}, {user_index}, {place_work}, {education}, {home_phone}, {car}, {email}, {vk}, {instagram}, {other_social}, {number_phone}, {pasport}, {snils}, {hobby}, {telegram}, {relative}, {other_info});"
	print(request)
	sql.execute(request)
	db.commit()