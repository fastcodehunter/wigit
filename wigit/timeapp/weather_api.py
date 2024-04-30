import requests
import datetime
import pytz

class WeatherCollector:
    api_ip = 'https://api.ipify.org?format=json'
    key = 'ed7d9cc96d1e9b56c49384fc30f9187e'
    
    def __init__(self):
        self.data = self.ip_address()
        self.time = self.time_zone(self.data)
        self.weather_data = self.weather()
        
    def ip_address(self):
        response_ip = requests.get(self.api_ip).json()['ip']
        return requests.get(f"http://ip-api.com/json/{response_ip}").json()
    
    def time_zone(self, ip_address):
        tz = pytz.timezone(ip_address['timezone'])
        now_time = datetime.datetime.now(tz)
        return now_time.strftime('%H:%M:%S')
    
    def weather(self):
        city = self.data['city']
        return requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.key}').json()

