# Basic Flask-MySQL App

This project demonstrates a simple application using Flask to display data from a MySQL database. The application and database are containerized using Docker and orchestrated with Docker Compose.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Docker and Docker Compose are installed on your system.

## Project Structure

Here's a brief overview of the project's structure:

```plaintext
/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Dockerfile for Flask application
└── docker-compose.yml      # Docker Compose file to orchestrate the services
```

Setup and Running
Follow these steps to get your application up and running:

1. Clone the repository
```
git clone https://github.com/erdenayates/container-demo.git
```

2. Install Docker and Docker Compose
```
curl -fsSL https://get.docker.com -o get-docker.sh ; sh get-docker.sh ; apt install docker-compose -y
```

3. Build and Run with Docker Compose
This command builds the Docker images for the Flask application and the MySQL database, and then starts the containers as defined in the docker-compose.yml file.
```
docker-compose up --build
```

4. Accessing the Application
After the containers are up and running, you can access the Flask application by navigating to http://localhost:5000 in your web browser. You should see the JSON output of the data fetched from your MySQL database.

5. Stopping the Application
To stop the application and remove the containers, use the following Docker Compose command:
```
docker-compose down
```
