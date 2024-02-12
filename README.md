# Multi-Language Web App Stack with MySQL Database

This project demonstrates a multi-language application stack using Flask (Python), Express (Node.js), and PHP to display data from a MySQL database. The applications and database are containerized using Docker and orchestrated with Docker Compose.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Docker and Docker Compose are installed on your system.

## Project Structure

Here's a brief overview of the project's structure:

```plaintext
/
├── flask/                  # Flask application directory
│   ├── app.py              # Flask application to display MySQL data
│   ├── requirements.txt    # Python dependencies for Flask
│   └── Dockerfile          # Dockerfile for Flask application
├── node/                   # Node.js application directory
│   ├── index.js            # Node.js application to display MySQL data
│   ├── package.json        # Node.js dependencies
│   └── Dockerfile          # Dockerfile for Node.js application
├── php/                    # PHP application directory
│   └── index.php           # PHP script to display MySQL data
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
Accessing the Applications
After the containers are up and running, you can access the applications by navigating to their respective ports in your web browser:  
Flask application: http://localhost:5000  
Node.js application: http://localhost:3000  
PHP application: http://localhost:8000  

5. Stopping the Application
To stop the application and remove the containers, use the following Docker Compose command:
```
docker-compose down
```
