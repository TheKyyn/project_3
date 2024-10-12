# Big Data Flask Project

## Description
This project is a Flask-based web application designed to work with a PostgreSQL database. It also integrates Prometheus for monitoring and Grafana for visualizing the metrics.

## Technologies
- **Python**: Flask for backend API
- **PostgreSQL**: For data storage
- **Docker**: For containerizing the application
- **Prometheus**: For monitoring
- **Grafana**: For visualization
- **psycopg2**: PostgreSQL adapter for Python

## Requirements
- Docker
- Docker Compose

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your_username/your_repo.git
cd your_repo
```

### 2. Set up the .env File
Create a .env file to configure environment variables like the database credentials.

```bash
POSTGRES_DB=DB_Project_3
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

### 3. Build and Run the Application with Docker Compose
To build and run the services (PostgreSQL, Flask, Prometheus, Grafana):
```bash
docker-compose up --build
```
This will:

- Start a PostgreSQL database.
- Start the Flask web application at http://localhost:5001.
- Start Prometheus at http://localhost:9090.
- Start Grafana at http://localhost:3000.

### 4. Access the Application
Flask API:

- http://localhost:5001 for the main page.
- http://localhost:5001/data to view or post data.
- http://localhost:5001/stats to view statistics.
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

### 5. Create the Database Table
Once the services are running, you will need to create the data_records table. Open a new terminal and run:
```bash
docker-compose exec db psql -U postgres -d DB_Project_3
```
Then, create the table:
```bash
CREATE TABLE data_records (
    id SERIAL PRIMARY KEY,
    data_value TEXT NOT NULL,
    category TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL
);
```

### 6. API Endpoints
POST /data: To insert new data into the ```data_records``` table. The body should contain ```data_value``` and ```category```.

Example request:
```json
{
  "data_value": "Sample Data",
  "category": "Sample Category"
}
```
- GET /data: To retrieve all data from the ```data_records``` table. You can filter data by category by passing the ```category``` query parameter.
- GET /stats: To retrieve statistics on the number of records per category.
- GET /metrics: Prometheus metrics for monitoring.

### Monitoring and Visualization
- Prometheus is used for scraping metrics from the Flask application at http://localhost:9090.
- Grafana is used for visualizing the metrics at http://localhost:3000.

## Grafana Setup
The default username and password for Grafana is admin / admin.

### Stopping the Application
To stop all services:
```bash
docker-compose down
```

### License
This project is licensed under the MIT License. See the LICENSE file for details.
