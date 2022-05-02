import kafka
import json
import requests
from kafka import KafkaConsumer

# utiliser kafka
consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'], api_version='2.0.0', group_id="test_id", value_deserializer = json.loads, max_poll_records = 1000)
print('before for ')
#for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # # e.g., for unicode: `message.value.decode('utf-8')`
    #print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
for msg in consumer:
    print('IN for')
    #print(type(consumer))
    print(json.loads(msg.value.decode()))
print(json.loads(consumer.seek()))
#print(consumer)