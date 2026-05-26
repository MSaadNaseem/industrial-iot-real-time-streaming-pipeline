import os
from dotenv import load_dotenv

load_dotenv()

REGION = os.getenv("AWS_REGION")
STREAM_NAME = os.getenv("STREAM_NAME")
PLANT_NAME = os.getenv("PLANT_NAME")

if not REGION:
    raise ValueError("AWS_REGION not set")

if not STREAM_NAME:
    raise ValueError("STREAM_NAME not set")

if not PLANT_NAME:
    raise ValueError("PLANT_NAME not set")