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

## Module Description

### main.py

Responsible for:

- Displaying the menu
- Taking user choices
- Calling the appropriate functions
- Controlling the main program loop

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

### validation.py

Contains reusable validation functions for:

- Roll number
- Name
- Age
- Course
- Marks

### file_handler.py

Responsible for:

- Loading student data from JSON
- Saving student data to JSON
- Handling missing or invalid JSON files

## Features

### Add Student

Users can add a new student by entering:

- Roll Number
- Name
- Age
- Course
- Marks

The system checks whether the roll number already exists.

### View Students

Displays all student records in a formatted table.

### Search Student

Searches for a student using the unique roll number.

### Update Student

Allows users to update:

- Name
- Age
- Course
- Marks

### Delete Student

Deletes a student after asking for confirmation.

### Student Report

Generates basic performance statistics including:

- Total students
- Highest marks
- Lowest marks
- Average marks
- Top scorer
- Pass students
- Fail students

### Sorting

Allows student records to be sorted based on selected criteria such as marks.

### CSV Export

Exports student data to:

```
students.csv
```

The CSV file can be opened using Excel or other spreadsheet applications.

## Data Persistence

Student data is stored in:

```
student.json
```

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
