import requests
s_city = "Ulan-Ude,RU"
city_id = 0
appid = "90afe3b298d718f5e67e53c78c8b4768"

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id=', city_id)
except Exception as e:
    print("Exception (find):", e)
    pass

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    print(weather)
    print(temp)
except Exception as e:
    print("Exception (find):", e)
    pass

