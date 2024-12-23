# Campus Enrollement App

A student management application developed with Python, Tkinter, and MySQL. This project follows the MVC (Model-View-Controller) architecture for better separation of concerns. The project structure includes: **Model (`model.py`)** to handle database operations, **View (`view.py`)** to create and manage the user interface with Tkinter, **Controller (`controller.py`)** to coordinate between the view and the model, and **Main (`main.py`)** as the entry point to run the application.

## Features

- Add a student with the fields **Name**, **Surname**, and **Email**.
- Display a list of students in a graphical user interface (table).
- Delete a selected student.
- Persist data in a MySQL database.

## Prerequisites

1. **Python 3.x**
2. **MySQL**
3. **Python library `mysql-connector-python`**
4. **Python library `python-dotenv`**

## Installation

Clone the repository using `git clone <REPOSITORY_URL>` and navigate to the directory with `cd <REPOSITORY_NAME>`. Install the dependencies with:  
```bash
pip install mysql-connector-python python-dotenv
```
Set up a .env file in the project's root directory with your MySQL credentials:
  ```  
    USERNAME=YourUsername 
    PASSWORD=YourPassword
```
Create a MySQL database called gestion_etudiants using the following command:
```
    CREATE DATABASE gestion_etudiants;
```

## Usage 
Run the application using: 
```bash
    python3 main.py
```
Use the interface to add, view, or delete students. Fill out the form to add a student, see the list of students displayed in a table, and select a student to delete them from the database.


## License 
This project is licensed under the MIT License. See the LICENSE file for more information.