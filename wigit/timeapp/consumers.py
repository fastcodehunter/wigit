from channels.generic.websocket import WebsocketConsumer
import json
from time import sleep
from datetime import datetime


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        while True:
            get_time=datetime.now()
            ttime=get_time.strftime('%H:%M:%S')
            self.send(json.dumps({'nowtime':ttime}))
            sleep(1)

        