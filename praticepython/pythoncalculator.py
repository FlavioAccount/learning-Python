# Python Calculator
import sys
import requests
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
import threading
import time
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.num_label = QLabel(self)
        self.operator_label = QLabel(self)
        self.button_num0 = QPushButton("0", self)
        self.button_num1 = QPushButton("1", self)
        self.button_num2 = QPushButton("2", self)
        self.button_num3 = QPushButton("3", self)
        self.button_num4 = QPushButton("4", self)
        self.button_num5 = QPushButton("5", self)
        self.button_num6 = QPushButton("6", self)
        self.button_num7 = QPushButton("7", self)
        self.button_num8 = QPushButton("8", self)
        self.button_num9 = QPushButton("9", self)
        self.button_numadd = QPushButton("+", self)
        self.button_numsub = QPushButton("-", self)
        self.button_nummul = QPushButton("*", self)
        self.button_numdiv = QPushButton("/", self)
        self.button_numequal = QPushButton("=", self)
        self.button_numerase = QPushButton("<-", self)
        self.button_par1 = QPushButton("(", self)
        self.button_par2 = QPushButton(")", self)
        self.button_dot = QPushButton(".", self)
        self.button_del = QPushButton("del", self)

        self.initUI()

    def initUI(self):
        self.test_attribute_bool = True # attribute created for test 
        self.buttondelclicked()
        self.aux_num = ""
        self.setWindowTitle("Calculator APP")
        self.setGeometry(1080, 600, 400, 600)

        vbox = QVBoxLayout()
        vbox.addWidget(self.num_label)
        vbox.addWidget(self.operator_label)

        self.setLayout(vbox)
        self.num_label.setObjectName("num_label")
        self.num_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.operator_label.setObjectName("operator_label")

        self.button_num0.setObjectName("button_num0")
        self.button_num0.setGeometry(150,250, 50, 50)
        self.button_num0.clicked.connect(self.button0clicked)

        self.button_num1.setObjectName("button_num1")
        self.button_num1.setGeometry(100,100, 50, 50)
        self.button_num1.clicked.connect(self.button1clicked)

        self.button_num2.setObjectName("button_num2")
        self.button_num2.setGeometry(150,100, 50, 50)
        self.button_num2.clicked.connect(self.button2clicked)

        self.button_num3.setObjectName("button_num3")
        self.button_num3.setGeometry(200,100, 50, 50)
        self.button_num3.clicked.connect(self.button3clicked)

        self.button_num4.setObjectName("button_num4")
        self.button_num4.setGeometry(100,150, 50, 50)
        self.button_num4.clicked.connect(self.button4clicked)

        self.button_num5.setObjectName("button_num5")
        self.button_num5.setGeometry(150,150, 50, 50)
        self.button_num5.clicked.connect(self.button5clicked)

        self.button_num6.setObjectName("button_num6")
        self.button_num6.setGeometry(200,150, 50, 50)
        self.button_num6.clicked.connect(self.button6clicked)

        self.button_num7.setObjectName("button_num7")
        self.button_num7.setGeometry(100,200, 50, 50)
        self.button_num7.clicked.connect(self.button7clicked)

        self.button_num8.setObjectName("button_num8")
        self.button_num8.setGeometry(150,200, 50, 50)
        self.button_num8.clicked.connect(self.button8clicked)

        self.button_num9.setObjectName("button_num9")
        self.button_num9.setGeometry(200,200, 50, 50)
        self.button_num9.clicked.connect(self.button9clicked)

        self.button_numadd.setObjectName("button_numadd")
        self.button_numadd.setGeometry(250,150, 50, 50)
        self.button_numadd.clicked.connect(self.buttonaddclicked)

        self.button_numsub.setObjectName("button_numsub")
        self.button_numsub.setGeometry(250,50, 50, 50)
        self.button_numsub.clicked.connect(self.buttonsubclicked)

        self.button_nummul.setObjectName("button_nummul")
        self.button_nummul.setGeometry(250,200, 50, 50)
        self.button_nummul.clicked.connect(self.buttonmulclicked)

        self.button_numdiv.setObjectName("button_numdiv")
        self.button_numdiv.setGeometry(250,100, 50, 50)
        self.button_numdiv.clicked.connect(self.buttondivclicked)

        self.button_numequal.setObjectName("button_numequal")
        self.button_numequal.setGeometry(250,250, 50, 50)
        self.button_numequal.clicked.connect(self.buttonequalclicked)

        self.button_numerase.setObjectName("button_erase")
        self.button_numerase.setGeometry(200,50, 50, 50)
        self.button_numerase.clicked.connect(self.buttoneraseclicked)

        self.button_par1.setObjectName("button_par1")
        self.button_par1.setGeometry(100,50, 50, 50)
        self.button_par1.clicked.connect(self.buttonpar1clicked)

        self.button_par2.setObjectName("button_par2")
        self.button_par2.setGeometry(150,50, 50, 50)
        self.button_par2.clicked.connect(self.buttonpar2clicked)

        self.button_dot.setObjectName("button_dot")
        self.button_dot.setGeometry(200,250, 50, 50)
        self.button_dot.clicked.connect(self.buttondotclicked)

        self.button_del.setObjectName("button_del")
        self.button_del.setGeometry(300,50, 50, 50)
        self.button_del.clicked.connect(self.buttondelclicked)

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#user_name{
                font-size: 20px;
                font-style: italic;
            }
            QLabel#num_label{
                font-size: 20px;
                font-style: italic;
            }
            QLabel#operator_label{
                font-size: 30px;
                font-style: italic;
            }
            QLineEdit#user_input{
                font-size: 20px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
        """)
    
    def button1clicked(self):
        if not self.equal_bool:
            self.num += "1"
            self.shownumber()
        else:
            pass
    
    def button2clicked(self):
        if not self.equal_bool:
            self.num += "2"
            self.shownumber()
        else:
            pass

    def buttoneraseclicked(self):
        if not self.equal_bool:
            self.num = self.num[:-1]
            self.shownumber()
        else:
            pass

    def button3clicked(self):
        if not self.equal_bool:
            self.num += "3"
            self.shownumber()
        else:
            pass
    
    def button4clicked(self):
        if not self.equal_bool:
            self.num += "4"
            self.shownumber()
        else:
            pass
    
    def button5clicked(self):
        if not self.equal_bool:
            self.num += "5"
            self.shownumber()
        else:
            pass
    
    def button6clicked(self):
        if not self.equal_bool:
            self.num += "6"
            self.shownumber()
        else:
            pass

    def button7clicked(self):
        if not self.equal_bool:
            self.num += "7"
            self.shownumber()
        else:
            pass

    def button8clicked(self):
        if not self.equal_bool:
            self.num += "8"
            self.shownumber()
        else:
            pass

    def button9clicked(self):
        if not self.equal_bool:
            self.num += "9"
            self.shownumber()
        else:
            pass

    def button0clicked(self):
        if not self.equal_bool:
            self.num += "0"
            self.shownumber()
        else:
            pass
    
    def buttonpar1clicked(self):
        if not self.equal_bool:
            self.num += "("
            self.shownumber()
        else:
            pass

    def buttonpar2clicked(self):
        if not self.equal_bool:
            self.num += ")"
            self.shownumber()
        else:
            pass

    def buttondotclicked(self):
        if not self.equal_bool:
            self.num += "."
            self.shownumber()
        else:
            pass

    def buttonequalclicked(self):
        try:
            if self.equal_bool == False and self.num != "":
                self.equal = " = "
                self.result = eval(self.num) 
                self.equal_bool = True 
                self.shownumber()
            else:
                pass
        except ZeroDivisionError:
            self.num_label.setText("Division by zero!")
        except:
            self.num_label.setText("Wrong operation! Try again")
            

    def buttonmulclicked(self):
        self.aux_num = ""
        if self.num != "" and self.equal_bool == False:
            self.num += " * " 
            self.shownumber()
        elif self.equal_bool == True:
            self.aux_num = self.result
            self.buttondelclicked()
            self.num += str(self.aux_num) + " * "
            self.shownumber()
        else:
            pass
    

    def buttonsubclicked(self):
        self.aux_num = ""
        if self.num != "" and self.equal_bool == False:
            self.num += " - " 
            self.shownumber()
        elif self.equal_bool == True:
            self.aux_num = self.result
            self.buttondelclicked()
            self.num += str(self.aux_num) + " - "
            self.shownumber()
        else:
            pass
        
    def buttondivclicked(self):
        self.aux_num = ""
        if self.num != "" and self.equal_bool == False:
            self.num += " / " 
            self.shownumber()
        elif self.equal_bool == True:
            self.aux_num = self.result
            self.buttondelclicked()
            self.num += str(self.aux_num) + " / "
            self.shownumber()
        else:
            pass
        
    def buttonaddclicked(self):
        if self.num != "" and self.equal_bool == False:
            self.num += " + "
            self.shownumber()
        elif self.equal_bool == True:
            self.aux_num = self.result
            self.buttondelclicked()
            self.num += str(self.aux_num) + " + "
            self.shownumber()
        else:
            pass

    def buttondelclicked(self):
        self.operator = ""
        self.num = ""
        self.operator = ""
        self.result = ""
        self.equal = ""
        self.equal_bool = False
        self.shownumber()
    
    def multtasking(self):
        self.check_atribute = threading.Thread(target= self.test_attribute)
        self.check_atribute.start()

    def test_attribute(self):
        num = self.num
        result = self.result
        equal = self.equal
        equal_bool = self.equal_bool
        aux_num = self.aux_num
        while self.test_attribute_bool:
            time.sleep(1)
            if (num != self.num or
                result != self.result or
                equal != self.equal or
                equal_bool != self.equal_bool):
                print("\n***************************************************")
                print(f"self.num: {self.num}")
                print(f"self.result: {self.result}")
                print(f"self.equal: {self.equal}")
                print(f"self.equal_bool: {self.equal_bool}")
                print(f"self.aux_num: {self.aux_num}")
                print("***************************************************\n")        
                num = self.num
                result = self.result
                equal = self.equal
                equal_bool = self.equal_bool
                aux_num = self.aux_num
            else:
                pass

    def shownumber(self):
        self.num_label.setText(f"{self.num}{self.equal}{self.result}")

if __name__=="__main__":
    app = QApplication(sys.argv) #It knows how to set up the dis play depending of the device's display
    win = Calculator() #Create the window that will actually be displayed on you window
    win.show() #this method will show the Window
    win.multtasking()
    sys.exit(app.exec_()) #This will wait for closing the application