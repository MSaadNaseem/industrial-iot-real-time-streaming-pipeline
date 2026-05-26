import json
import base64
import boto3
import os
from datetime import datetime

s3 = boto3.client("s3")
BUCKET_NAME = os.environ["S3_BUCKET"]

def transform(data):

    # derived metric
    data["temperature_f"] = round((data["temperature"] * 9/5) + 32, 2)

    # health score
    data["health_score"] = round(
        100 - (data["vibration"] * 10 + data["pressure"] * 0.5),
        2
    )

    # alert classification
    if data["temperature"] > 90 or data["vibration"] > 2:
        data["alert_level"] = "CRITICAL"
    elif data["temperature"] > 80:
        data["alert_level"] = "WARNING"
    else:
        data["alert_level"] = "NORMAL"

    # metadata
    data["processed_at"] = datetime.utcnow().isoformat()

    return data


def lambda_handler(event, context):

    for record in event["Records"]:

        payload = base64.b64decode(record["kinesis"]["data"])
        data = json.loads(payload)

        transformed_data = transform(data)

        now = datetime.utcnow()

        file_path = (
            f"iot-data/"
            f"year={now.year}/month={now.month:02d}/day={now.day:02d}/"
            f"{data['machine_id']}_{now.isoformat()}.json"
        )

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_path,
            Body=json.dumps(transformed_data)
        )

    return {"statusCode": 200}