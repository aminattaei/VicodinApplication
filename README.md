## Installation & Setup

Follow these steps to set up the project locally on your machine:

1. **Clone the repository**  
   Clone the project repository from GitHub to your local system:

2. **Create and activate a virtual environment**  
   It is highly recommended to use a virtual environment to manage dependencies separately from your system Python:

3. **Install the required dependencies**  
   Install all the necessary Python packages using `pip` and the provided requirements file:

4. **Apply database migrations**  
   Set up the database schema and apply any migrations:

5. **Create a superuser account**  
   Create an administrative user to access the Django admin interface:

6. **Run the development server**  
   Start the Django development server to preview and test the application locally:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
python -m venv venv
# Activate the virtual environment:
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
