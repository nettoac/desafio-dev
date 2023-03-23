from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_ler_dados():
    response = client.get("/visualizar-dados")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "<html>" in response.text
