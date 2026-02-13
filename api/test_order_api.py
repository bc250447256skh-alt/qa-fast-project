import requests
import time

def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    start_time = time.time()
    response = requests.post(url, json=payload)
    response_time = time.time() - start_time

    print("Response time:", response_time)

    # Status code
    assert response.status_code == 201

    # JSON fields
    data = response.json()
    assert "id" in data

    # Performance check
    assert response_time < 2

