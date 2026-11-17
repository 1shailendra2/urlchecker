import requests
BASE_URL = "https://jsonplaceholder.typicode.com/posts"
def test_get_post_ok():
    response = requests.get(f"{BASE_URL}/1" )
    assert response.status_code == 200
    assert response.json()["id"] == 1
def test_get_post_not_found():
    response = requests.get(f"{BASE_URL}/99999")
    assert response.status_code == 404
def test_create_post():
    body = {
        "title": "test",
        "body": "hello",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}", json=body)
    assert response.status_code == 201
    assert response.json()["title"] == "test"
    assert response.json()["body"] == "hello"
    assert response.json()["userId"] == 1
    print(response.request.headers)