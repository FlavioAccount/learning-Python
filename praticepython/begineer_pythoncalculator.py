# Python Calculator
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
class Calculator(QWidget):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age
        self.user_name = QLabel("Enter your name", self)
        self.user_input = QLineEdit(self)
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
        self.initUI()

    def initUI(self):
        self.num= ""
        self.number1 = 0
        self.number2 = ""
        self.setWindowTitle("Calculator APP")
        self.setGeometry(700, 400, 500, 500)
        vbox = QVBoxLayout()
        vbox.addWidget(self.user_name)
        vbox.addWidget(self.user_input)
        self.setLayout(vbox)
        self.user_name.setAlignment(Qt.AlignCenter)
        self.user_input.setAlignment(Qt.AlignCenter)
        self.user_name.setObjectName("user_name")
        self.user_input.setObjectName("user_input")

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
        self.button_numequal.setGeometry(250,100, 50, 50)
        self.button_numequal.clicked.connect(self.buttonequalclicked)

        self.button_numerase.setObjectName("button_erase")
        self.button_numerase.setGeometry(200,50, 50, 50)
        self.button_numerase.clicked.connect(self.buttoneraseclicked)
    
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#user_name{
                font-size: 20px;
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
    def useroperator(self):
        self.operator = input("Enter the operator: + , - , * , /  -> ")
        return self.operator
    
    def button1clicked(self):
        self.num += "1"
        print(self.num)
    
    def button2clicked(self):
        self.num += "2"
        print(self.num)
    
    def button3clicked(self):
        self.num += "3"
        print(self.num)
    
    def button4clicked(self):
        self.num += "4"
        print(self.num)
    
    def button5clicked(self):
        self.num += "5"
        print(self.num)
    
    def button6clicked(self):
        self.num += "6"
        print(self.num)

    def button7clicked(self):
        self.num += "7"
        print(self.num)

    def button8clicked(self):
        self.num += "8"
        print(self.num)

    def button9clicked(self):
        self.num += "9"
        print(self.num)

    def button0clicked(self):
        self.num += "0"
        print(self.num)

    def buttonmulclicked(self):
        self.operator = "*"
        self.number1 = int(self.num)
        self.num=""
        print(self.operator)
    
    def buttonequalclicked(self): 
        self.equal = "="
        self.number2 = int(self.num)
        print(f"{self.number1} {self.operator} {self.number2}")

    
    def buttonsubclicked(self):
        self.operator = "-"
        print(self.num)

    def buttondivclicked(self):
        self.operator = "/"
        print(self.operator)
    
    def buttonaddclicked(self):
        self.operator = "+"
        print(self.operator)

    def buttoneraseclicked(self):
        self.operator = "<-"
        self.num = ""
        self.operator = ""
        print(self.operator)
    
        
    
    def operation(self, operator):
        if operator == "+":
            num = self.enternum()
            result = self.sum(num[0], num[1])
        elif operator == "-":
            num = self.enternum()
            result = self.subt(num[0], num[1])
        elif operator == "*":
            num = self.enternum()
            result = self.mult(num[0], num[1])
        elif operator == "/":
            num = self.enternum()
            result = self.div(num[0], num[1])
        else:
            print("Invalid operator, try again!")
            return 0
        return result

    def enternum(self):
        self.button_num1.clicked.connect(self.enternum())
        self.num1 = int(input("Enter the first number: "))
        self.num2 = int(input("Enter the second number: "))
        return self.num1, self.num2
    
    def sum(self, num1, num2):
        return num1 + num2
    
    def div(self, num1, num2):
        return num1/num2
    
    def mult(self, num1, num2):
        return num1 * num2
    
    def subt(self, num1, num2):
        return num1 - num2
    
    def printresult(self, result):
        print(f"{self.num1} {self.operator} {self.num2} = {result}")

# def main():
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     print(f"***** Hello {name}, Welcome to Python Calculator exercise *****")
#     calculator = Calculator(name, age)
#     operator = calculator.useroperator()
#     result = calculator.operation(operator)
#     calculator.printresult(result)

if __name__=="__main__":
    app = QApplication(sys.argv) #It knows how to set up the display depending of the device's display
    win = Calculator("Flavio", "28") #Create the window that will actually be displayed on you window
    win.show() #this method will show the Window
    sys.exit(app.exec_()) #This will wait for closing the application