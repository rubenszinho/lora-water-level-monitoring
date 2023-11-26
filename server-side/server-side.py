import os
from flask import Flask, jsonify, request, send_from_directory
from pymongo import MongoClient
from datetime import datetime
import paho.mqtt.client as mqtt
from threading import Thread
from datetime import datetime, timezone

app = Flask(__name__, static_folder='build/static', template_folder='build')

# Configurações do MQTT
MQTT_BROKER = "andromeda.lasdpc.icmc.usp.br"
MQTT_PORT = 7046
MQTT_TOPIC = "enoe/nivelrio"
MQTT_USERNAME = "giot06"
MQTT_PASSWORD = "YhW6Mt3O"

# Configurações do MongoDB
MONGO_URI = 'mongodb://mongodb:27017/'
DB_NAME = 'loradb'
COLLECTION_NAME = 'sensor_data'

# Conectar ao MongoDB
mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DB_NAME]
collection = db[COLLECTION_NAME]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        current_message = msg.payload.decode()
        print(f"Received `{current_message}` from `{msg.topic}` topic")

        result = collection.update_one(
            {'sensor_id': '1'},
            {'$set': {
                'value': current_message,
                'timestamp': datetime.now().isoformat() + "Z"
            }},
            upsert=True
        )
        print(f"MongoDB document updated. Modified count: {result.modified_count}")

    except Exception as e:
        print(f"An error occurred in on_message: {e}")

@app.route('/')
def index():
    return send_from_directory(app.template_folder, 'index.html')

@app.route('/<path:path>')
def send_file(path):
    return send_from_directory(app.static_folder, path)

@app.route('/sensor_data', methods=['GET'])
def get_sensor_data():
    sensor_id = request.args.get('sensor_id')

    if sensor_id:
        sensor_data = collection.find_one({'sensor_id': sensor_id}, {'_id': False})
        if sensor_data:
            return jsonify(sensor_data)
        else:
            return jsonify({'error': 'Sensor not found'}), 404
    else:
        return jsonify({'error': 'Sensor ID is required'}), 400

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

from threading import Thread
def start_mqtt_loop():
    mqtt_client.loop_forever()

mqtt_thread = Thread(target=start_mqtt_loop)
mqtt_thread.start()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
