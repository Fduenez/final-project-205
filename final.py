import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PIL import Image
from PyQt5.QtGui import QPixmap, QPalette
#import restoreImage 
import restoreFile as rf

pic = 'diplo.jpeg'
#scroll, zoom
class ImageExample(QWidget):
	def __init__(self):
		super().__init__()

		self.setWindowTitle('Photo Shop')

		self.setBackgroundRole(QPalette.Base)
		self.buttonCropping = QPushButton('Crop', self) # Making the crop button
		self.buttonCropping.clicked.connect(self.cropButtonClicked)

		self.buttonFiltering = QPushButton('Filter', self) # Making the filtering button
		self.buttonFiltering.clicked.connect(self.filteringButtonClicked)

		self.buttonZooming = QPushButton('Zoom', self) # Making the filtering button
		self.buttonZooming.clicked.connect(self.zoomingButtonClicked)

		self.buttonExit = QPushButton('Exit', self)# create an exit button
		self.buttonExit.clicked.connect(self.exitButtonClicked)

		self.picture_label = QLabel(self) # Getting the picture
		self.my_image = QPixmap('winkled.jpg')
		self.picture_label.setPixmap(self.my_image)

		hbox = QHBoxLayout() # Making the layout for the buttons
		hbox.addWidget(self.buttonCropping)
		hbox.addWidget(self.buttonFiltering)
		hbox.addWidget(self.buttonZooming)
		hbox.addWidget(self.buttonExit)

		vbox = QVBoxLayout()
		vbox.addLayout(hbox)
		vbox.addWidget(self.picture_label)

		self.setLayout(vbox)

		self.show()
	def zoomingButtonClicked(self): # This function will run when the zooom button is clicked
		print("Zoom button clicked")

	def cropButtonClicked(self): # This function will run when the crop button is click
		print("Crop Button Clicked")

	def filteringButtonClicked(self): # This function will run when the filter button is click
		print("Filtering Button Clicked")
		rf.restore('winkled.jpg')

	def exitButtonClicked(self): # This function will run when the filter button is click
		print("Exit Button Clicked")

im = QApplication(sys.argv)
image_window = ImageExample()
sys.exit(im.exec_())