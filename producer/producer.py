import json
import time
import boto3

from sensor_generator import generate_sensor_data
from config import STREAM_NAME, REGION

kinesis = boto3.client(
    "kinesis",
    region_name=REGION
)

def send_to_kinesis(data):

    response = kinesis.put_record(
        StreamName=STREAM_NAME,
        Data=json.dumps(data),
        PartitionKey=data["machine_id"]
    )

    print("Sent:", data)

    return response

def run():

    while True:

        try:
            sensor_data = generate_sensor_data()

            send_to_kinesis(sensor_data)

            time.sleep(5)

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    run()