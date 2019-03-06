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
			self.dict_product["name"] = typedName
			self.dict_product["year"] = typedYear
			self.products.append(self.dict_product)
			self.txtName.setText('')
			self.txtYear.setText('')
	"""	
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
	"""
	def __init__(self):		
		self.window = QWidget()
		self.window.resize(800, 600)
		self.window.setWindowTitle('This is Product Screen')
		self.dict_product = {}

		self.gridLayout = QGridLayout()
		self.gridLayout.setSpacing(10)

		self.gridLayout.addWidget(QLabel("Name"), 0, 0)
		self.txtName = QLineEdit()
		self.txtName.setPlaceholderText("Enter product's name")
		self.gridLayout.addWidget(self.txtName, 0, 1)

		self.gridLayout.addWidget(QLabel("Year"), 1, 0)
		self.txtYear = QLineEdit()
		self.txtYear.setPlaceholderText('Year')
		self.gridLayout.addWidget(self.txtYear, 1, 1)

		self.gridLayout.addWidget(QLabel("Status"), 2, 0)
		self.comboStatus = QComboBox()
		self.status = ["Old", "New"]
		self.comboStatus.addItems(self.status)
		self.comboStatus.currentIndexChanged.connect(self.select_status)
		self.gridLayout.addWidget(self.comboStatus, 2, 1)

		#vbox.addStretch(2)
		btn_save = QPushButton("Add product")
		btn_save.clicked.connect(self.click_ok)
		self.gridLayout.addWidget(btn_save, 3, 0)

		btn_show_list = QPushButton("Show product List")
		self.gridLayout.addWidget(btn_show_list, 3, 1)
		btn_show_list.clicked.connect(self.btn_show_list)

		self.window.setLayout(self.gridLayout)
		self.window.show()
		self.products = []
		self.product_list = None
	def select_status(self, index):
		self.dict_product['status'] = self.status[index]
	def btn_show_list(self):
		if self.product_list == None:
			self.product_list = ProductList(self, self.products)