import random
import time
import boto3
import botocore.exceptions

# Make sure this matches your Firehose stream name exactly
DELIVERY_STREAM_NAME = "student-esli-stream"

# Explicit region to avoid any default-region surprises
client = boto3.client("firehose", region_name="eu-west-1")

with open("/data/exportVideos.json") as file:
    # Skip header line if there is one
    # If there is no header, you can remove this line
    _ = file.readline()

    for line in file:
        data = line.strip()
        if not data:
            continue

        print(data)

        try:
            client.put_record(
                DeliveryStreamName=DELIVERY_STREAM_NAME,
                Record={"Data": data.encode("utf-8")}
            )
        except botocore.exceptions.ClientError as e:
            print("PutRecord failed:", e)
            break

        sleep = random.randint(50, 100) / 50.0  # between 1.0 and 2.0 seconds
        time.sleep(sleep)
