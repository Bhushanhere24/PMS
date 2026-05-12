import os
import patient_manager
from app import app

def test_web_add_and_get_patient():
    # Clean up before test
    if os.path.exists('patients.json'):
        os.remove('patients.json')
    client = app.test_client()
    # Add patient
    response = client.post('/api/patients', json={
        'id': '2', 'name': 'WebTest', 'age': '25', 'gender': 'F'
    })
    assert response.status_code == 200
    # Get patients
    response = client.get('/api/patients')
    data = response.get_json()
    assert any(p['id'] == '2' for p in data)
    print('Web add/get test passed.')

def test_web_delete_patient():
    client = app.test_client()
    response = client.delete('/api/patients/2')
    assert response.status_code == 200
    print('Web delete test passed.')

def run_web_tests():
    test_web_add_and_get_patient()
    test_web_delete_patient()
    print('All web tests passed.')

if __name__ == '__main__':
    run_web_tests()
