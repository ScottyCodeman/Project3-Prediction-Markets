# Streamlit Chat App with MongoDB

This project is a simple chat application built with Streamlit and MongoDB. Users can register, log in, and chat with each other. Admin users can clear the chat. The chat messages are stored in a MongoDB database and are automatically refreshed every 5 seconds.

## Prerequisites

Before running the app, make sure you have the following prerequisites installed:

- Python (3.7 or higher)
- [Streamlit](https://streamlit.io/)
- [PyMongo](https://pymongo.readthedocs.io/)
- [Passlib](https://passlib.readthedocs.io/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- A running MongoDB server

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/streamlit-chat-app.git

## Usage

1. Open the app in your web browser by navigating to the provided URL.

2. Register a new user by selecting "Register" and providing a username and password.

3. Log in with your newly registered user or an existing user by selecting "Login."

4. Chat with other users by entering messages in the chat input box and clicking "Send."

5. Admin users can clear the chat by clicking the "Clear Chat" button.

## Implementation Details
* User registration and authentication are handled through MongoDB. User passwords are securely hashed using the Passlib library.
* Chat messages are stored in a MongoDB collection and are periodically refreshed every 5 seconds, ensuring that all logged-in users see the same chat messages.
* Admin users have the ability to clear the chat, which removes all chat messages from the MongoDB collection.
