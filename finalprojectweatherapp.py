# ********Final Project**********
#          Weather APP
# This opened API will be used to get the APIs
# https://openweathermap.org/api
# API Key 0664d9540db89f5733f1d646913b3d08

import sys
import socket
import requests 
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                            QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt, QTime
from datetime import date

class WeatherApp(QWidget):
    def __init__(self): #Defining the constructor
        super().__init__()
        self.city_label = QLabel("Enter city name: ",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel("🌞", self)
        self.description_label = QLabel(f"Hello {socket.gethostname()}",self)
        
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Weather App")
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 25px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "0664d9540db89f5733f1d646913b3d08"
        city = self.city_input.text()
        current_date = date.today()
        url_geo = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{""},{""}&limit={""}&appid={api_key}" #Go to documentation and take the API: https://openweathermap.org/api/one-call-3?collection=one_call_api_3.0&collection=one_call_api_3.0#history
        try:
            response_url_geo = requests.get(url_geo)
            response_url_geo.raise_for_status()
            data_url_geo = response_url_geo.json()
            if data_url_geo:
                url = f"https://api.openweathermap.org/data/2.5/weather?lat={data_url_geo[0]["lat"]}&lon={data_url_geo[0]["lon"]}&appid={api_key}"
                response_url = requests.get(url)
                data_url = response_url.json()
                self.display_weather(data_url)
            else:
                self.display_error("City not found, try again!")
                self.emoji_label.setText("⛔")
        
        except requests.exceptions.HTTPError as http_error:
            match response_url.status_code:
                case 400:
                    self.display_error("Bad request: \nPlease check your input")
                case 401:
                    self.display_error("Unauthorized: \nInvalid API Key")
                case 403:
                    self.display_error("Forbidden: \naccess is denied")
                case 404:
                    self.display_error("Not found: \nCity not found")
                case 500:
                    self.display_error("Internal Server Error: \nPlease try again later")
                case 502:
                    self.display_error("Bad gateway: \nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable: \nServer is down")
                case 504:
                    self.display_error("Gateway Timeout: \nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occured: \n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error: \nCheck your internet connection")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error: \nThe request timed out")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects: \nCheck the URL")

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error: \n{req_error}")

    def display_error(self, message):
        self.temperature_label.setText(message)
        

    def display_weather(self, data_url):
        self.temperature_label.setStyleSheet(" font-size: 75px; font-weight: bold;")
        temperature_c = int((data_url["main"]["temp"] - 273.15))
        temperature_k = int(data_url["main"]["temp"])
        self.temperature_label.setText(str(f"{temperature_c}°C "))
        self.display_description(data_url)
        self.display_emoji(data_url)
        
    def display_description(self, data_url):
        self.description_label.setText(str(f"{data_url["weather"][0]["main"]}"))
        

    def display_emoji(self, data_url):
        weather_id = data_url["weather"][0]["id"]

        if data_url["weather"][0]["main"] == "Rain":
            self.emoji_label.setText("🌧️")
        elif data_url["weather"][0]["main"] == "Sunny":
            self.emoji_label.setText("☀️")
        elif data_url["weather"][0]["main"] == "Clear":
            self.emoji_label.setText("☀️")
        elif data_url["weather"][0]["main"] == "Snow":
            self.emoji_label.setText("❄️")
        elif data_url["weather"][0]["main"] == "Clouds":
            self.emoji_label.setText("⛅")
        else:
            self.emoji_label.setText("🍋")

        

if __name__== "__main__":
    app = QApplication(sys.argv) #If you have commands arguments to send to this application, you can use this
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
