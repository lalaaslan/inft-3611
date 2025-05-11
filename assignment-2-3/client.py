import requests
import time

SERVICE_URL = "https://lala-aslan-960957615762.me-central1.run.app"
TEST_COUNT = 100

success_count = 0

for n in range(TEST_COUNT):
    try:
        response = requests.get(f"{SERVICE_URL}/getbalance", timeout=10)

        if response.status_code == 200:
            success_count += 1
            print(f"Request {n+1}: Success (HTTP {response.status_code})")

        else:
            print(f"Request {n + 1}: Failed (HTTP {response.status_code})")

    except requests.exceptions.RequestException as e:
        print(f"Request {n + 1}: Error - {str(e)}")

    time.sleep(1)
    