# Mini Platform

## Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mini-platform.git
   cd mini-platform
   ```

2. Build the Docker containers:
   ```bash
   docker compose build
   ```

3. Start the application:
   ```bash
   docker compose up
   ```

> ⚠️ **Note:** Stop any running PostgreSQL instance on your local machine before starting the app to avoid port conflicts.

## Access

- **Frontend:** [http://localhost:4200](http://localhost:4200)
- **Backend (API docs):** [http://localhost:8000/docs](http://localhost:8000/docs)
