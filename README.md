*Vulnerable Flask Todo List Application with MySQL*

This is a simple Flask application integrated with a MySQL database, featuring a Todo List management system. Users can create, view, and manage todos with this application.
Features

    Create a Todo: Add a new todo with a name, description, and due date.
    View Todos: Display a list of all todos.
    View Last Todo: Show the most recently added todo.
    Delete Todo: Remove a todo from the list.

Project Structure

graphql

my-project/
│
├── Dockerfile                # Dockerfile for Flask application
├── docker-compose.yml        # Docker Compose configuration
├── Database/
│   ├── Dockerfile            # Dockerfile for MySQL database
│   └── init.sql              # SQL script to initialize database
└── app/
    ├── Dockerfile            # Dockerfile for the Flask application
    ├── requirements.txt      # Python dependencies
    ├── app.py                # Main Flask application
    ├── templates/            # HTML templates
    │   ├── index.html
    │   ├── home.html
    │   └── last.html
    └── static/               # Static files (e.g., CSS)
        └── styles.css

Prerequisites

    Docker
    Docker Compose

Getting Started

    Clone the Repository:

    bash

git clone https://github.com/yourusername/your-repository.git
cd your-repository

Build and Start the Containers:

bash

    docker-compose up --build

    This command will build Docker images for both the Flask application and the MySQL database, and start the containers.

    Access the Application:

    Open your web browser and navigate to http://localhost:5000 to use the Flask application.

Endpoints

    Home Page: http://localhost:5000/home
    View the list of todos.

    Create Todo: http://localhost:5000/create
    Add a new todo.

    Last Todo: http://localhost:5000/last
    View the most recently added todo.

    Delete Todo: http://localhost:5000/delete/<todo_id>
    Delete a todo by its ID.

Security Notice

This application contains a security vulnerability. The objective of this project is to identify and exploit the vulnerability.

Important: This is intended for educational purposes and should not be used in a production environment.
Notes

    Database Initialization: The init.sql script initializes the MySQL database and sets up the required tables and initial data.
    Flask Configuration: The Flask application is configured to run on 0.0.0.0 to be accessible from outside the Docker container.

Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Contact

For any questions or inquiries, please contact:

    Your Name - your.email@example.com
