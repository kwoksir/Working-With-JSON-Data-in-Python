import json
import requests

urljson = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=fnd&lang=tc')

getData = json.loads(urljson.text)

weatherList = getData['weatherForecast']

for dayW in weatherList:
    print(dayW['week'] + ":" + dayW['forecastWeather'])


