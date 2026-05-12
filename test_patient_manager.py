import os
import json
import patient_manager

def test_add_and_find_patient():
    # Clean up before test
    if os.path.exists('patients.json'):
        os.remove('patients.json')
    patient = {'id': '1', 'name': 'Test', 'age': '30', 'gender': 'M'}
    patient_manager.add_patient(patient)
    found = patient_manager.find_patient('1')
    assert found is not None, 'Patient not found after adding.'
    assert found['name'] == 'Test', 'Patient name mismatch.'

def test_update_patient():
    updated = patient_manager.update_patient('1', {'name': 'Updated'})
    assert updated, 'Update failed.'
    found = patient_manager.find_patient('1')
    assert found['name'] == 'Updated', 'Patient not updated.'

def test_delete_patient():
    deleted = patient_manager.delete_patient('1')
    assert deleted, 'Delete failed.'
    found = patient_manager.find_patient('1')
    assert found is None, 'Patient not deleted.'

def run_tests():
    test_add_and_find_patient()
    test_update_patient()
    test_delete_patient()
    print('All tests passed.')

if __name__ == '__main__':
    run_tests()
