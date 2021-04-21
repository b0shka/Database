#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from database import *
from style import main
from style import about_person
from style import new_table

# Основное окно
class Database(QtWidgets.QMainWindow, main.Ui_Database_user):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setIcon()
		self.click_button()
		self.get_name_table()
		self.filter()
		self.mode_table = get_table()
		self.add_name_person()

	# Добавление фотографии
	def setIcon(self):
		self.appIcon = QIcon('icon/icon.png')
		self.setWindowIcon(self.appIcon)

	# Вызов функций при нажатии кнопок
	def click_button(self):
		self.pushButton.clicked.connect(self.add_user)
		self.pushButton_2.clicked.connect(self.search_result)
		self.pushButton_3.clicked.connect(self.drop_search)
		self.pushButton_10.clicked.connect(self.create_table)
		self.pushButton_12.clicked.connect(self.delete_table)
		self.listWidget.itemDoubleClicked.connect(self.open_info)
		self.listWidget_2.itemDoubleClicked.connect(self.open_other_table)
		self.lineEdit.returnPressed.connect(self.search_result)

	def keyPressEvent(self, e):
		if e.key() == Qt.Key_Escape:
			self.close()

	# Добавление пользователей в список
	def add_name_person(self):
		data = get_main_data_users()
		for i in data:
			if len(str(i['id'])) == 1:
				num1 = str(i['id']) + '    '
			elif len(str(i['id'])) == 2:
				num1 = str(i['id']) + '  '

			if len(str(i['name'])) <= 5:
				num2 = i['name'] + '\t\t'
			else:
				num2 = i['name'] + '\t'

			if len(str(i['last_name'])) >= 8:
				if len(str(i['last_name'])) >= 17:
					num3 = i['last_name'] + '\t'
				else:
					num3 = i['last_name'] + '\t\t'
			else:
					num3 = i['last_name'] + '\t\t\t'

			num4 = i['middle_name']
			result = str(num1) + str(num2) + str(num3) + str(num4)
			self.listWidget.addItem(f"{result}")

	# Поиск слова с ошибкой
	def valid_name(self, search_name, name_main):
		if len(search_name) == len(name_main):
			number = 0
			for i in range(len(name_main)):
				if search_name[i] != name_main[i]:
					number += 1
			if number <= 2:
				return 1
			else:
				return 0
		else:
			return 0

	# Вывод результата поиска
	def search_result(self):
		text = self.lineEdit.text().title().split(' ')
		global result_search
		result_search = []
		if self.lineEdit.text() == '':
			self.listWidget.clear()
			self.add_name_person()

		elif len(text) == 1 and f"{text[0]}".isdigit():
			user_id = text[0]
			self.lineEdit.setText("")
			self.listWidget.clear()
			result_user = get_info_search_id(user_id)
			for i in result_user:
				if len(str(i['id'])) == 1:
					num1 = str(i['id']) + '    '
				elif len(str(i['id'])) == 2:
					num1 = str(i['id']) + '  '

				if len(str(i['name'])) <= 5:
					num2 = i['name'] + '\t\t'
				else:
					num2 = i['name'] + '\t'

				if len(str(i['last_name'])) >= 8:
					if len(str(i['last_name'])) >= 17:
						num3 = i['last_name'] + '\t'
					else:
						num3 = i['last_name'] + '\t\t'
				else:
					num3 = i['last_name'] + '\t\t\t'

				num4 = i['middle_name']
				result = str(num1) + str(num2) + str(num3) + str(num4)
				self.listWidget.addItem(f"{result}")

		elif len(text) == 1:
			self.lineEdit.setText("")
			self.listWidget.clear()
			result_user = get_info_search()
			for i in result_user:
				if self.valid_name(text[0], i['name']) == 1 or self.valid_name(text[0], i['last_name']) == 1 or self.valid_name(text[0], i['middle_name']) == 1:
					result_search.append(i)
				elif str(text[0]) in str(i['name']) or str(text[0]) in str(i['last_name']) or str(text[0]) in str(i['middle_name']):
					result_search.append(i)
			self.add_result_search(result_search)

		elif len(text) == 2:
			self.lineEdit.setText("")
			self.listWidget.clear()
			result_user = get_info_search()
			for i in result_user:
				n = 0
				if self.valid_name(text[0], i['name']) == 1 and self.valid_name(text[1], i['last_name']) == 1 or self.valid_name(text[0], i['name']) == 1 and self.valid_name(text[1], i['middle_name']) == 1:
					n += 1
				elif self.valid_name(text[0], i['last_name']) == 1 and self.valid_name(text[1], i['name']) == 1 or self.valid_name(text[0], i['last_name']) == 1 and self.valid_name(text[1], i['middle_name']) == 1:
					n += 1
				elif self.valid_name(text[0], i['middle_name']) == 1 and self.valid_name(text[1], i['name']) == 1 or self.valid_name(text[0], i['middle_name']) == 1 and self.valid_name(text[1], i['last_name']) == 1:
					n += 1
				elif str(text[0]) in str(i['name']) and str(text[1]) in str(i['last_name']):
					n += 1
				elif str(text[0]) in str(i['name']) and str(text[1]) in str(i['middle_name']):
					n += 1
				elif str(text[0]) in str(i['last_name']) and str(text[1]) in str(i['name']):
					n += 1
				elif str(text[0]) in str(i['last_name']) and str(text[1]) in str(i['middle_name']):
					n += 1
				elif str(text[0]) in str(i['middle_name']) and str(text[1]) in str(i['name']):
					n += 1
				elif str(text[0]) in str(i['middle_name']) and str(text[1]) in str(i['last_name']):
					n += 1

				if n > 0:
					if i not in result_search:
						result_search.append(i)
			self.add_result_search(result_search)

		elif len(text) == 3 and not(f"{text[0]}".isdigit()):
			n = 0
			self.lineEdit.setText("")
			self.listWidget.clear()
			result_user = get_info_search()
			for i in result_user:
				n = 0
				if self.valid_name(text[0], i[1]) == 1 and self.valid_name(text[1], i[2]) == 1 and self.valid_name(text[2], i[3]) == 1:
					n += 1
				elif self.valid_name(text[0], i[1]) == 1 and self.valid_name(text[1], i[3]) == 1 and self.valid_name(text[2], i[2]) == 1:
					n += 1
				elif self.valid_name(text[0], i[2]) == 1 and self.valid_name(text[1], i[1]) == 1 and self.valid_name(text[2], i[3]) == 1:
					n += 1
				elif self.valid_name(text[0], i[2]) == 1 and self.valid_name(text[1], i[3]) == 1 and self.valid_name(text[2], i[1]) == 1:
					n += 1
				elif self.valid_name(text[0], i[3]) == 1 and self.valid_name(text[1], i[1]) == 1 and self.valid_name(text[2], i[2]) == 1:
					n += 1
				elif self.valid_name(text[0], i[3]) == 1 and self.valid_name(text[1], i[2]) == 1 and self.valid_name(text[2], i[1]) == 1:
					n += 1
				elif str(text[0]) in str(i[1]) and str(text[1]) in str(i[2]) and str(text[2]) in str(i[3]):
					n += 1
				elif str(text[0]) in str(i[1]) and str(text[1]) in str(i[3]) and str(text[2]) in str(i[2]):
					n += 1
				elif str(text[0]) in str(i[2]) and str(text[1]) in str(i[1]) and str(text[2]) in str(i[3]):
					n += 1
				elif str(text[0]) in str(i[2]) and str(text[1]) in str(i[3]) and str(text[2]) in str(i[1]):
					n += 1
				elif str(text[0]) in str(i[3]) and str(text[1]) in str(i[1]) and str(text[2]) in str(i[2]):
					n += 1
				elif str(text[0]) in str(i[3]) and str(text[1]) in str(i[2]) and str(text[2]) in str(i[1]):
					n += 1

				if n > 0:
					if i not in result_search:
						result_search.append(i)
			self.add_result_search(result_search)

		else:
			self.lineEdit.setText("")

	# Добавление результата поиска в программу
	def add_result_search(self, result_search):
		for data in result_search:
			person_data = get_info_search_listwidget(data)
			for i in person_data:
				if len(str(i['id'])) == 1:
					num1 = str(i['id']) + '    '
				elif len(str(i['id'])) == 2:
					num1 = str(i['id']) + '  '

				if len(str(i['name'])) <= 5:
					num2 = i['name'] + '\t\t'
				else:
					num2 = i['name'] + '\t'

				if len(str(i['last_name'])) >= 8:
					if len(str(i['last_name'])) >= 17:
						num3 = i['last_name'] + '\t'
					else:
						num3 = i['last_name'] + '\t\t'
				else:
					num3 = i['last_name'] + '\t\t\t'

				num4 = i['middle_name']
				result = str(num1) + str(num2) + str(num3) + str(num4)
				self.listWidget.addItem(result)
		result_search = []

	# Очищение результата поиска
	def drop_search(self):
		self.listWidget.clear()
		self.add_name_person()
		self.listWidget_2.clear()
		self.get_name_table()
		self.comboBox.clear()
		self.filter()

	# Очищение всех полей при создании нового пользователя
	def clean_all(self):
		self.lineEdit_2.setText("")
		self.lineEdit_3.setText("")
		self.lineEdit_4.setText("")
		self.lineEdit_5.setText("")
		self.lineEdit_6.setText("")
		self.lineEdit_7.setText("")
		self.lineEdit_8.setText("")
		self.lineEdit_9.setText("")
		self.lineEdit_10.setText("")
		self.lineEdit_11.setText("")
		self.lineEdit_12.setText("")
		self.lineEdit_13.setText("")
		self.lineEdit_14.setText("")
		self.lineEdit_15.setText("")
		self.lineEdit_16.setText("")
		self.lineEdit_17.setText("")
		self.lineEdit_18.setText("")
		self.lineEdit_19.setText("")
		self.textEdit_1.setText("")
		self.textEdit_2.setText("")
		self.textEdit_3.setText("")
		self.textEdit_4.setText("")
		self.textEdit_5.setText("")

	# Вывод названий таблиц
	def get_name_table(self):
		name_tables = get_name_all_table()
		for i in name_tables:
			self.listWidget_2.addItem(i['Tables_in_server'])

	# При нажатии на название таблицы вывести ее содержание
	def open_other_table(self, item):
		self.listWidget.clear()
		self.mode_table = item.text()
		self.add_name_person()

	# Создание новой таблицы
	def create_table(self):
		self.table = new_table()
		self.table.show()

	# Удаление таблицы
	def delete_table(self):
		user_true = QMessageBox.question(self, 'Удалить', 'Вы действительно хотите удалить?', QMessageBox.Yes | QMessageBox.No)
		if user_true == QMessageBox.Yes:
			tables = get_name_all_table()
			if len(tables) == 1:
				QMessageBox.information(self.pushButton, 'Уведомление', 'Таблица не может быть удалена, так как она последняя')
			else:
				delete_table(self.mode_table)
				get_table()
				self.drop_search()
		elif user_true == QMessageBox.No:
			pass

	# Добавление в фильтр название таблиц
	def filter(self):
		name_tables = get_name_all_table()
		for i in name_tables:
			self.comboBox.addItem(i['Tables_in_server'])

	# Получение данных из строк и добаление их в базу данных
	def add_user(self):
		name_table = self.comboBox.currentText()
		user_id = generate_id(name_table)
		name = self.lineEdit_2.text().title()

		if name == '':
			lock_style_form = """
			padding:2px 5px;
			font-size: 14px;
			height: 28px;
			color: white;
			background-color: #404040;
			border: 2px solid #f5a2a2;
			border-radius: 5px;
			"""
			self.lineEdit_2.setStyleSheet(lock_style_form)
			#QMessageBox.information(self.pushButton, 'Уведомление', 'Заполните имя')
		else:
			default_style_form = """
			padding:2px 5px;
			font-size: 14px;
			height: 28px;
			color: white;
			background-color: #404040;
			border-radius: 5px;
			"""
			self.lineEdit_2.setStyleSheet(default_style_form)

			last_name = self.lineEdit_3.text().title()
			middle_name = self.lineEdit_4.text().title()
			age = self.lineEdit_5.text()
			birth = self.lineEdit_6.text()
			city = self.lineEdit_7.text().title()
			address = self.lineEdit_8.text().title()
			user_index = self.lineEdit_9.text()
			place_work = self.lineEdit_10.text()
			education = self.textEdit_1.toPlainText()
			home_phone = self.lineEdit_11.text()
			car = self.lineEdit_12.text().title()
			email = self.lineEdit_13.text()
			vk = self.lineEdit_14.text()
			instagram = self.lineEdit_15.text()
			other_social = self.textEdit_2.toPlainText()
			number_phone = self.lineEdit_16.text()
			pasport = self.textEdit_3.toPlainText()
			snils = self.lineEdit_17.text()
			hobby = self.lineEdit_18.text().title()
			telegram = self.lineEdit_19.text()
			relative = self.textEdit_4.toPlainText()
			other_info = self.textEdit_5.toPlainText()

			add_user(name_table, user_id, name, last_name, middle_name, age, birth, city, address, user_index, place_work, education, home_phone, car, email, vk, instagram, other_social, number_phone, pasport, snils, hobby, telegram, relative, other_info)
			QMessageBox.information(self.pushButton, 'Уведомление', 'Запись успешно создана!')

			self.listWidget.clear()
			self.add_name_person()
			self.clean_all()

	# Открытие информации о человеке
	def open_info(self, item):
		global title_people
		global mode_table
		mode_table = self.mode_table
		print(mode_table)
		title_people = item.text().split()
		self.person = Info_window()
		self.person.show()


# Окно с информацией о человеке
class Info_window(QtWidgets.QMainWindow, about_person.Ui_mainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setIcon()
		self.click_button()
		self.add_label()
		self.add_info()
		self.filter()

	# Добавление фотографии
	def setIcon(self):
		self.person_icon = QIcon('icon/icon_person.png')
		self.setWindowIcon(self.person_icon)

	# Добавление заголовка
	def add_label(self):
		try:
			if title_people[1][0] in "АОЭЕИУЁЮЯ":
				self.label.setText('Информация об ' + str(title_people[1]) + ' ' + str(title_people[2]))
			else:
				self.label.setText('Информация о ' + str(title_people[1]) + ' ' + str(title_people[2]))
		except IndexError:
			if title_people[1][0] in "АОЭЕИУЁЮЯ":
				self.label.setText('Информация об ' + str(title_people[1]))
			else:
				self.label.setText('Информация о ' + str(title_people[1]))

	# Кнопка сохранения измененных данных
	def save_user(self):
		name = self.lineEdit_200.text().title()
		if name == '':
			lock_style_form = """
			padding:2px 5px;
			font-size: 14px;
			height: 28px;
			color: white;
			background-color: #404040;
			border: 2px solid #f5a2a2;
			border-radius: 5px;
			"""
			self.lineEdit_200.setStyleSheet(lock_style_form)
			#QMessageBox.information(self.pushButton_6, 'Уведомление', 'Заполните имя')
		else:
			default_style_form = """
			padding:2px 5px;
			font-size: 14px;
			height: 28px;
			color: white;
			background-color: #404040;
			border-radius: 5px;
			"""
			self.lineEdit_200.setStyleSheet(default_style_form)

			last_name = self.lineEdit_201.text().title()
			middle_name = self.lineEdit_202.text().title()
			age = self.lineEdit_203.text()
			birth = self.lineEdit_204.text()
			city = self.lineEdit_205.text().title()
			address = self.lineEdit_206.text().title()
			user_index = self.lineEdit_207.text()
			place_work = self.lineEdit_208.text()
			education = self.textEdit_1.toPlainText()
			home_phone = self.lineEdit_209.text()
			car = self.lineEdit_210.text().title()
			email = self.lineEdit_211.text()
			vk = self.lineEdit_212.text()
			instagram = self.lineEdit_213.text()
			other_social = self.textEdit_2.toPlainText()
			number_phone = self.lineEdit_214.text()
			pasport = self.textEdit_3.toPlainText()
			snils = self.lineEdit_215.text()
			hobby = self.lineEdit_216.text().title()
			telegram = self.lineEdit_217.text().title()
			relative = self.textEdit_4.toPlainText()
			other_info = self.textEdit_5.toPlainText()

			sql.execute(f"UPDATE '{mode_table}' SET name = '{name}', last_name = '{last_name}', middle_name = '{middle_name}', age = '{age}', birth = '{birth}', city = '{city}', address = '{address}', user_index = '{user_index}', place_work = '{place_work}', education = '{education}', home_phone = '{home_phone}', car = '{car}', email = '{email}', vk = '{vk}', instagram = '{instagram}', other_social = '{other_social}', number_phone = '{number_phone}', pasport = '{pasport}', snils = '{snils}', hobby = '{hobby}', telegram = '{telegram}', relative = '{relative}', other_info = '{other_info}' WHERE id = '{title_people[0]}'")
			db.commit()
			QMessageBox.information(self.pushButton_6, 'Уведомление', 'Сохранение успешно завершено')
			self.close()

	# Удаление записи пользователя
	def delete_user(self):
		user_true = QMessageBox.question(self, 'Удалить', 'Вы действительно хотите удалить?', QMessageBox.Yes | QMessageBox.No)
		if user_true == QMessageBox.Yes:
			sql.execute(f"DELETE FROM '{mode_table}' WHERE id = '{title_people[0]}'")
			db.commit()
			self.close()
		elif user_true == QMessageBox.No:
			pass

	# Добавления в поля информации из базы данных
	def add_info(self):
		sql.execute(f"SELECT name, last_name, middle_name, age, birth, city, address, user_index, place_work, education, home_phone, car, email, vk, instagram, other_social, number_phone, pasport, snils, hobby, telegram, relative, other_info FROM '{mode_table}' WHERE id = '{title_people[0]}'")

		people_info = sql.fetchone()

		self.lineEdit_200.setText(people_info[0])
		self.lineEdit_201.setText(people_info[1])
		self.lineEdit_202.setText(people_info[2])
		self.lineEdit_203.setText(str(people_info[3]))
		self.lineEdit_204.setText(str(people_info[4]))
		self.lineEdit_205.setText(people_info[5])
		self.lineEdit_206.setText(str(people_info[6]))
		self.lineEdit_207.setText(str(people_info[7]))
		self.lineEdit_208.setText(people_info[8])
		self.textEdit_1.setText(str(people_info[9]))
		self.lineEdit_209.setText(str(people_info[10]))
		self.lineEdit_210.setText(people_info[11])
		self.lineEdit_211.setText(people_info[12])
		self.lineEdit_212.setText(people_info[13])
		self.lineEdit_213.setText(str(people_info[14]))
		self.textEdit_2.setText(str(people_info[15]))
		self.lineEdit_214.setText(str(people_info[16]))
		self.textEdit_3.setText(str(people_info[17]))
		self.lineEdit_215.setText(str(people_info[18]))
		self.lineEdit_216.setText(str(people_info[19]))
		self.lineEdit_217.setText(str(people_info[20]))
		self.textEdit_4.setText(people_info[21])
		self.textEdit_5.setText(people_info[22])

	# Перемещение пользователя в другую таблицу
	def move_user_to_other_table(self):
		name_table = self.comboBox.currentText()

		user_id = 1
		for i in sql.execute(f"SELECT id FROM '{name_table}';"):
			if int(i[0]) == user_id:
				user_id += 1
			else:
				break
		name = self.lineEdit_200.text().title()
		if name == '':
			QMessageBox.information(self.pushButton_5, 'Уведомление', 'Заполните имя и фамилию')
		else:
			last_name = self.lineEdit_201.text().title()
			middle_name = self.lineEdit_202.text().title()
			age = self.lineEdit_203.text()
			birth = self.lineEdit_204.text()
			city = self.lineEdit_205.text().title()
			address = self.lineEdit_206.text().title()
			user_index = self.lineEdit_207.text()
			place_work = self.lineEdit_208.text()
			education = self.textEdit_1.toPlainText()
			home_phone = self.lineEdit_209.text()
			car = self.lineEdit_210.text().title()
			email = self.lineEdit_211.text()
			vk = self.lineEdit_212.text()
			instagram = self.lineEdit_213.text()
			other_social = self.textEdit_2.toPlainText()
			number_phone = self.lineEdit_214.text()
			pasport = self.textEdit_3.toPlainText()
			snils = self.lineEdit_215.text()
			hobby = self.lineEdit_216.text().title()
			telegram = self.lineEdit_217.text().title()
			relative = self.textEdit_4.toPlainText()
			other_info = self.textEdit_5.toPlainText()

			sql.execute(f"INSERT INTO '{name_table}' (id, name, last_name, middle_name, age, birth, city, address, user_index, place_work, education, home_phone, car, email, vk, instagram, other_social, number_phone, pasport, snils, hobby, telegram, relative, other_info) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (user_id, name, last_name, middle_name, age, birth, city, address, user_index, place_work, education, home_phone, car, email, vk, instagram, other_social, number_phone, pasport, snils, hobby, telegram, relative, other_info))
			db.commit()
			sql.execute(f"DELETE FROM '{mode_table}' WHERE id = '{title_people[0]}'")
			db.commit()
			QMessageBox.information(self.pushButton_6, 'Уведомление', 'Перемещение успешно завершено')
			self.close()

	# Добавление в фильтр название таблиц
	def filter(self):
		for i in sql.execute('SELECT name FROM sqlite_master WHERE type = "table"'):
			self.comboBox.addItem(f"{i[0]}")

	# Вызов функций кнопок
	def click_button(self):
		self.pushButton_6.clicked.connect(self.save_user)
		self.pushButton_7.clicked.connect(self.delete_user)
		self.pushButton_8.clicked.connect(self.move_user_to_other_table)


# Окно для создания новой таблицы
class new_table(QtWidgets.QMainWindow, new_table.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setIcon()
		self.click_create()
		self.key_click()
		
	# Добавление фотографии
	def setIcon(self):
		self.person_icon = QIcon('icon/icon_table.png')
		self.setWindowIcon(self.person_icon)

	# Действия для клавиш
	def key_click(self):
		self.lineEdit_1.returnPressed.connect(self.create)

	def click_create(self):
		self.pushButton_1.clicked.connect(self.create)

	def create(self):
		table_name = self.lineEdit_1.text()
		if table_name == '':
			lock_style_form = """
			padding:2px 5px;
			font-size: 14px;
			height: 28px;
			color: white;
			background-color: #404040;
			border: 2px solid #f5a2a2;
			border-radius: 5px;
			"""
			self.lineEdit_1.setStyleSheet(lock_style_form)
		else:
			default_style_form = """
			padding:2px 5px;
			font-size: 14px;
			height: 28px;
			color: white;
			background-color: #404040;
			border-radius: 5px;
			"""
			self.lineEdit_1.setStyleSheet(default_style_form)

			names = []
			for i in sql.execute('SELECT name FROM sqlite_master WHERE type = "table"'):
				names.append(i[0])
			if table_name not in names:
				create_new_table(table_name)
			else:
				QMessageBox.information(self.pushButton_1, 'Уведомление', 'Таблица с таким названием уже существует')
			self.close()


if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  window = Database()
  window.show()
  sys.exit(app.exec_())