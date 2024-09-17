from app import app

def test_home_instructions():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'Welcome to the Calculator App!' in response.data
    assert b'Use the following format to calculate:' in response.data

def test_calculate_add():
    response = app.test_client().get('/?operation=add&num1=5&num2=3')
    assert response.status_code == 200
    assert response.json['result'] == 8

def test_calculate_subtract():
    response = app.test_client().get('/?operation=subtract&num1=10&num2=4')
    assert response.status_code == 200
    assert response.json['result'] == 6

def test_calculate_multiply():
    response = app.test_client().get('/?operation=multiply&num1=6&num2=7')
    assert response.status_code == 200
    assert response.json['result'] == 42

def test_calculate_divide():
    response = app.test_client().get('/?operation=divide&num1=20&num2=5')
    assert response.status_code == 200
    assert response.json['result'] == 4

def test_calculate_divide_by_zero():
    response = app.test_client().get('/?operation=divide&num1=10&num2=0')
    assert response.status_code == 400
    assert 'error' in response.json

def test_calculate_invalid_operation():
    response = app.test_client().get('/?operation=invalid&num1=5&num2=3')
    assert response.status_code == 400
    assert 'error' in response.json

def test_calculate_invalid_input():
    response = app.test_client().get('/?operation=add&num1=5&num2=abc')
    assert response.status_code == 400
    assert 'error' in response.json