from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["application"] == "Airline Booking API"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_flights():
    client = app.test_client()

    response = client.get("/flights")

    assert response.status_code == 200
    assert len(response.json) == 3