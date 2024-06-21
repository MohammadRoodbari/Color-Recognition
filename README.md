# Color-Recognition

This project utilizes the K-means clustering algorithm to detect and recognize dominant color from images. The recognized colors include Red, Green, Yellow, Blue, White, Black, and Gray. The project is implemented using FastAPI for the backend and is containerized using Docker for easy deployment.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

- **Color Detection**
- **K-means Clustering**
- **FastAPI**
- **Dockerized**

## Installation

### Prerequisites

- Python 3.8+
- Docker

### Clone the Repository

```bash
git clone https://github.com/yourusername/Color-Recognition.git
```
```bash
cd Color-Recognition
```

## Usage
To start the FastAPI server
```bash
cd app
```
```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```
### Docker Deployment
To build and run the Docker container, follow these steps:

```bash
docker build -t color-recognition
```
```bash
docker run -d -p 8000:8000 color-recognition
```

