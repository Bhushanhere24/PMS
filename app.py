from flask import Flask, request, jsonify, render_template
import patient_manager

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/patients', methods=['GET'])
def get_patients():
    return jsonify(patient_manager.get_all_patients())

@app.route('/api/patients', methods=['POST'])
def add_patient():
    data = request.json
    patient_manager.add_patient(data)
    return jsonify({'status': 'success'})

@app.route('/api/patients/<patient_id>', methods=['PUT'])
def update_patient(patient_id):
    data = request.json
    updated = patient_manager.update_patient(patient_id, data)
    return jsonify({'status': 'success' if updated else 'not found'})

@app.route('/api/patients/<patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    deleted = patient_manager.delete_patient(patient_id)
    return jsonify({'status': 'success' if deleted else 'not found'})

if __name__ == '__main__':
    app.run(debug=True)
