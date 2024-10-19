from confluent_kafka import Consumer, KafkaError
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()



conf = {
    'bootstrap.servers': 'realtimeloc-alwenpy.j.aivencloud.com:13284',
    'client.id': 'your-producer-id',
    'security.protocol': 'SASL_SSL',
    'group.id': 'consumer-group',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': os.getenv('KAFKA_USERNAME'),
    'sasl.password': os.getenv('KAFKA_PASSWORD'),
    'ssl.ca.location': 'ca.pem',
}

consumer = Consumer(conf)


def consume_location_updates():
    consumer.subscribe(['location'])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f"Error: {msg.error()}")
                    break

            # Decode and process the message
            location_data = msg.value().decode('utf-8')
            print(f"Received message: {location_data}")

            # Send a POST request to the Django backend to update location
            requests.post('http://localhost:8000/api/update_location/', json=json.loads(location_data))

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

   

# Example Usage
if __name__ == "__main__":
    consume_location_updates()
