# Nova ChatBot

Nova ChatBot is a Django-based web application that leverages the Cohere API to provide interactive conversational capabilities. The application is designed to respond to user queries intelligently.

## Project Structure

nova_chatbot/ ├── manage.py # Django's command-line utility for administrative tasks ├── db.sqlite3 # SQLite database file ├── nova_chatbot/ # Main project directory │ ├── init.py
│ ├── asgi.py
│ ├── settings.py # Project settings │ ├── urls.py # URL declarations for the project │ ├── wsgi.py
├── chat/ # Chat app directory │ ├── migrations/ # Database migrations │ │ └── init.py
│ ├── init.py
│ ├── admin.py # Admin panel configurations │ ├── apps.py
│ ├── models.py # Database models │ ├── tests.py # Test cases │ ├── views.py # View functions │ ├── templates/ # HTML templates │ │ └── chat/ │ │ └── chat.html # Main template for the chat application │ ├── static/ # Static files (CSS, images) │ │ ├── favicon.ico # Favicon for the chat application │ │ └── style.css # Custom styles for the chat application


## Features

- Interactive chat interface
- Responses powered by the Cohere API
- Simple and intuitive user interface

## Requirements

To run this project, you'll need to have Python installed along with the following packages:

- Django
- Cohere Python client (install via `pip install cohere`)

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/Nova_ChatBot.git
   cd Nova_ChatBot

2. Clone the repository:

   ```bash
   pip install django cohere

3. Obtain a free API key from Cohere by visiting:[ Get API Key](https://coral.cohere.com/)
4. In `views.py`, replace the placeholder API key with your own:
   ```python
   co = cohere.Client('YOUR_API_KEY_HERE')
5. Run the migrations:
   ```bash
   python manage.py migrate
6. Start the development server:
   ```bash
   python manage.py runserver
7. Open your browser and navigate to http://127.0.0.1:8000/ to access the chat application



   
