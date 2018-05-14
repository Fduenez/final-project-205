import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox, QFileDialog, QLineEdit
from PIL import Image
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QPalette
import restoreImage as rf
import colorFilter as cf
import numberGenerator as ng
import mUp as mu
#import searchFile as sf

my_list = ["Filter", "increase red", "increase blue", "increase green"]
my_colors = ["Red", "Green", "Blue", "Black", "White"]
my_locations = ["top right", "top left", "bottom right", "bottom_left", "middle", "custom"]
my_up = ["2-Up", "4-Up", "8-Up"]

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

		self.numberingButton = QPushButton("Number")
		self.numberingButton.clicked.connect(self.numberingButtonClicked)

		self.multipleUpButton = QPushButton("Multiple-Up")
		self.multipleUpButton.clicked.connect(self.multipleUpButtonClicked)

		hbox = QHBoxLayout() # Making the layout for the buttons
		hbox.addWidget(self.buttonCropping) # Crop Button
		hbox.addWidget(self.buttonRestoring) # If pic is modified then it restores the og img
		hbox.addWidget(self.buttonZooming) # zoom button
		hbox.addWidget(self.my_combo_box) # Filter Button
		hbox.addWidget(self.numberingButton) # numbering button
		hbox.addWidget(self.multipleUpButton) # multiple up button
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

	def numberingButtonClicked(self):
		self.numbering_window = NumberingWindow()
		self.numbering_window.show()

	def multipleUpButtonClicked(self):
		self.up_window = MultipleUpWindow()
		self.up_window.show()

#######################################################################################
	def exitButtonClicked(self): # This function will run when the filter button is click
		print("Exit Button Clicked")

class NumberingWindow(QWidget):       # Class for opening a secondary window for numbering documents
	def __init__(self):
		super().__init__()

		# size window
		self.setWindowTitle("Numbering Window")
		self.setGeometry(0, 0, 300, 300)

		# Create instructions for each field and ComboBox
		self.startField = QLabel("Enter the starting number:")
		self.endField = QLabel("Enter the ending number:")
		self.setField = QLabel("Enter # of pages in a set:")
		self.locField = QLabel("Document number location:")
		self.cLocField = QLabel("Custom location (x) (y):")
		self.sizeField = QLabel("Enter font size in (pt):")
		self.colorField = QLabel("Select color for numbers:")

		# Create widgets to use for numbering inputs
		self.startingNumberField = QLineEdit()
		self.endingNumberField = QLineEdit()
		self.pagesInSetField = QLineEdit()
		self.locationComboBox = QComboBox()
		self.cLocationField1 = QLineEdit()
		self.cLocationField2 = QLineEdit()
		self.fontSizeField = QLineEdit()
		self.colorComboBox = QComboBox()
		self.proofInput = QPushButton("Proof")
		self.proofInput.clicked.connect(self.onProofClick)
		self.submitInput = QPushButton("Submit")
		self.submitInput.clicked.connect(self.onSubmitClick)

		# Populate ComboBox widgets
		self.locationComboBox.addItems(my_locations)
		self.colorComboBox.addItems(my_colors)

		# Pair instructions with input fields and boxes using the horizontal layout
		hbox1 = QHBoxLayout()
		hbox2 = QHBoxLayout()
		hbox3 = QHBoxLayout()
		hbox4 = QHBoxLayout()
		hbox5 = QHBoxLayout()
		hbox6 = QHBoxLayout()
		hbox7 = QHBoxLayout()
		hbox1.addWidget(self.startField)
		hbox1.addWidget(self.startingNumberField)
		hbox2.addWidget(self.endField)
		hbox2.addWidget(self.endingNumberField)
		hbox3.addWidget(self.setField)
		hbox3.addWidget(self.pagesInSetField)
		hbox4.addWidget(self.locField)
		hbox4.addWidget(self.locationComboBox)
		hbox5.addWidget(self.cLocField)
		hbox5.addWidget(self.cLocationField1)
		hbox5.addWidget(self.cLocationField2)
		hbox6.addWidget(self.sizeField)
		hbox6.addWidget(self.fontSizeField)
		hbox7.addWidget(self.colorField)
		hbox7.addWidget(self.colorComboBox)

		# add each instruction group to vertical layout
		numberingLayout = QVBoxLayout()
		numberingLayout.addLayout(hbox1)
		numberingLayout.addLayout(hbox2)
		numberingLayout.addLayout(hbox3)
		numberingLayout.addLayout(hbox4)
		numberingLayout.addLayout(hbox5)
		numberingLayout.addLayout(hbox6)
		numberingLayout.addLayout(hbox7)
		numberingLayout.addWidget(self.proofInput)
		numberingLayout.addWidget(self.submitInput)

		# final layout
		self.setLayout(numberingLayout)

		self.show()

	def onProofClick(self):
		filename = "falcon_heavy.jpg"
		startNum = int(self.startingNumberField.text())
		endNum = int(self.endingNumberField.text())
		setPageNum = int(self.pagesInSetField.text())
		location = my_locations[self.locationComboBox.currentIndex()]
		cLocation = (int(self.cLocationField1.text()), int(self.cLocationField2.text()))
		fontSize = int(self.fontSizeField.text())
		fontColor = my_colors[self.colorComboBox.currentIndex()]

		ng.proofResult(filename, startNum, endNum, setPageNum, location, cLocation, fontSize, fontColor)

	def onSubmitClick(self):
		filename = "falcon_heavy.jpg"
		startNum = int(self.startingNumberField.text())
		endNum = int(self.endingNumberField.text())
		setPageNum = int(self.pagesInSetField.text())
		location = my_locations[self.locationComboBox.currentIndex()]
		cLocation = (int(self.cLocationField1.text()), int(self.cLocationField2.text()))
		fontSize = int(self.fontSizeField.text())
		fontColor = my_colors[self.colorComboBox.currentIndex()]

		ng.generateNumbers(filename, startNum, endNum, setPageNum, location, cLocation, fontSize, fontColor)

class MultipleUpWindow(QWidget):       # Class for opening a secondary window to duplicate a document
	def __init__(self):
		super().__init__()

		# size window and set title
		self.setWindowTitle("Numbering Window")
		self.setGeometry(0, 0, 200, 200)

		self.instruction = QLabel("Select n-Up:")

		self.nUpComboBox = QComboBox()
		self.nUpComboBox.addItems(my_up)

		self.proofButton = QPushButton("Proof")
		self.proofButton.clicked.connect(self.onProofClick)
		self.submitButton = QPushButton("Submit")
		self.submitButton.clicked.connect(self.onSubmitClick)

		hbox1 = QHBoxLayout()
		hbox1.addWidget(self.instruction)
		hbox1.addWidget(self.nUpComboBox)

		upLayout= QVBoxLayout()
		upLayout.addLayout(hbox1)
		upLayout.addWidget(self.proofButton)
		upLayout.addWidget(self.submitButton)

		self.setLayout(upLayout)

		self.show()

	def onProofClick(self):
		choice = my_up[self.nUpComboBox.currentIndex()]
		print(choice)
		if (choice == "2-Up"):
			up = 2
		elif (choice == "4-Up"):
			up = 4
		elif (choice == "8-Up"):
			up = 8

		mu.proofUp("diplo.jpeg", up)

	def onSubmitClick(self):
		choice = my_up[self.nUpComboBox.currentIndex()]
		if (choice == "2-Up"):
			up = 2
		elif (choice == "4-Up"):
			up = 4
		elif (choice == "8-Up"):
			up = 8

		mu.multipleUp("diplo.jpeg", up)

im = QApplication(sys.argv)
image_window = ImageExample()
sys.exit(im.exec_())
