import os
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"
MQTT_PORT = 1883

def main():

    # Create a client object for MQTT connections
    client = mqtt.Client()

    # Connect function might have a for loop.. testing on one
    # topic at the moment
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_SERVER, MQTT_PORT, 60)

    cli(client)


def cli(client):
    quits = {
    	"exit": "Quitting",
    	"quit": "Quitting",
    }
    # Main Loop
    while(1):
        uinput = input('$ ')

        # check if input is a valid command
        if uinput is "show topics":
            show_topics()
        elif uinput is "delete topic":
            delete_topic()
        elif uinput is "add topic":
            add_topic()
        elif uinput is "msg":
            send_msg()
        elif uinput is "?help":
            show_help()
        elif uinput in quits:
            print("Quitting...")
            exit(0)
        else:
            print("Invalid command, type ?help for more info.")

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        client.loop_forever()


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    # more callbacks, etc

def show_topics():
    print("show topics")

def delete_topic():
    print("delete topic")

def add_topic():
    print("add topic")

def send_msg():
    print("send message")

def show_help():
    print("show help")


if __name__ == '__main__':
    main()
