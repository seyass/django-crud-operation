# Django CRUD Application

This is a Django application that demonstrates basic CRUD (Create, Read, Update, Delete) operations.

## Features

- Create new customers
- Read and display records
- Update existing records
- Delete records

## Technologies Used

- Python
- Django
- SQLite (default database)
- HTML/CSS
- JavaScript (if applicable)

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

- To create a new record, navigate to the create page and fill out the form.
- To view all records, navigate to the home page.
- To update a record, click the edit button next to the record you want to update, then modify the form and submit.
- To delete a record, click the delete button next to the record you want to remove.

## Project Structure

- `manage.py`: Command-line utility for administrative tasks.
- `your_app/`: Django app containing the CRUD operations.
  - `migrations/`: Database migrations.
  - `templates/`: HTML templates.
  - `views.py`: Logic for handling requests and returning responses.
  - `models.py`: Database models.
  - `urls.py`: URL routing.
- `static/`: Static files (CSS, JavaScript,
