import requests
import sys

def test_smoke():
    """
    Simple smoke test to check if the application is responding.
    Assuming the app runs on localhost:8000
    """
    url = "http://localhost:8000"
    for _ in range(5):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Smoke test passed: Service is up and responding 200 OK.")
                return
            else:
                print(f"Smoke test failed: Service responded with {response.status_code}")
                sys.exit(1)
        except requests.exceptions.ConnectionError:
            import time
            print("Connection failed, retrying in 2 seconds...")
            time.sleep(2)
    
    print("Smoke test failed: Could not connect to the service after multiple retries.")
    sys.exit(1)

if __name__ == "__main__":
    test_smoke()
