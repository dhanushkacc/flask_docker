from app import app

def test_home():
    responce = app.test_client().get('/')

    assert responce.status_code == 200
    assert responce.data == b'Hello, World!'