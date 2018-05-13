import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox, QFileDialog
from PIL import Image
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QPalette
import restoreImage as rf
import colorFilter as cf
#import searchFile as sf

my_list = ["Filter", "increase red", "increase blue", "increase green"]

class ImageExample(QWidget):
	def __init__(self):
		super().__init__()

		self.pic = 'winkled.jpg'

		self.setWindowTitle('Photo Shop')

		self.setBackgroundRole(QPalette.Base)
		self.buttonCropping = QPushButton('Crop', self) # Making the crop button
		self.buttonCropping.clicked.connect(self.cropButtonClicked)

		self.buttonRestoring = QPushButton('Restore Image', self ) # Restoring original image
		self.buttonRestoring.clicked.connect(self.restoreButtonClicked)

		self.buttonZooming = QPushButton('Zoom', self) # Making the zooming button
		self.buttonZooming.clicked.connect(self.zoomingButtonClicked)

		self.my_combo_box = QComboBox() # Filter
		self.my_combo_box.addItems(my_list) # Adding items to filter

		self.my_combo_box.currentIndexChanged.connect(self.applyFilterClicked) # Filter

		self.buttonExit = QPushButton('Exit', self)
		self.buttonExit.clicked.connect(self.exitButtonClicked)

		self.picture_label = QLabel(self) # Getting the picture
		self.my_image = QPixmap(self.pic)
		self.picture_label.setPixmap(self.my_image)

		self.buttonSearching = QPushButton('Search', self) # Making the filtering button
		self.buttonSearching.clicked.connect(self.searchingButtonClicked)

		hbox = QHBoxLayout() # Making the layout for the buttons
		hbox.addWidget(self.buttonCropping) # Crop Button
		hbox.addWidget(self.buttonRestoring) # If pic is modified then it restores the og img
		hbox.addWidget(self.buttonZooming) # zoom button
		hbox.addWidget(self.my_combo_box) # Filter Button
		hbox.addWidget(self.buttonSearching) # Seach Button
		hbox.addWidget(self.buttonExit) # Exit Button

		vbox = QVBoxLayout()
		vbox.addLayout(hbox)
		vbox.addWidget(self.picture_label)

		self.setLayout(vbox)

		self.show()


	def zoomingButtonClicked(self):
		print("Zoom button clicked")

	def cropButtonClicked(self): # This function will run when the crop button is click
		print("Crop Button Clicked")

	def restoreButtonClicked(self): # This function will run when the filter button is click
		print("Restore Button Clicked")
		rf.restore(self.pic)
		self.my_image = QPixmap('good.jpg')
		self.picture_label.setPixmap(self.my_image)
		im = Image.open(self.pic)
		im.show()

	def filterButtonClicked(self):
		print("Filter Button Clicked")
		rf.restore(self.pic)
		self.my_image = QPixmap('good.jpg')
		self.picture_label.setPixmap(self.my_image)

	def applyFilterClicked(self, value):
		print("Apply Filtered Clicked")
		print(value)

		if value == 1:
			pic = cf.red_Multiply(self.pic, 0)
		elif value == 2:
			pic = cf.green_Multiply(self.pic, 0)
		else:
			pic = cf.blue_Multiply(self.pic, 0)

		pic.save('temp.jpg')
		self.my_image = QPixmap('temp.jpg')
		self.picture_label.setPixmap(self.my_image)
##################################################################################3
	def searchingButtonClicked(self):
		print("Search Button Clicked")
		search = QFileDialog.Options()
		search = QFileDialog.DontUseNativeDialog
		fileName,_= QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=search)
		print(fileName)
		self.picture_label = QLabel(self)
		self.my_image = QPixmap(fileName)
		self.picture_label.setPixmap(self.my_image)
#######################################################################################
	def exitButtonClicked(self): # This function will run when the filter button is click
		print("Exit Button Clicked")

im = QApplication(sys.argv)
image_window = ImageExample()
sys.exit(im.exec_())