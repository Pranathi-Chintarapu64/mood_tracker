import os
import paho.mqtt.publish as publish
from dotenv import load_dotenv

load_dotenv()

MQTT_HOST = os.getenv("MQTT_HOST")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")



def publish_report_status(user_id: int, message: str):
    topic = f"reports/notify"
    payload = f"User {user_id}: {message}"
    try:
        publish.single(
            topic=topic,
            payload=payload,
            hostname=MQTT_HOST,
            port=MQTT_PORT,
            auth={"username": MQTT_USERNAME, "password": MQTT_PASSWORD}
        )
        print(f"[MQTT] Published to {topic}: {payload}")
    except Exception as e:
        print(f"[MQTT] Failed to publish message: {e}")


def publish_reminder(user_id: int, message: str):
    topic = f"mood/reminder"  # <- FIXED
    payload = f"User {user_id}: {message}"

    print(f"Connecting to MQTT @ {MQTT_HOST}:{MQTT_PORT}")
    print(f"Publishing to topic: {topic} | Payload: {payload}")
    try:
        publish.single(
            topic=topic,
            payload=payload,
            hostname=MQTT_HOST,
            port=MQTT_PORT,
            auth={"username": MQTT_USERNAME, "password": MQTT_PASSWORD},
            tls={'cert_reqs': 0}
        )
        print(" MQTT message published successfully")
    except Exception as e:
        print("Failed to publish MQTT message:", e)


