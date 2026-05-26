import random
from datetime import datetime

def generate_sensor_data():

    return {
        "plant": "Plant-A",
        "machine_id": f"MACHINE-{random.randint(100,105)}",
        "temperature": round(random.uniform(65, 95), 2),
        "pressure": round(random.uniform(20, 40), 2),
        "vibration": round(random.uniform(0.1, 2.5), 2),
        "rpm": random.randint(1000, 3000),
        "power_consumption": round(random.uniform(200, 500), 2),
        "status": random.choice([
            "RUNNING",
            "IDLE",
            "WARNING"
        ]),
        "timestamp": datetime.utcnow().isoformat()
    }