# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(371, 152)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(54, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.mac_lineEdit = QtWidgets.QLineEdit(Form)
        self.mac_lineEdit.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.mac_lineEdit.setObjectName("mac_lineEdit")
        self.horizontalLayout.addWidget(self.mac_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMinimumSize(QtCore.QSize(54, 0))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.encrypt_lineEdit = QtWidgets.QLineEdit(Form)
        self.encrypt_lineEdit.setObjectName("encrypt_lineEdit")
        self.horizontalLayout_2.addWidget(self.encrypt_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.hint_label = QtWidgets.QLabel(Form)
        self.hint_label.setStyleSheet("color: rgb(0, 85, 255);")
        self.hint_label.setText("")
        self.hint_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hint_label.setObjectName("hint_label")
        self.verticalLayout.addWidget(self.hint_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.copy_pushButton = QtWidgets.QPushButton(Form)
        self.copy_pushButton.setObjectName("copy_pushButton")
        self.horizontalLayout_3.addWidget(self.copy_pushButton)
        self.generate_pushButton = QtWidgets.QPushButton(Form)
        self.generate_pushButton.setObjectName("generate_pushButton")
        self.horizontalLayout_3.addWidget(self.generate_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "测评软件授权码生成器"))
        self.label_2.setText(_translate("Form", "加密内容:"))
        self.label_3.setText(_translate("Form", "密      文:"))
        self.copy_pushButton.setText(_translate("Form", "拷贝密文"))
        self.generate_pushButton.setText(_translate("Form", "生成密文"))

