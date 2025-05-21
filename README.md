# MLOPS_LAB02

This project demonstrates how to deploy a machine learning model using Docker and Docker Compose. The setup ensures reproducibility by specifying exact versions for all dependencies.

## Prerequisites

Before running the project, ensure you have the following installed on your system:

1. **Docker**: Install Docker from [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/).
2. **Docker Compose**: Docker Compose is usually included with Docker. Verify its installation by running `docker-compose --version`.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ht-N/MLOPS_LAB02.git
   cd MLOPS_LAB02
   ```

2. **Environment Configuration**:
   - Ensure Docker is running on your machine.
   - Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
   requirements.txt:
   ```bash
    fastapi==0.103.1
    uvicorn==0.23.2
    Pillow==9.5.0
    python-multipart==0.0.20
    torch==2.2.2
    torchvision==0.17.2
    numpy==1.24.4
   ```

## Running the Project

1. **Start the Service**:
   Run the following command to start the service using Docker Compose:
   ```bash
   docker-compose up
   ```

   This will:
   - Pull the Docker image `flex1by/mlops_th02:v1.0.4` (if not already present).
   - Start the `ml-api` service and expose it on port `5000`.

2. **Verify the Service**:
   Open a web browser or use a tool like `curl` to verify the service is running:
   ```bash
   curl http://localhost:5000
   ```

   Or, go to this urL:
   ```bash
   http://localhost:5000/docs
   ```

## Stopping the Project

To stop the service, press `Ctrl+C` in the terminal where the service is running, or run:
```bash
docker-compose down
```

## Dependencies

The project relies on the following dependencies, which are encapsulated in the Docker image:

- **Docker Image**: `flex1by/mlops_th02:v1.0.4`
  - This image includes all necessary libraries and their specific versions to ensure compatibility.

## Notes

- **Version Control**: The Docker image and its dependencies are pinned to specific versions to avoid breaking changes.
- **Port Configuration**: The service is configured to run on port `5000`. Ensure this port is available on your machine.

## Troubleshooting

- If the service fails to start, check the Docker logs for errors:
  ```bash
  docker-compose logs
  ```
- Ensure Docker has sufficient resources (CPU, memory) allocated.
