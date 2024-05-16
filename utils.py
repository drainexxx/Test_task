import requests

def get_weather_data(city):
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'.format(city)

    res = requests.get(url)
    data = res.json()

    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']

    print(city,':')
    print('Температура:',temp,'°C')
    print('Ветер:',wind)
    print('Давление: ',pressure)
    print('Влажность: ',humidity)
    print('Описание:',description, '\n')

    return city, temp, wind, pressure, humidity, description