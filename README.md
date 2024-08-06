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

##Images
The Homepage
![image](https://github.com/user-attachments/assets/25cbca89-e556-47c6-ae67-3ced503a3dbc)


## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure to follow the coding standards and include relevant tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
