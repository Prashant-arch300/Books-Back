import requests

def test_login_endpoint():
    # Test a successful login
    response = requests.post('http://localhost:8000/login', json={'email': 'user@example.com', 'password': 'password123'})
    assert response.status_code == 200
    assert 'success' in response.json()
    
    # Test a failed login
    response = requests.post('http://localhost:8000/login', json={'email': 'user@example.com', 'password': 'wrongpassword'})
    assert response.status_code == 401
    assert 'error' in response.json()
