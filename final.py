import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox
from PIL import Image
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QPalette
import restoreImage as rf
import colorFilter as cf
#scroll, zoom

my_list = ["Filter", "increase red", "increase blue", "increase green"]

class ImageExample(QWidget):
	def __init__(self):
		super().__init__()

		self.pic = 'winkled.jpg'

		self.setWindowTitle('Photo Shop')

		self.setBackgroundRole(QPalette.Base)
		self.buttonCropping = QPushButton('Crop', self) # Making the crop button
		self.buttonCropping.clicked.connect(self.cropButtonClicked)

		self.buttonRestoring = QPushButton('Restore Image', self ) # Making the filtering button
		self.buttonRestoring.clicked.connect(self.restoreButtonClicked)

		self.buttonZooming = QPushButton('Zoom', self) # Making the filtering button
		self.buttonZooming.clicked.connect(self.zoomingButtonClicked)

		#self.restartButton = QPushButton('Original', self) #Getting original file
		self.my_combo_box = QComboBox()
		self.my_combo_box.addItems(my_list)

		self.my_combo_box.currentIndexChanged.connect(self.applyFilterClicked)

		self.buttonExit = QPushButton('Exit', self)
		self.buttonExit.clicked.connect(self.exitButtonClicked)

		self.picture_label = QLabel(self) # Getting the picture
		self.my_image = QPixmap(self.pic)
		self.picture_label.setPixmap(self.my_image)

		hbox = QHBoxLayout() # Making the layout for the buttons
		hbox.addWidget(self.buttonCropping)
		hbox.addWidget(self.buttonRestoring)
		hbox.addWidget(self.buttonZooming)
		hbox.addWidget(self.my_combo_box)
		hbox.addWidget(self.buttonExit)

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
			cf.red_Multiply(self.pic, 100)
		elif value == 2:
			return "increase blue"
		else:
			return "increase green"

		redImage = cf.red_Multiply(self.pic, 100)
		redImage.save('temp.jpg')
		self.my_image = QPixmap('temp.jpg')
		self.picture_label.setPixmap(self.my_image)
		#create a new pixmap
		#put that pixmap in the label


	def exitButtonClicked(self): # This function will run when the filter button is click
		print("Exit Button Clicked")

im = QApplication(sys.argv)
image_window = ImageExample()
sys.exit(im.exec_())
