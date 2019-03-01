from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class LoginScreen:
	def click_ok(self):
		message_box = QMessageBox()
		typedName = self.txtName.text().strip()
		typedEmail = self.txtEmail.text().strip()
		if len(typedName)==0 or len(typedEmail) == 0:
			message_box.setText('Please input information')
		else:
			message_box.setText('Ban da nhap name:'+\
				typedName+",email:"+typedEmail)
		message_box.exec_()

	def __init__(self):
		self.window = QWidget()
		self.window.resize(800, 600)
		self.window.setWindowTitle('This is Login Screen')

		vbox = QVBoxLayout()
		vbox.setSpacing(10)

		self.txtName = QLineEdit()
		self.txtName.setPlaceholderText('Enter your name')
		self.txtEmail = QLineEdit()
		self.txtEmail.setPlaceholderText('Enter your email')
		self.txtPassword = QLineEdit()
		self.txtPassword.setPlaceholderText('Enter your password')
		self.txtPassword.setEchoMode(QLineEdit.Password)

		vbox.addWidget(self.txtName)
		vbox.addWidget(self.txtEmail)
		vbox.addWidget(self.txtPassword)
		#vbox.addStretch(2)

		hbox = QHBoxLayout()
		btn_ok = QPushButton("OK")
		btn_ok.clicked.connect(self.click_ok)

		hbox.addWidget(btn_ok)
		btn_cancel = QPushButton("Cancel")
		

		hbox.addWidget(btn_cancel)
		vbox.addStretch(1)
		vbox.addLayout(hbox)
		vbox.addStretch(2)
		self.window.setLayout(vbox)
		self.window.show()