import threading

class MqttThread(threading.Thread):
    def __init__(self, threadID, client):
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        self.client.loop_forever()
