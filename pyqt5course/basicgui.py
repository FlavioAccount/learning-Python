#Welcome to the PyQT5 Course
#First step. Install the pips:
#pip install pyqt5  ,   pip install pyqt5-tools
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()
        self.setGeometry(700, 400, 100, 100) # X position, Yposition, width, height (0, 0, x, x) will position your window in top left corner
        self.setWindowTitle("Flavio's lesson")#This will set the Window's title
    
    def initUI(self):
        self.label = QtWidgets.QLabel(self) #create a label to add in win
        self.label.setText("My first label")
        self.label.move(50, 50)

        self.button1 = QtWidgets.QPushButton(self) #Instance of this new button
        self.button1.setText("Click on me! ") #Set the message to the button
        self.button1.clicked.connect(self.buttonclicked) #After clicking the button, it shows the message on the terminal
        
        self.slider = QSlider(self)
        self.slider.setMinimum(100)
        self.slider.setMaximum(900)
        self.slider.setSingleStep(3)
        position = self.slider.sliderMoved.connect(self.slider_position)
        self.slider.sliderPressed.connect(self.slider_pressed)
        self.slider.sliderReleased.connect(self.slider_released)
        self.slider.show()
        self.slider.scroll(0, position)
        self.slider.setGeometry(100, 100, 20, 1000)

    def slider_position(self, p):
        print(p)
        return p
    
    def slider_pressed(self):
        print("Slider pressed")
    
    def slider_released(self):
        print("Slider released")

    def buttonclicked(self):
        self.label.setText("clicked!")
        self.update()
    
    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv) #It knows how to set up the display depending of the device's display
    win = MyWindow() #Create the window that will actually be displayed on you window

    win.show() #this method will show the Window
    sys.exit(app.exec_()) #This will wait for closing the application

window()
