import requests
import subprocess
import time

# inicia servidor antes dos testes
def setup_module():
    global server
    server = subprocess.Popen(["python", "calculator/app.py"])
    time.sleep(1)

def teardown_module():
    server.terminate()

def test_api_soma():
    resp = requests.post(
        "http://127.0.0.1:5000/calc",
        json={"a": 2, "b": 5, "op": "+"}
    )
    assert resp.status_code == 200
    assert resp.json()["result"] == 7
