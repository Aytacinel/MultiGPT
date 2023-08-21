
# Flask Chatbot Simulator with OpenAI

## Overview

This Flask-based application simulates a chatbot environment, leveraging the power of OpenAI's GPT-3.5-turbo model. Users can interact with multiple chatbot personalities, and the application responds in real-time using the GPT-3.5-turbo model.

## Features

### 1. Multiple Chatbot Personalities

The application offers various chatbot personalities, each with a distinct behavior and response pattern:

- DeveloperGPT: Answers coding questions and provides real-world code examples.
- Helpful Assistant: Acts as a general-purpose helpful assistant.
- Python Interpreter: Executes Python code provided by the user.

### 2. Dynamic Response Generation

The chatbot dynamically generates responses based on the user's message and the selected chatbot personality.

### 3. Chat Log

The application maintains a chat log, saving the history of interactions for each chatbot personality. This allows for context-aware responses.

### 4. Modular Code Structure

The application's code is organized and modular, ensuring easy scalability and maintenance.

## Installation and Setup

### Prerequisites

Ensure you have Flask and other necessary libraries installed:
```
pip install Flask openai
```

### Running the Application

1. Clone/download the repository to your local machine.
2. Navigate to the project directory in the terminal.
3. Run the application using the command:
```
python app.py
```
4. Open your browser and navigate to the provided address (usually `http://127.0.0.1:5000/`) to interact with the chatbot.

## Contributing

Contributions are welcome! If you'd like to improve the application or add new features, please fork the repository, make your changes, and submit a pull request.

