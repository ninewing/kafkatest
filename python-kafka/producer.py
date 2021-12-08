from kafka import KafkaProducer
import json
import time
from datetime import datetime

#producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

sr = open('btc.csv', 'r')
sr.readline()
messages = []
for line in sr:
    data = line.replace('K', '').split(',')
    messages.append([float(data[1]), float(data[2]), float(data[3]), float(data[4])])
sr.close()
while True:
    for i in range(len(messages)):
        message = {
            'date': datetime.now().isoformat(),
            'close': messages[i][0],
            'open': messages[i][1],
            'high': messages[i][2],
            'low': messages[i][3],
        }
        producer.send('btc', message)
        #print(f'send at: {datetime.now().isoformat()}')
        time.sleep(5)
