import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)


# Callback Function on Connection with MQTT Server
def on_connect(connect_client, userdata, flags, rc):
    print("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    connect_client.subscribe("test")


# Callback Function on Receiving the Subscribed Topic/Message
def on_message(message_client, userdata, msg):
    # print the message received from the subscribed topic
    message = str(msg.payload, 'utf-8')
    print(message)
    if message.strip() == 'lights on':
        GPIO.output(4, True)
    elif message.strip() == 'lights off':
        GPIO.output(4, False)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("admin", "password")
client.connect("192.168.40.222", 1883, 60)

client.loop_forever()