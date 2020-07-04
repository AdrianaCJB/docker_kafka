import time
import random
from kafka import KafkaProducer
import json

# give broker IP from docker
producer = KafkaProducer(bootstrap_servers='localhost:9092')


for i in range(155):
    # data = { 'level' : 'sam',
    #          'message' : i
    #         }
    num = random.randint(0, 10)

    num_bytes = bytes(str(num), encoding='utf-8')
    
    data = { 'UserId' : i+1000,
             'ActivityType' : i+1000,
             'Amount' : 3.0,
             'CurrencyId' : i+1000,
             'Date' : '2020-02-20'
        }

    producer.send('axity_mx_topic', json.dumps(data).encode('utf-8'))
    time.sleep(1)