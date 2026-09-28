def test_health(client):
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_homeab(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "About" in response.text


def test_homepro(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Customer" in response.text