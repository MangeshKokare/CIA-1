#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import mysql.connector
from tabulate import tabulate

# Connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mangesh@123",
            database="patients"
        )
        print("Connected to the database")
        return connection
    except mysql.connector.Error as error:
        print("Error while connecting to the database:", error)

# Sort patients by department
def sort_patients_by_department(connection, department):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM patients.patients WHERE Department_name = %s", (department,))
        patients = cursor.fetchall()
        return patients
    except mysql.connector.Error as error:
        print("Error while sorting patients by department:", error)

# Get doctors by department
def get_doctors_by_department(department):
    doctors = {
        "Nephrology": ["Dr. Smith", "Dr. Johnson", "Dr. Brown", "Dr. Wilson", "Dr. Davis"],
        "Cardiology": ["Dr. Anderson", "Dr. Martinez", "Dr. Taylor", "Dr. Thomas", "Dr. Harris"],
        "Neurology": ["Dr. Clark", "Dr. Lewis", "Dr. Lee", "Dr. Walker", "Dr. Hall"],
        "OT(Emergency)": ["Dr. Garcia", "Dr. Martin", "Dr. Rodriguez", "Dr. Martinez", "Dr. Lewis"],
        "Optometry": ["Dr. Adams", "Dr. Cooper", "Dr. Rogers", "Dr. Griffin", "Dr. Collins"],
        "Dental": ["Dr. Turner", "Dr. Moore", "Dr. Ward", "Dr. Nelson", "Dr. Reed"],
        "Physiotherapy": ["Dr. Murphy", "Dr. Baker", "Dr. Simmons", "Dr. Morris", "Dr. Foster"]
    }
    return doctors.get(department, [])

# Create a table for patients using tabulate
def create_patient_table(patients, doctors):
    headers = ["Patient_id", "Patient Name", "Contact No.", "Department", "Assigned Doctor","", "Age", "Gender"]
    table = []
    num_doctors = len(doctors)
    for i, patient in enumerate(patients):
        doctor = doctors[i % num_doctors]
        patient_with_doctor = list(patient)
        patient_with_doctor.insert(4, doctor)
        table.append(patient_with_doctor)
    table = tabulate(table, headers, tablefmt="fancy_grid")
    return table

# Save table to a CSV file
def save_table_to_csv(table):
    filename = input("Enter the filename to save the table (without extension): ")
    filename += ".csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(table)
    print("Table saved to", filename)

# Main program
def main():
    connection = connect_to_database()
    if connection:
        while True:
            department = input("Enter the department to sort patients (or 'q' to quit): ")
            if department.lower() in ["q", "quit"]:
                break
            patients = sort_patients_by_department(connection, department)
            if patients:
                doctors = get_doctors_by_department(department)
                if doctors:
                    print("Doctors assigned to the", department, "department:", doctors)
                    if len(patients) > len(doctors):
                        doctors = doctors * (len(patients) // len(doctors)) + doctors[:len(patients) % len(doctors)]
                    table = create_patient_table(patients, doctors)
                    print(table)
                    save_table_to_csv(patients)  # Save the patients data to CSV
                else:
                    print("No doctors found for the", department, "department.")
            else:
                print("No patients found for the", department, "department.")
        connection.close()

if __name__ == "__main__":
    main()


# In[ ]:




