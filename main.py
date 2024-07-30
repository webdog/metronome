import random

from dotenv import load_dotenv
from datetime import datetime, timezone
from os import getenv
from uuid import uuid4
import requests
from time import sleep

load_dotenv()

BASE_URL = "https://api.metronome.com/v1"


def send_usage(count=1):
    rlist = []
    rdict = {}
    for c in range(count):
        now = datetime.now(timezone.utc)
        rdict["timestamp"] = now.isoformat()
        rdict["transaction_id"] = str(uuid4())
        rdict["customer_id"] = getenv("CUSTOMER_ID")
        rdict["event_type"] = "hour_consumed"
        rdict["properties"] = {
            "cloud_provider": "aws"
        }
        rlist.append(rdict)

    return rlist


headers = {
    "Authorization": f"Bearer {getenv('API_TOKEN')}"
}

for each in range(random.randint(1, 125)):
    r = requests.post(f"{BASE_URL}/ingest", headers=headers, json=send_usage())
    sleep(0.25)
    print(r.status_code, r.text)
