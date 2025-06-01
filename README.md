# Airfoil Self-Noise Regression

This project involves the analysis and prediction of airfoil self-noise using a dataset provided by NASA. The dataset was obtained from a series of aerodynamic and acoustic tests of two and three-dimensional airfoil blade sections conducted in an anechoic wind tunnel.

## Dataset Information

- **Source**: NASA
- **Number of Instances**: 1503
- **Number of Features**: 5
- **Feature Type**: Real
- **Subject Area**: Physics and Chemistry
- **Associated Tasks**: Regression
- **Missing Values**: No

The dataset comprises different size NACA 0012 airfoils at various wind tunnel speeds and angles of attack. The span of the airfoil and the observer position were the same in all of the experiments.

## Project Structure

- `.github/workflows/`: Contains GitHub Actions CI/CD workflows.
- `data/`: Contains the dataset files.
- `models/`: Trained machine learning models.
- `notebooks/`: Jupyter notebooks for data exploration and model development.
- `templates/`: HTML templates for Flask UI.
- `.dockerignore`: Files/folders ignored in Docker builds.
- `.gitignore`: Files/folders ignored by Git.
- `app.py`: Flask app for serving the model via API.
- `Dockerfile`: Used to containerize the app.
- `README.md`: Project documentation.
- `requirements.txt`: List of Python dependencies.

## Prerequisites

- Python 3.x
- Flask
- Pandas
- NumPy
- Scikit-learn

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Airfoil-Self-Noise-Regression.git
   cd Airfoil-Self-Noise-Regression
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server using:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Fill in the input fields and click "Predict" to see the prediction.

## Model Performance

Use the Jupyter notebooks in the notebooks/ directory to explore the data and train machine learning models. We evaluated several algorithms, including Linear Regression, Decision Tree, Elastic Net, Ridge Regression, and Random Forest, to determine the best model based on accuracy scores. The Random Forest model was selected as the best-fit model due to its superior performance.

## API Usage

Send a POST request to the `/predict_api` endpoint with the required input features to get predictions.

### Input Features

The model expects the following 5 input features:

1. **Frequency** *(Hz)*
2. **Angle of attack** *(degrees)*
3. **Chord length** *(meters)*
4. **Free-stream velocity** *(m/s)*
5. **Suction side displacement thickness** *(meters)*

### Example: API Request

Send a POST request to `http://127.0.0.1:5000/predict_api` with this JSON payload:
```json
{
  "data": {
    "Frequency": 1250,
    "Angle of attack": 0,
    "Chord length": 0.3048,
    "Free-stream velocity": 71.3,
    "Suction side displacement thickness": 0.00266337
  }
}
```
## Run with Docker

To build and run the app in Docker:

```bash
docker build -t airfoil-noise-app .
docker run -p 5000:5000 airfoil-noise-app
```

## Deployment

This project is containerized using Docker for easy deployment and scalability.
- **Dockerized App**: The application is packaged with a Dockerfile, ready to run in any container environment.
- **CI/CD Pipeline**: The GitHub repository is integrated with a CI/CD pipeline that automates testing, building, and deploying the application whenever code is pushed.
- **Render**: The app is deployed live on Render, enabling easy sharing and real-time use of the application.

### 🔗 Live App

You can try the live version here: [airfoil-app.onrender.com](https://airfoil-self-noise-regression.onrender.com/)

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments

NASA for providing the dataset.
