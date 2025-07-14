import paho.mqtt.client as mqtt

BROKER = "efd8e825.ala.dedicated.aws.emqxcloud.com"
PORT = 8883
TOPIC = "mood/reminder"

USERNAME = "mood_user"
PASSWORD = "strongpassword123"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    if rc == 0:
        client.subscribe(TOPIC)
        print(f"Subscribed to: {TOPIC}")
    else:
        print("Connection failed")

def on_message(client, userdata, msg):
    print(f"MQTT Message Received: {msg.topic} -> {msg.payload.decode()}")

client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()  

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
print("[MQTT] Subscriber connected and running...")
client.loop_forever()
