from kafka import KafkaConsumer

# continuous loop
var = 1
while var == 1:

    # initialize consumer to given topic and broker
    consumer = KafkaConsumer('sample',
                            bootstrap_servers='localhost:9092')

    # loop and print messages
    for msg in consumer:
        print (msg)