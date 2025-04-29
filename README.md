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

- `data/`: Contains the dataset files.
- `notebooks/`: Jupyter notebooks for data exploration and model development.
- `models/`: Trained machine learning models.
- `app.py`: Flask application for deploying the model as an API.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Project documentation.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Pandas
- NumPy
- Scikit-learn

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Airfoil-Self-Noise-Regression.git
   cd Airfoil-Self-Noise-Regression


Install the required packages:
`pip install -r requirements.txt`

## Usage

### Data Exploration and Model Training

Use the Jupyter notebooks in the notebooks/ directory to explore the data and train machine learning models. We evaluated several algorithms, including Linear Regression, Decision Tree, Elastic Net, Ridge Regression, and Random Forest, to determine the best model based on accuracy scores. The Random Forest model was selected as the best-fit model due to its superior performance.

### Model Deployment

The Flask application in the `app.py` file can be used to deploy the trained model as an API. Run the application using:

`python app.py`

### API Usage

Send a POST request to the `/predict_api` endpoint with the required input features to get predictions.

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments

NASA for providing the dataset.
