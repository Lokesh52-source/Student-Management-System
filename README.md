# Student Management System

A Python-based Student Management System developed to practice Python programming, file handling, modular programming, data validation, and basic data analysis concepts.

## Project Overview

This project allows users to manage student records through a command-line interface.

The system supports:

- Adding students
- Viewing students
- Searching students
- Updating student information
- Deleting students
- Student performance reports
- Sorting students
- Exporting student data to CSV
- JSON data persistence
- Input validation

## Technologies Used

- Python
- JSON
- CSV
- Python Lists
- Python Dictionaries
- Functions
- Exception Handling
- File Handling
- Modules
- Lambda Functions

## Python Modules Used

### 1. json

Used to store and retrieve student data in JSON format.

```python
import json
```
<img width="665" height="917" alt="image" src="https://github.com/user-attachments/assets/4adfe24f-956e-4385-92e0-ddcf9a6d4d3d" />


### 2. pathlib

Used to create reliable file paths.

```python
from pathlib import Path
```

### 3. csv

Used to export student records into CSV format.

```python
import csv
```
<img width="1067" height="1029" alt="image" src="https://github.com/user-attachments/assets/bb6d398e-1df1-4dd2-98fe-33900dc74375" />


## Project Structure

```
StudentManagementSystem/
│
├── main.py
├── student_operations.py
├── validation.py
├── file_handler.py
├── student.json
├── students.csv
├── README.md
└── .gitignore
```
<img width="264" height="292" alt="image" src="https://github.com/user-attachments/assets/81e4fe55-650d-4e02-978d-18d405580b6d" />

## Module Description

### main.py

Responsible for:

- Displaying the menu
- Taking user choices
- Calling the appropriate functions
- Controlling the main program loop
 <img width="1915" height="1002" alt="Screenshot 2026-08-10 191040" src="https://github.com/user-attachments/assets/d94317c7-f02c-4936-b3f1-82a599dc953c" />


### student_operations.py

Contains the main student operations:

- Add Student
- View Students
- Search Student
- Update Student
- Delete Student
- Student Report
- Sorting
- CSV Export
 <img width="1904" height="1005" alt="image" src="https://github.com/user-attachments/assets/eea735b2-910d-40b6-9381-46d9aa670c36" />


### validation.py

Contains reusable validation functions for:

- Roll number
- Name
- Age
- Course
- Marks
 <img width="1919" height="1005" alt="Screenshot 2026-08-10 191409" src="https://github.com/user-attachments/assets/67f8652d-9cd6-4559-852a-434ea639050b" />


### file_handler.py

Responsible for:

- Loading student data from JSON
- Saving student data to JSON
- Handling missing or invalid JSON files
 <img width="1906" height="955" alt="image" src="https://github.com/user-attachments/assets/2ced491f-665d-4938-a7f7-0cbd9ac33826" />


## Features

### Add Student

Users can add a new student by entering:

- Roll Number
- Name
- Age
- Course
- Marks
 <img width="1907" height="1002" alt="image" src="https://github.com/user-attachments/assets/f319ebd3-809f-46cb-aade-d9bddc33638c" />


The system checks whether the roll number already exists.

### View Students

Displays all student records in a formatted table.
<img width="1919" height="1002" alt="image" src="https://github.com/user-attachments/assets/00feed74-3180-4073-8080-a5db0cafbebd" />


### Search Student

Searches for a student using the unique roll number.
<img width="1915" height="862" alt="Screenshot 2026-08-10 192003" src="https://github.com/user-attachments/assets/74b9b68a-bd11-4c91-9d52-d9336c04b3a9" />


### Update Student

Allows users to update:

- Name
- Age
- Course
- Marks
 <img width="1907" height="958" alt="Screenshot 2026-08-10 194643" src="https://github.com/user-attachments/assets/6a328816-ff10-4d75-a23d-be9ec09b3ab8" />


### Delete Student

Deletes a student after asking for confirmation.
<img width="1918" height="920" alt="Screenshot 2026-08-10 195102" src="https://github.com/user-attachments/assets/6f10e8ec-199f-4f56-888e-0760f77c6f8d" />


### Student Report

Generates basic performance statistics including:

- Total students
- Highest marks
- Lowest marks
- Average marks
- Top scorer
- Pass students
- Fail students
   <img width="1908" height="889" alt="Screenshot 2026-08-10 194849" src="https://github.com/user-attachments/assets/ce41820b-f9f2-486e-8b6f-58795634ccaa" />


### Sorting

Allows student records to be sorted based on selected criteria such as marks.

### CSV Export

Exports student data to:

```
students.csv
```
<img width="1912" height="640" alt="Screenshot 2026-08-10 200850" src="https://github.com/user-attachments/assets/b6d67a72-776d-4159-aff4-c120fbdbce1a" />


The CSV file can be opened using Excel or other spreadsheet applications.

## Data Persistence

Student data is stored in:

```
student.json
```
<img width="1831" height="935" alt="Screenshot 2026-08-10 190843" src="https://github.com/user-attachments/assets/945c3121-0155-40f0-bca8-ecdf4b9fc063" />


When the program starts, existing data is loaded from the JSON file.
When a student is added, updated, or deleted, the JSON file is updated.

## Input Validation

The project validates user input to prevent invalid data.

Examples:

- Roll number must be positive
- Name cannot be empty
- Age must be within the allowed range
- Marks must be between 0 and 100
- Invalid numeric input is handled using exception handling

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/StudentManagementSystem.git
   cd StudentManagementSystem
   ```
2. Run the program:
   ```bash
   python main.py
   ```
3. Follow the on-screen menu to add, view, search, update, delete, sort, or export student records.

## Concepts Practiced

This project helped me practice:

- Variables
- Data types
- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- List iteration
- Dictionary access
- Exception handling
- File handling
- JSON
- CSV
- Modular programming
- Lambda functions
- Basic data processing

## License

This project is open source and available for learning purposes.
