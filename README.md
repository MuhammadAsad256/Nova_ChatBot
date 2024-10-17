# Nova ChatBot

Nova ChatBot is a Django-based web application that leverages the Cohere API to provide interactive conversational capabilities. The application is designed to respond to user queries intelligently.

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

3. Obtain a free API key from Cohere by visiting:[ Get API Key](https://dashboard.cohere.com/api-keys)
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

## Usage
- Type your message in the input box and press send.
- The Chatbot will respond based on your input and its conversation histry.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Cohere](https://coral.cohere.com/) for providing the API to power the chat responses.
- Django for the robust web framework.


   
