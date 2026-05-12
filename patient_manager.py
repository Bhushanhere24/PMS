import json
import os

DATA_FILE = 'patients.json'

def load_patients():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_patients(patients):
    with open(DATA_FILE, 'w') as f:
        json.dump(patients, f, indent=4)

def add_patient(patient):
    patients = load_patients()
    patients.append(patient)
    save_patients(patients)

def get_all_patients():
    return load_patients()

def find_patient(patient_id):
    patients = load_patients()
    for p in patients:
        if p['id'] == patient_id:
            return p
    return None

def update_patient(patient_id, updated_data):
    patients = load_patients()
    for i, p in enumerate(patients):
        if p['id'] == patient_id:
            patients[i].update(updated_data)
            save_patients(patients)
            return True
    return False

def delete_patient(patient_id):
    patients = load_patients()
    new_patients = [p for p in patients if p['id'] != patient_id]
    if len(new_patients) != len(patients):
        save_patients(new_patients)
        return True
    return False
