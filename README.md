# Mindease

**Mindease** is a web-based application that enables users to book appointments for mental health sessions with professional psychologists. The project is designed to provide a seamless experience for users to schedule appointments while ensuring secure authentication and management.

## Project Structure

The project directory is organized as follows:

- **appointment/**: Contains all the logic related to managing appointments, such as models, views, and serializers.
- **authentication/**: Handles user authentication and registration.
- **core/**: Contains shared logic and settings for the project.
- **mindease/**: The main project directory housing global configurations.
- **static/**: Includes static files like CSS, JavaScript, and images.
- **staticfiles/**: A directory for collected static files after running `collectstatic`.
- **templates/**: Stores HTML templates used for rendering web pages.

## Requirements

The project relies on the dependencies listed in `requirements.txt`. Make sure you install these before running the project.

## Getting Started

Follow these steps to set up and run the project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/divine40/Mindease.git
cd Mindease
```

### 2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies.

For Linux/MacOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
Install all required packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
Run the following commands to apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
Create an admin account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

### 6. Run the Server
Start the development server:

```bash
python manage.py runserver
```
The application will be accessible at `http://127.0.0.1:8000/`


### AUTHOR
#### `DIVINE AKUNYIBA`
