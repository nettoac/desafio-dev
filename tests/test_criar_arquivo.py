from fastapi.testclient import TestClient
from main import app
from io import BytesIO

client = TestClient(app)

def test_create_upload_file():
    contents = b'5201903010000013200556418150633123****7687145607MARIA JOSEFINALOJA DO A - MATRIZ'
    file = BytesIO(contents)
    response = client.post("/uploadfile/", files={"file": ("file.txt", file)})
    assert response.status_code == 200
