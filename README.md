# Course Management System

## Overview

This mini-project is a Course Management System developed as part of a Fullstack Development with Django course in my third year. The system allows for managing courses, student registrations, and more, showcasing skills in web development and database management.

## Technologies Used

- **HTML**: For structuring the web pages.
- **CSS**: For styling and layout.
- **Python**: With **Django** framework for backend development.
- **jQuery**: For enhancing user interface with AJAX.
- **AJAX**: For asynchronous data fetching.
- **MySQL**: For database management.

## Features

- **Student Management**: View and manage student details.
- **Course Enrollment**: Students can enroll in courses.
- **Course Management**: Admin can manage courses.
- **Search Functionality**: Search for courses and students using AJAX.

## Setup and Installation

To run this project locally, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/dhruth-in/Course-Management-System.git
    ```

2. **Navigate to the Project Directory**

    ```bash
    cd Course-Management-System
    ```

3. **Create and Activate a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install Required Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set Up the Database**

    Update the `DATABASES` setting in `settings.py` to configure MySQL, then run:

    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser (Optional)**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

8. **Access the Application**

    Open your browser and go to `http://127.0.0.1:8000/` to view the application.

## Project Structure

- `course_management/`: The main project directory.
- `course_app/`: The main application directory
- `templates/`: HTML templates for the frontend.
- `static/`: CSS, JavaScript, and other static files.

## Images

- **The Homepage**
  ![image](https://github.com/user-attachments/assets/00431144-1313-4812-a5df-a54fe6f226b2)

- **Enroll in a Course**
  ![image](https://github.com/user-attachments/assets/aedb6fc7-ff9a-47be-a5d5-2d6769180464)

- **Add Project**
  ![image](https://github.com/user-attachments/assets/ba5dd60f-73b4-41d9-8698-2f1ce94c82c7)

- **Course Search**
  ![image](https://github.com/user-attachments/assets/816d3606-6c30-4426-91fc-9702268bc6de)

- **Student List**
  ![image](https://github.com/user-attachments/assets/c9bb1fe5-78c4-4e2f-9bc3-330b80f31e7a)

- **Student Details**
  ![image](https://github.com/user-attachments/assets/4f77d812-3e21-47ed-9fac-4b259a23ec2b)


## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure to follow the coding standards and include relevant tests.

