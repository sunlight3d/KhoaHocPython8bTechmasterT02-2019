from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ProductList:		
	def __init__(self):
		self.window = QWidget()
		self.window.resize(1000, 700)
		self.window.setWindowTitle('This is Product List')	
		self.window.show()