import json
from json import dumps
import requests
from kafka import KafkaProducer
import time
from kafka.errors import KafkaError
import logging
import urllib
import datetime

#key = "cee2a70a52ec18b2929008285005059f23ac5a34"
#url = "https://api.jcdecaux.com/vls/v1/stations?apiKey={}".format(key)
#producer = KafkaProducer(bootstrap_servers="localhost:9092")
#while True:
#    response = urllib.request.urlopen(url)
#    stations = json.loads(response.read().decode())
#    for station in stations:
#        producer.send("velib-stations", json.dumps(station).encode())
#    print("{} Produced {} station records".format(time.time(), len(stations)))
#    time.sleep(1)
# get data
res = requests.get('http://127.0.0.1:8880/twitter')
producer = KafkaProducer(bootstrap_servers=':9092', value_serializer=lambda x: json.dumps(x).encode('utf-8'))
while True:
    data = json.loads(res.content.decode('utf-8'))
    print("Produced {} amont of data".format( len(data)))
    producer.send(topic='test', value=data)
    time.sleep(1)
    producer.flush()