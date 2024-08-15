# Forecast Sale Model API

This project provides a REST API for serving a machine learning model that forecasts sales based on input features. The API is built using FastAPI and is containerized with Docker for easy deployment.

## Project Structure

- **`app/`**: Contains the core application logic.
  - `main.py`: Entry point for the FastAPI application.
  - `models/`: Contains the model loading and prediction logic.
  - `api/`: Defines API endpoints.
  - `utils/`: Utility functions for preprocessing data.

- **`data/`**: Contains training and test datasets.
- **`notebooks/`**: Jupyter notebooks for model training and analysis.
- **`tests/`**: Unit tests for the application.
- **`Dockerfile`**: Docker configuration for containerizing the application.
- **`requirements.txt`**: Lists Python dependencies.
- **`README.md`**: Project documentation.

## Setup and Installation

To set up the project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone <repository-url>
cd forecast-model-api

```
### 2. Download and Prepare Data

  1. Download the dataset from [Kaggle Demand Forecasting Competition](https://www.kaggle.com/c/demand-forecasting-kernels-only/data).
  2. Unzip the downloaded dataset folder.
  3. Place all the files (e.g., `train.csv`, `test.csv`) into a directory named `data` located in the root directory of your project.


### 3. Install Dependencies
You can install dependencies using Docker or manually:

  **Option 1: Using Docker (Recommended)**

  1. Build the Docker Image:
  ```bash
  docker build -t forecast-model-api .
  ```

  2. Run the Docker Container:
  ```bash
  docker run -p 8000:8000 forecast-model-api
  ```

  The API will be accessible at http://localhost:8000.

  **Option 2: Manual Installation**

  1. Create a Virtual Environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  #On Windows use `venv\Scripts\activate`
  ```

  2. Install Dependencies:
  ```bash
  pip install -r requirements.txt
  ```

  3. Run the Application:
  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8000
  ```

  The API will be accessible at http://localhost:8000.


### 4. API Endpoints

- **`POST /predict`:** Predicts the number of items sold based on the input features.

**Request Body:**
```json
{
  "date": "2013-01-01",
  "store": 1,
  "item": 1
}
```

**Response:**
```json
{
  "sales": <predicted_value>
}
```

- **`GET /status`:** Returns the status of the API.

**Response:**
```json
{
  "status": "API is running"
}
```

### 5. Testing
To run the tests for the application, use:
```bash
pytest
```

Make sure you have pytest installed, which can be done via `pip install pytest`, and create empty `conftest.py` in project root directory. 