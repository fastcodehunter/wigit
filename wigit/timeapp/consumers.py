from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asyncio import sleep, create_task
from datetime import datetime
from pytz import timezone
from timeapp.weather_api import WeatherCollector

class WSConsumer(AsyncWebsocketConsumer):
    def __init__(self):
        super().__init__()
        self.weather = WeatherCollector()
        self.weather_task = None
    
    async def connect(self):
        await self.accept()
        geogesser = self.weather.data
        self.weather_task = create_task(self.weather_update())
        while True:
            now_time = self.weather.time_zone(geogesser)
            await self.send(json.dumps({'nowtime': now_time}))
            await sleep(1)
            
    async def weather_update(self):
        while True:
            weather_data = self.weather.weather()
            await self.send(json.dumps({'weather': weather_data}))
            await sleep(3600)
            
    async def disconnect(self):
        if self.weather_task:
            self.weather_task.cancel()