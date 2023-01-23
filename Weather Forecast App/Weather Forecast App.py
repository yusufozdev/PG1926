import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 32479))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 32359))
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Maksimum Sıcaklık: " + str(max_temp)+ "°C" + \
                 "\n" + "Minimum Sıcaklık: " + str(min_temp)+ "°C" + \
                 "\n" + "Basınç: " + str(pressure)+ " hPa" + \
                 "\n" + "Nem: " +"%" + str(humidity) + \
                 "\n" + "Rüzgar Hızı: " + str(wind) +" km/s" + \
                 "\n" + "Gün doğumu (A:M): " + sunrise + \
                 "\n" + "Gün batımı (P:M): " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Marasel Hava durumu")
canvas.configure(background = "#8FAADC")
canvas.iconbitmap("C:\icon.ico")
greeting = tk.Label(text="09.02.2021 | Versiyon 1.0")
greeting.config(font = ("poppins",20))
greeting.pack()
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")
textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)
label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()
canvas.mainloop()