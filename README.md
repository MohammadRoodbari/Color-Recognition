# Color-Recognition

Welcome to the **Color-Recognition** project! This project utilizes the K-means clustering algorithm to detect and recognize dominant color from images. The recognized colors include Red, Green, Yellow, Blue, White, Black, and Gray. The project is implemented using FastAPI for the backend and is containerized using Docker for easy deployment.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)

## Features

- **Color Detection**: Detects and identifies Red, Green, Yellow, Blue, White, Black, and Gray colors in images.
- **K-means Clustering**: Uses the K-means algorithm to cluster and identify colors.
- **FastAPI**: Provides a fast and efficient API for color recognition.
- **Dockerized**: Easily deployable with Docker.

## Technologies

- **Python**: The programming language used for developing the application.
- **K-means Clustering**: Algorithm used for color recognition.
- **FastAPI**: Web framework used for building the API.
- **Docker**: Containerization tool used for deployment.

## Installation

### Prerequisites

- Python 3.8+
- Docker

### Clone the Repository

```bash
git clone https://github.com/yourusername/Color-Recognition.git
cd Color-Recognition
```

## Usage
To start the FastAPI server
```bash
cd app
uvicorn main:app --host 0.0.0.0 --port 8080
```

### Docker Deployment
To build and run the Docker container, follow these steps:

```bash
docker build -t color-recognition
docker run -d -p 8000:8000 color-recognition
```


