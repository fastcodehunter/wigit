import datetime
import requests
import json






def get_ip_addres():
    data_list=[]
    sourse='https://api.ipify.org?format=json'
    key='ed7d9cc96d1e9b56c49384fc30f9187e'
    response_ip=requests.get(sourse).json()['ip']
    data=requests.get(f"http://ip-api.com/json/{response_ip}").json()

    get_weather=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={data['city']}&appid={key}').json()
    return  get_weather
print(get_ip_addres())