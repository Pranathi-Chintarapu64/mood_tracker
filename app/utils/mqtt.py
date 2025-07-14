import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv
import paho.mqtt.publish as publish

load_dotenv()

MQTT_BROKER = os.getenv("MQTT_BROKER_URL")
MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")

client = mqtt.Client()

def connect_mqtt():
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.connect(MQTT_BROKER.split("://")[-1])
    client.loop_start()

def publish_message(topic: str, message: str):
    client.publish(topic, message)

def publish_reminder(topic: str, message: str):
    publish.single(
        topic,
        payload=message,
        hostname="efd8e825.ala.dedicated.aws.emqxcloud.com",  # replace with actual EMQX host
        port=1883,
        auth={'username': 'mood_user', 'password': 'strongpassword123'},
        qos=1
    )