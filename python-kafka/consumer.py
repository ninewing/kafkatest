from kafka import KafkaConsumer
consumer = KafkaConsumer(bootstrap_servers='localhost:9093')
consumer.subscribe(['btc'])
for msg in consumer:
    #assert isinstance(msg.value, dict)
    print(msg.value)