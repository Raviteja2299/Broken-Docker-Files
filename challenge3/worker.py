import requests
import time

while True:
    print("Worker running...")
    response = requests.get("https://example.com")
    print(response.status_code)
    time.sleep(5)
