# Django CRUD Application

This is a Django application that demonstrates basic CRUD (Create, Read, Update, Delete) operations.

## Features
- Signup/login
- Admin
- Create new customers
- Read and display customers
- Update existing customers
- Delete customers

## Technologies Used

- Python
- Django
- SQLite (default database)
- HTML/CSS
- JavaScript
- Bootstrap

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (version 3.6+)
- pip (Python package installer)
- virtualenv (optional, but recommended)

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment (optional, but recommended):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser (optional, for admin access):**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

7. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- To create a new user, login to admin and navigate to the admin/adduser and fill out the form.
- To view all users, login admin.
- To update a users, login to admin click the edit button next to the user you want to update, then modify the form and submit.
- To delete a user, lgoin to admin and click the delete button next to the user you want to remove.

## Project Structure

- `manage.py`: Command-line utility for administrative tasks.
- `main/`: Django app containing the CRUD operations.
  - `migrations/`: Database migrations.
  - `views.py`: Logic for handling requests and returning responses.
  - `models.py`: Database models.
  - `forms.py` : Database forms.
  - `urls.py`: URL routing.
- `templates/`: HTML templates.
- `static/`: Static files (CSS, JavaScript)
- `CRUDop/`: default app
  - `settings.py` : project settings.py
  - `urls.py` : main url rounting
- `db.sqlite3`: default database
