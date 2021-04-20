# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Database_user(object):
    def setupUi(self, Database_user):
        if not Database_user.objectName():
            Database_user.setObjectName(u"Database_user")
        Database_user.resize(863, 628)
        Database_user.setStyleSheet(u"background-color: #2a2a2a;")
        self.action = QAction(Database_user)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(Database_user)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 871, 631))
        self.tabWidget.setStyleSheet(u"background-color: #2a2a2a;\n"
"font-size: 13px;\n"
"color: white;")
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 211, 31))
        self.lineEdit.setStyleSheet(u"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;\n"
"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;")
        self.lineEdit.setClearButtonEnabled(True)
        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(230, 10, 91, 31))
        self.pushButton_2.setStyleSheet(u"font-size: 14px;\n"
"background-color: #404040;\n"
"color: white;\n"
"border-radius: 5px;")
        self.listWidget = QListWidget(self.tab)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 50, 671, 541))
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"	font-size:16px;\n"
"	background-color: #404040;\n"
"	color: white;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"	padding-top: 6px;\n"
"}")
        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(590, 10, 91, 31))
        self.pushButton_3.setStyleSheet(u"font-size: 14px;\n"
"background-color: #404040;\n"
"color: white;\n"
"border-radius: 5px;")
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(770, 20, 81, 21))
        font = QFont()
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"font-size: 18px;\n"
"color: white;")
        self.listWidget_2 = QListWidget(self.tab)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(690, 50, 161, 461))
        self.listWidget_2.setStyleSheet(u"QListWidget {\n"
"	font-size:16px;\n"
"	padding: 5px;\n"
"	background-color: #404040;\n"
"	color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"	padding-top: 5px;\n"
"}")
        self.pushButton_10 = QPushButton(self.tab)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(690, 520, 161, 31))
        self.pushButton_10.setStyleSheet(u"font-size:14px;\n"
"background-color: #404040;\n"
"border-radius: 5px;\n"
"color: white;")
        self.pushButton_12 = QPushButton(self.tab)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(690, 560, 161, 31))
        self.pushButton_12.setStyleSheet(u"font-size:14px;\n"
"background-color: #404040;\n"
"border-radius: 5px;\n"
"color: white;")
        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(490, 10, 91, 31))
        self.pushButton_4.setStyleSheet(u"font-size: 14px;\n"
"background-color: #404040;\n"
"color: white;\n"
"border-radius: 5px;")
        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(390, 10, 91, 31))
        self.pushButton_5.setStyleSheet(u"font-size: 14px;\n"
"background-color: #404040;\n"
"color: white;\n"
"border-radius: 5px;")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(750, 560, 101, 31))
        self.pushButton.setStyleSheet(u"font-size: 14px;\n"
"background-color: #404040;\n"
"color: white;\n"
"border-radius: 5px;")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 240, 151, 21))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: white;\n"
"font-size: 16px;")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 201, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: white;\n"
"font-size: 16px;")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(570, 10, 131, 21))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"font-size: 16px;\n"
"color: white;")
        self.comboBox = QComboBox(self.tab_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(390, 560, 161, 31))
        self.comboBox.setStyleSheet(u"font-size:14px;")
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(320, 530, 231, 20))
        self.label_10.setStyleSheet(u"font-size:15px;\n"
"color: white;")
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(570, 270, 101, 21))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"font-size: 16px;\n"
"color: white;")
        self.textEdit_5 = QTextEdit(self.tab_2)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(570, 300, 281, 231))
        self.textEdit_5.setStyleSheet(u"font-size:14px;\n"
"padding: 4px;\n"
"background-color: #404040;\n"
"color: white;\n"
"border-radius: 5px;")
        self.textEdit_4 = QTextEdit(self.tab_2)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(570, 40, 281, 221))
        self.textEdit_4.setStyleSheet(u"font-size:14px;\n"
"padding: 4px;\n"
"background-color: #404040;\n"
"color: white;\n"
"border-radius: 5px;")
        self.lineEdit_12 = QLineEdit(self.tab_2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(270, 200, 281, 32))
        self.lineEdit_12.setStyleSheet(u"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;\n"
"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;")
        self.lineEdit_9 = QLineEdit(self.tab_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(10, 320, 241, 32))
        self.lineEdit_9.setStyleSheet(u"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;\n"
"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;")
        self.lineEdit_4 = QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(10, 120, 241, 32))
        self.lineEdit_4.setStyleSheet(u"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;\n"
"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;")
        self.lineEdit_3 = QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 80, 241, 32))
        self.lineEdit_3.setStyleSheet(u"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;\n"
"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;")
        self.lineEdit_7 = QLineEdit(self.tab_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(10, 240, 241, 32))
        self.lineEdit_7.setStyleSheet(u"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;\n"
"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;")
        self.lineEdit_8 = QLineEdit(self.tab_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(10, 280, 241, 32))
        self.lineEdit_8.setStyleSheet(u"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;\n"
"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;")
        self.lineEdit_10 = QLineEdit(self.tab_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(270, 40, 281, 32))
        self.lineEdit_10.setStyleSheet(u"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;\n"
"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;")
        self.lineEdit_2 = QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 40, 241, 32))
        self.lineEdit_2.setStyleSheet(u"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;\n"
"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;")
        self.lineEdit_5 = QLineEdit(self.tab_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(10, 160, 241, 32))
        self.lineEdit_5.setStyleSheet(u"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;\n"
"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;")
        self.lineEdit_6 = QLineEdit(self.tab_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(10, 200, 241, 32))
        self.lineEdit_6.setStyleSheet(u"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;\n"
"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;")
        self.lineEdit_11 = QLineEdit(self.tab_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(10, 400, 241, 32))
        self.lineEdit_11.setStyleSheet(u"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;\n"
"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;")
        self.textEdit_1 = QTextEdit(self.tab_2)
        self.textEdit_1.setObjectName(u"textEdit_1")
        self.textEdit_1.setGeometry(QRect(10, 480, 241, 111))
        self.textEdit_1.setStyleSheet(u"font-size:14px;\n"
"padding: 4px;\n"
"background-color: #404040;\n"
"color: white;\n"
"border-radius: 5px;")
        self.lineEdit_13 = QLineEdit(self.tab_2)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(270, 270, 281, 32))
        self.lineEdit_13.setStyleSheet(u"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;\n"
"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;")
        self.lineEdit_14 = QLineEdit(self.tab_2)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(270, 310, 281, 32))
        self.lineEdit_14.setStyleSheet(u"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;\n"
"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;")
        self.lineEdit_15 = QLineEdit(self.tab_2)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(270, 350, 281, 32))
        self.lineEdit_15.setStyleSheet(u"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;\n"
"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;")
        self.textEdit_2 = QTextEdit(self.tab_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(270, 430, 281, 91))
        self.textEdit_2.setStyleSheet(u"font-size:14px;\n"
"padding: 4px;\n"
"background-color: #404040;\n"
"color: white;\n"
"border-radius: 5px;")
        self.textEdit_3 = QTextEdit(self.tab_2)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(270, 80, 281, 71))
        self.textEdit_3.setStyleSheet(u"font-size:14px;\n"
"padding: 4px;\n"
"background-color: #404040;\n"
"color: white;\n"
"border-radius: 5px;")
        self.lineEdit_16 = QLineEdit(self.tab_2)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(10, 360, 241, 32))
        self.lineEdit_16.setStyleSheet(u"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;\n"
"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;")
        self.lineEdit_17 = QLineEdit(self.tab_2)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(QRect(270, 160, 281, 32))
        self.lineEdit_17.setStyleSheet(u"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;\n"
"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;")
        self.lineEdit_18 = QLineEdit(self.tab_2)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setGeometry(QRect(10, 440, 241, 32))
        self.lineEdit_18.setStyleSheet(u"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;\n"
"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;")
        self.lineEdit_19 = QLineEdit(self.tab_2)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setGeometry(QRect(270, 390, 281, 32))
        self.lineEdit_19.setStyleSheet(u"color: white;\n"
"background-color: #404040;\n"
"border-radius: 5px;\n"
"padding:2px 5px;\n"
"font-size: 14px;\n"
"height: 28px;")
        self.tabWidget.addTab(self.tab_2, "")
        Database_user.setCentralWidget(self.centralwidget)

        self.retranslateUi(Database_user)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Database_user)
    # setupUi

    def retranslateUi(self, Database_user):
        Database_user.setWindowTitle(QCoreApplication.translate("Database_user", u"Database", None))
        self.action.setText(QCoreApplication.translate("Database_user", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043d\u0438\u0446\u0438\u0430\u043b\u044b...", None))
        self.pushButton_2.setText(QCoreApplication.translate("Database_user", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.pushButton_3.setText(QCoreApplication.translate("Database_user", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label_8.setText(QCoreApplication.translate("Database_user", u"\u0422\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.pushButton_10.setText(QCoreApplication.translate("Database_user", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.pushButton_12.setText(QCoreApplication.translate("Database_user", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.pushButton_4.setText(QCoreApplication.translate("Database_user", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.pushButton_5.setText(QCoreApplication.translate("Database_user", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Database_user", u"\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.pushButton.setText(QCoreApplication.translate("Database_user", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Database_user", u"\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u0435\u0442\u0438", None))
        self.label_3.setText(QCoreApplication.translate("Database_user", u"\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("Database_user", u"\u0420\u043e\u0434\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u0438", None))
        self.label_10.setText(QCoreApplication.translate("Database_user", u"\u0412 \u043a\u0430\u043a\u0443\u044e \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c?", None))
        self.label_9.setText(QCoreApplication.translate("Database_user", u"\u041e\u0441\u0442\u0430\u043b\u044c\u043d\u043e\u0435", None))
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u041c\u0430\u0448\u0438\u043d\u0430", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u0418\u043d\u0434\u0435\u043a\u0441", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u0413\u043e\u0440\u043e\u0434/\u0421\u0442\u0440\u0430\u043d\u0430", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u041c\u0435\u0441\u0442\u043e \u0440\u0430\u0431\u043e\u0442\u044b/\u0443\u0447\u0451\u0431\u044b", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u0418\u043c\u044f", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u0414\u043e\u043c\u0430\u0448\u043d\u0438\u0439 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.textEdit_1.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u041e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.lineEdit_14.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u0412\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0435", None))
        self.lineEdit_15.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u0418\u043d\u0441\u0442\u0430\u0433\u0440\u0430\u043c", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u0414\u0440\u0443\u0433\u0438\u0435 \u0441\u043e\u0446 \u0441\u0435\u0442\u0438", None))
        self.textEdit_3.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442", None))
        self.lineEdit_16.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.lineEdit_17.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u0421\u043d\u0438\u043b\u0441", None))
        self.lineEdit_18.setPlaceholderText(QCoreApplication.translate("Database_user", u"\u0423\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.lineEdit_19.setPlaceholderText(QCoreApplication.translate("Database_user", u"Telegram", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Database_user", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

