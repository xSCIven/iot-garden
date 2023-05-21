import paho.mqtt.client as local_mqtt
import threading as threading
import queue as queue
import logging as logging

import time as time
from serial import Serial




def local_mqtt_t():
    while True:
        if not serial_data_queue.empty():
            data = serial_data_queue.get()
            local_mqtt_client.publish("sensors/ardunio1/temperature", data)
        #Calling mqtt.loop() will process the network traffic and callbacks
        local_mqtt_client.loop(timeout=1.0, max_packets=1)


def read_data_t():
    while True:
        data = serial.readline().decode().strip()
        try:
            data = float(data)
            serial_data_queue.put(data)
        except ValueError:
            #skip iteration if the value is not sensor data
            continue

        



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    #global makes the variable accessible to all scopes
    global serial
    serial = Serial(SERIAL_PORT1, SERIAL_BAUD_RATE)
    time.sleep(2)


    global local_mqtt_client
    local_mqtt_client = local_mqtt.Client()
    local_mqtt_client.connect("localhost", 1883)
    

    global serial_data_queue
    serial_data_queue = queue.Queue()

    # Start the functions concurrently using threads
    mqtt_thread = threading.Thread(target=local_mqtt_t)
    read_data_thread = threading.Thread(target=read_data_t)

    mqtt_thread.daemon = True
    read_data_thread.daemon = True


    read_data_thread.start()
    mqtt_thread.start()
