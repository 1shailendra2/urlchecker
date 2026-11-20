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

def test_get_post_has_expected_fields():
    response = requests.get(f"{BASE_URL}/1")
    assert response.status_code == 200
    data = response.json()
    expected_fields = ["userId", "id", "title", "body"]
    for field in expected_fields:
        assert field in data 
def  test_get_post_wrong():
    response = requests.get(f"{BASE_URL}/abc")
    assert response.status_code == 404
def test_create_post_missing_fields():
    body = {
        "title": "test"
    }
    response = requests.post(f"{BASE_URL}", json=body)
    assert response.status_code == 201
    assert response.json()["title"] == "test"
    assert "body" not in response.json()
    assert "userId" not in response.json()