from patient_manager import *

def print_menu():
    print("\nPatient Management System")
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. Find Patient by ID")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter choice: ")
        if choice == '1':
            id = input("Enter ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            gender = input("Enter Gender: ")
            add_patient({'id': id, 'name': name, 'age': age, 'gender': gender})
            print("Patient added.")
        elif choice == '2':
            patients = get_all_patients()
            if not patients:
                print("No patients found.")
            for p in patients:
                print(p)
        elif choice == '3':
            id = input("Enter Patient ID: ")
            patient = find_patient(id)
            if patient:
                print(patient)
            else:
                print("Patient not found.")
        elif choice == '4':
            id = input("Enter Patient ID to update: ")
            patient = find_patient(id)
            if not patient:
                print("Patient not found.")
                continue
            name = input(f"Enter Name [{patient['name']}]: ") or patient['name']
            age = input(f"Enter Age [{patient['age']}]: ") or patient['age']
            gender = input(f"Enter Gender [{patient['gender']}]: ") or patient['gender']
            updated = update_patient(id, {'name': name, 'age': age, 'gender': gender})
            if updated:
                print("Patient updated.")
            else:
                print("Update failed.")
        elif choice == '5':
            id = input("Enter Patient ID to delete: ")
            deleted = delete_patient(id)
            if deleted:
                print("Patient deleted.")
            else:
                print("Patient not found.")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
