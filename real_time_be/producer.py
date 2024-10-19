from confluent_kafka import Producer
import json
import os
import dotenv

dotenv.load_dotenv()
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

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

producer = Producer(conf)

def send_location_update(location_data):
    try:
        location_message = json.dumps(location_data)
        print(f"Sending location update: {location_message}")
        producer.produce('location', value=location_message, callback=delivery_report)

        producer.poll(0)
        producer.flush()
    except Exception as e:
        print(f"Failed to send location update: {e}")

if __name__ == "__main__":
    location = {"latitude": 51.509865, "longitude": -0.118092}
    send_location_update(location)
