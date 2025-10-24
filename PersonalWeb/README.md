# PersonalWeb Docker Setup

This directory contains a Dockerized version of the PersonalWeb Flask application.

## Prerequisites

- Docker Desktop installed on your system
- Docker Compose (usually comes with Docker Desktop)

## Files Created

- `Dockerfile` - Defines how to build the Docker image
- `docker-compose.yml` - Orchestrates the container setup
- `requirements.txt` - Python dependencies
- `.dockerignore` - Files to exclude from Docker build context
- `README.md` - This file

## How to Run

### Method 1: Using Docker Compose (Recommended)

1. Open a terminal/command prompt in the PersonalWeb directory
2. Run the following command:
   ```bash
   docker-compose up --build
   ```
3. Access the application at: http://localhost:5000

### Method 2: Using Docker directly

1. Build the image:
   ```bash
   docker build -t personalweb .
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 personalweb
   ```
3. Access the application at: http://localhost:5000

## Stopping the Application

### If using Docker Compose:
```bash
docker-compose down
```

### If using Docker directly:
```bash
docker ps  # Find the container ID
docker stop <container_id>
```

## Development Mode

To run in development mode with live reloading, you can mount the current directory as a volume:

```bash
docker run -p 5000:5000 -v "$(pwd):/app" personalweb
```

## Troubleshooting

1. **Port already in use**: Change the port mapping in `docker-compose.yml` from `5000:5000` to `8080:5000` (or any available port)
2. **Permission issues**: Make sure Docker has the necessary permissions to access the project directory
3. **Build failures**: Ensure all files are present and Docker has internet access to download dependencies

## Container Details

- **Base Image**: python:3.11-slim
- **Exposed Port**: 5000
- **Working Directory**: /app
- **User**: Non-root user (flaskuser) for security
- **Health Check**: HTTP GET to / every 30 seconds