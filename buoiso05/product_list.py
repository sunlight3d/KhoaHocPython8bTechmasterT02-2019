from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ProductList:		
	def __init__(self, product_screen, products = []):
		self.window = QWidget()
		self.window.resize(1000, 700)
		self.window.setWindowTitle('This is Product List')	
		#Reference from ProductScreen
		self.product_screen = product_screen
		self.products = products
		self.setup_ui()
		print(self.products)
		self.window.show()

	def setup_ui(self):
		self.vbox = QVBoxLayout()
		self.vbox.setSpacing(10)
		self.window.setLayout(self.vbox)

		self.label_title = QLabel("This is a list of products")
		self.label_title.setAlignment(Qt.AlignLeft)
		self.vbox.addWidget(self.label_title)
		self.table = QTableWidget()
		
		self.table.horizontalHeader().setFixedHeight(50)
		self.table.setRowCount(len(self.products))
		
		row = 0
		for product in self.products:
			self.table.setColumnCount(len(product))
			self.table.setColumnWidth(row, self.table.width() / 2)
			self.table.setItem(row,0, QTableWidgetItem(product['name']))
			self.table.setItem(row,1, QTableWidgetItem(product['year']))
			self.table.setItem(row,2, QTableWidgetItem(product['status']))
			row = row + 1
		self.table.move(0,0)
		self.table.setHorizontalHeaderLabels(["Tên sản phẩm", "Năm sản xuất", "Trạng thái"])
		self.vbox.addWidget(self.table)