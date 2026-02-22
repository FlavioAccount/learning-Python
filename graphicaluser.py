# PyQt5 introduction
import sys #This module provides access to some variables used or maintained bu the interpreter and to functions that interpract strongly with the interpreter
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel #Pay attention on capitalization
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
#**Study the libraries above

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI") #This method changes the title
        self.setGeometry(0, 0, 500, 500) 
        self.setWindowIcon(QIcon("robot_image.jpg"))
        #The following methods create a label
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 20))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #DB4437;"
                            "background-color: #F4B400;"
                            "font-weight: bold;"
                            "font-style:italic;"
                            "text-decoration: underline;") #Changes the color of the word
        # label.setAlignment(Qt.AlignTop) #It aligns the text to the top
        # label.setAlignment(Qt.AlignBottom) #It aligns the text to the bottom
        # label.setAlignment(Qt.AlignVCenter) #It aligns the text on the center
        # label.setAlignment(Qt.AlignRight) #Horizontally right
        # label.setAlignment(Qt.AlignHCenter) #Horizontally center
        # label.setAlignment(Qt.AlignLeft) #Horizontally left
        label.setAlignment(Qt.AlignCenter)
        
        # # Is possible to combine both

        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #Center & Top
        label.setAlignment(Qt.AlignCenter)# Center & Bottom


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() #The windows shows for less than 1 second
    sys.exit(app.exec_())



if __name__=="__main__":
    main()