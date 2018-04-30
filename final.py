import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PIL import Image
from PyQt5.QtGui import QPixmap, QPalette
import restoreImage 


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

		self.buttonZooming = QPushButton('Zoom', self) # Making the zooming button
		self.buttonZooming.clicked.connect(self.zoomingButtonClicked)

		# create an exit button
		self.buttonExit = QPushButton('Exit', self)
		self.buttonExit.clicked.connect(self.exitButtonClicked)

		self.picture_label = QLabel(self) # Getting the picture
		self.my_image = QPixmap(pic)
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

	def cropButtonClicked(self): # This function will run when the crop button is click
		print("Crop Button Clicked")

	def filteringButtonClicked(self): # This function will run when the filter button is click
		print("Filtering Button Clicked")

	def zoomingButtonClicked(self):
		print("Zooming Button Clicked")

	def exitButtonClicked(self):
		print("Exit Button Clicked")

im = QApplication(sys.argv)
image_window = ImageExample()
sys.exit(im.exec_())