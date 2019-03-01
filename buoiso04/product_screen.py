from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from product_list import ProductList
class ProductScreen:
	def click_ok(self):
		message_box = QMessageBox()
		typedName = self.txtName.text().strip()
		typedYear = self.txtYear.text().strip()
		if len(typedName)==0 or len(typedYear) == 0:
			message_box.setText('Please input information')
			message_box.exec_()
		else:
			dict_product = {"name": typedName, \
				"year": typedYear}
			self.products.append(dict_product)
		
	def __init__(self):
		self.window = QWidget()
		self.window.resize(800, 600)
		self.window.setWindowTitle('This is Product Screen')

		vbox = QVBoxLayout()
		vbox.setSpacing(10)

		self.txtName = QLineEdit()
		self.txtName.setPlaceholderText("Enter product's name")
		self.txtYear = QLineEdit()
		self.txtYear.setPlaceholderText('Year')

		vbox.addWidget(self.txtName)
		vbox.addWidget(self.txtYear)
		#vbox.addStretch(2)
		btn_save = QPushButton("Add product")
		btn_save.clicked.connect(self.click_ok)
		vbox.addWidget(btn_save)

		btn_show_list = QPushButton("Show product List")
		vbox.addWidget(btn_show_list)
		btn_show_list.clicked.connect(self.btn_show_list)

		self.window.setLayout(vbox)
		self.window.show()
		self.products = []
		self.product_list = None
	def btn_show_list(self):
		if self.product_list == None:
			self.product_list = ProductList()