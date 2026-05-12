# Patient Management System (PMS)

A simple Python 3.12 application to perform CRUD operations on Patient entities, using a JSON file for data storage.

## Features
- Add, view, update, and delete patient records
- Data stored in a local JSON file
- CLI-based interface

## Getting Started

### 1. Create and Activate Virtual Environment
```
python -m venv venv
.\venv\Scripts\activate
```

### 2. Install Requirements
No external packages required for basic CRUD functionality.

### 3. Run the Application
```
python main.py
```

## Project Structure
- main.py: Entry point and CLI for CRUD operations
- patient_manager.py: Logic for managing patient data
- patients.json: Data file (auto-created)

## Next Steps
- Add CI/CD with GitHub Actions
- Extend features as needed
