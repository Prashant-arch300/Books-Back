# Books-Back
Book Management
This is a simple book management system that allows users to view details about books stored in a CSV file. The system has a backend implemented using Python and the Django framework, and a frontend implemented using HTML, CSS, and JavaScript.

Getting Started
To run this project, you'll need to have Python 3 and pip installed on your machine. You'll also need to create a virtual environment to install the required Python packages.

Clone this repository to your local machine.
Create a virtual environment by running the following command: python -m venv env.
Activate the virtual environment by running the appropriate command for your operating system:
For Windows: .\env\Scripts\activate
For Linux/MacOS: source env/bin/activate
Install the required Python packages by running the following command: pip install -r requirements.txt.
Migrate the database by running the following command: python manage.py migrate.
Create a superuser by running the following command: python manage.py createsuperuser.
Run the development server by running the following command: python manage.py runserver.
You should now be able to access the Book Management system by navigating to http://localhost:8000 in your web browser.

Features
The Book Management system has the following features:

Login page: Users can log in with their email and password.
Book details page: Users can view details about books stored in the CSV file. The details are displayed in a tabular format.
Logout button: Users can log out of the system by clicking the Logout button.
Technologies Used
The following technologies were used in the implementation of this project:

Python 3
Django
Django REST framework
HTML
CSS
JavaScript
