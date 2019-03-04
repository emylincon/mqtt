import time
import paho.mqtt.client as mqtt
import os

# https://www.youtube.com/watch?v=4vU2iZWdNTg
# http://embeddedlaboratory.blogspot.com/2018/01/getting-started-with-mqtt-using-python.html


# Callback Function on Connection with MQTT Server
def on_connect(client, userdata, flags, rc):
    print("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    client.subscribe("test/#")


# Callback Function on Receiving the Subscribed Topic/Message
def on_message(message_client, userdata, msg):
    # print the message received from the subscribed topic
    print(str(msg.payload, 'utf-8'))


def publish(message='Auto: Hello World, Its me'):
    host = '192.168.40.222'
    topic = 'test'
    cmd = 'mosquitto_pub -h {} -t "{}" -m "{}" -u "admin" -P "password"'.format(host, topic, message)
    os.system(cmd)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("admin", "password")
client.connect("192.168.40.222", 1883, 60)

# client.loop_forever()
client.loop_start()
time.sleep(1)
while True:
    try:
        publish()
        time.sleep(15)
    except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()
