# Patient Management System Documentation


## Table of Contents

1. Overview
2. Installation
3. Setup
4. Usage
5. Functionality
6. Examples
7. Functions




1.	Overview

The Patient Management System is a Python-based application that provides a user-friendly interface for managing patient data stored in a MySQL database. It offers a range of features to streamline the process of organizing and accessing patient information.

1.	Connecting to the Database: The system establishes a connection to the MySQL database, allowing seamless interaction with the patient data.

2.	Sorting and Displaying Patients by Department: Users can input a specific department name, and the system retrieves and displays all patients associated with that department. This feature facilitates efficient organization and retrieval of patient records based on departmental categorization.

3.	Assigning Doctors to Patients: The system provides the functionality to assign doctors to patients within a specific department. This enables effective tracking of patient-doctor relationships and ensures appropriate medical care.

4.	Generating Formatted Tables: The application utilizes the tabulate library to create visually appealing and well-structured tables for displaying patient information. This enhances readability and simplifies data interpretation for users.

5.	Saving Patient Data to CSV: Users can export patient data displayed in the table format to a CSV (Comma-Separated Values) file. This feature enables data portability and allows for further analysis or integration with other systems.

By combining these features, the Patient Management System offers healthcare professionals and administrators a comprehensive tool to efficiently manage patient data, streamline workflows, and enhance the overall quality of patient care.



2.	Installation
To use the Patient Management System, ensure that you have the following dependencies installed on your system:
•	Python 3.x
•	MySQL Connector/Python: Install it using pip install mysql-connector-python
•	Tabulate: Install it using pip install tabulate



3.	Setup
Before running the program, perform the following steps:
•	Create a MySQL database named "patients".
•	Within the "patients" database, create a table named "patients" using the provided schema.
•	Insert some sample patient data into the "patients" table.


4.	Usage
•	Run the patient_management_system.py script using python patient_management_system.py.
•	Enter the department name to sort and display patients. Type 'q' to quit the program.
•	The system will show the assigned doctors for the selected department and display a table with patient data and their assigned doctors.
•	Optionally, you can save the patient data table to a CSV file by providing a filename when prompted.


5.	Functionality
The Patient Management System comprises the following modules and functions:
1.	connect_to_database()
•	Purpose: Establishes a connection with the MySQL database.
•	Parameters: None
•	Returns: The database connection object.
2.	sort_patients_by_department(connection, department)
•	Purpose: Retrieves patients belonging to a specific department from the database.
•	Parameters:
•	connection: The database connection object.
•	department: The name of the department to sort patients by.
•	Returns: A list of patients belonging to the specified department.
3.	get_doctors_by_department(department)
•	Purpose: Returns a list of doctors associated with a department.
•	Parameters:
•	department: The name of the department.
•	Returns: A list of doctors for the specified department.
4.	create_patient_table(patients, doctors)
•	Purpose: Generates a formatted table displaying patient data and their assigned doctors.
•	Parameters:
•	patients: A list of patient data.
•	doctors: A list of doctors corresponding to the patients' department.
•	Returns: A formatted table string.

5.	save_table_to_csv(table)
•	Purpose: Saves the patient data table to a CSV file.
•	Parameters:
•	table: The patient data table to be saved.
•	Returns: None

6.	main()
•	Purpose: The main entry point of the program, manages user interactions and controls the program flow.
•	Parameters: None
•	Returns: None


Examples
Sorting and Displaying Patient Data:
•	Department: Cardiology
•	Assigned Doctors: Dr. Anderson, Dr. Martinez, Dr. Taylor, Dr. Thomas, Dr. Harris
•	Patient Data:

Patient_id | Patient Name | Contact No. | Department | Assigned Doctor |  | Age | Gender
-----------|--------------|-------------|------------|-----------------|--|-----|-------
1          | John Doe     | 1234567890  | Cardiology | Dr. Anderson    |  | 35  | M
2          | Jane Smith   | 9876543210  | Cardiology | Dr. Martinez    |  | 28  | F
