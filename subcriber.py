import paho.mqtt.client as mqtt

# Define the callback for connection
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code {rc}")
    client.subscribe("test/topic")

# Define the callback for incoming messages
def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

# Create a client instance
client = mqtt.Client()

# Register callbacks using the new API
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect("localhost", 1883, 60)

# Start the network loop
client.loop_forever()
