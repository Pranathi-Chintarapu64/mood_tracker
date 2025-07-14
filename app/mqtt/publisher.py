import paho.mqtt.client as mqtt
import os

MQTT_BROKER = os.getenv("MQTT_HOST", "efd8e825.ala.dedicated.aws.emqxcloud.com")
MQTT_PORT = int(os.getenv("MQTT_PORT", 8883))
MQTT_USERNAME = os.getenv("MQTT_USERNAME", "mood_user")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD", "strongpassword123")
MQTT_TOPIC = "mood/reminder"

def publish_reminder(user_id: int, message: str = None):
    client = mqtt.Client()
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.tls_set()

    print(f"Connecting to MQTT broker {MQTT_BROKER}:{MQTT_PORT} ...")
    client.connect(MQTT_BROKER, MQTT_PORT)
    client.loop_start()

    if not message:
        message = f"Hey User {user_id}, don't forget to log your mood!"

    result = client.publish(MQTT_TOPIC, message)
    print(f"[MQTT] Sent: {message} to {MQTT_TOPIC} (result={result.rc})")

    client.loop_stop()
    client.disconnect()
