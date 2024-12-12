from sense_hat import SenseHat
import time
import requests

#This is our temp sensor
sense = SenseHat()

url = "https://seasonalstoryrest.azurewebsites.net/api/temperatures"
 # Wrapping the integer in a dictionary



def update_temp():
    measured_temp = sense.temp
    roundedtemp = round(measured_temp)
    return roundedtemp

def show_temp(temp):
   tempstring = str(temp)
   print("Temp:"+ (tempstring))
   sense.show_message(tempstring)

def send_to_api(temperature):
    data = {"value": temperature} 
    response = requests.post(url, json=data)  # Use json= for JSON encoding
    print(response.status_code, response.text)

while True:
    value = update_temp()
    show_temp(value)
    send_to_api(value)
    time.sleep(60)
