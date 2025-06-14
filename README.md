# 🚗 Car Price Prediction

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
</div>

<p align="center">
  <strong>A machine learning powered web application for predicting car prices with high accuracy based on various features.</strong>
</p>

![Car Price Prediction Demo](https://via.placeholder.com/1200x400?text=Car+Price+Prediction+Application)

## ✨ Features

- **🔮 Accurate Price Prediction**: Get reliable car price estimates using gradient boosting regression
- **📊 Interactive Data Visualization**: Explore the dataset through intuitive charts and graphs
- **📱 Responsive Design**: Seamless experience across desktop, tablet, and mobile devices
- **🛠️ Modular Architecture**: Clean separation of concerns with components-based design
- **🧪 Extensive Model Evaluation**: Multiple algorithms tested to ensure optimal performance

## 🚀 Tech Stack

<div>
  <table>
    <tr>
      <th>Category</th>
      <th>Technologies</th>
    </tr>
    <tr>
      <td>Backend</td>
      <td>FastAPI, Python, scikit-learn</td>
    </tr>
    <tr>
      <td>Frontend</td>
      <td>HTML, CSS, JavaScript, Tailwind CSS</td>
    </tr>
    <tr>
      <td>Data Processing</td>
      <td>Pandas, NumPy</td>
    </tr>
    <tr>
      <td>ML Algorithms</td>
      <td>Gradient Boosting, Random Forest, XGBoost, CatBoost</td>
    </tr>
    <tr>
      <td>Visualization</td>
      <td>Chart.js, Matplotlib, Seaborn</td>
    </tr>
  </table>
</div>

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/car-price-prediction.git
   cd car-price-prediction
   ```

2. **Set up a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   uvicorn app:app --reload
   ```

5. **Access the application**
   - Open your browser and navigate to http://localhost:8000

## 🏗️ Project Architecture

```
Car Price Prediction/
├── app.py                 # Main FastAPI application
├── artifacts/             # Model artifacts and data
│   ├── model.pkl          # Trained ML model
│   ├── processor.pkl      # Data preprocessor
│   ├── raw.csv            # Raw dataset
│   ├── train.csv          # Training dataset
│   └── test.csv           # Test dataset
├── Logs/                  # Application logs
├── Notebook/              # Jupyter notebooks for model development
│   ├── GradientBoost_Regression_Algortihm.ipynb
│   ├── cardekho_imputated.csv
│   └── cars.csv           # Original dataset
└── src/                   # Source code
    ├── components/        # Model components
    │   ├── data_ingestion.py      # Data loading and splitting
    │   ├── data_transformation.py # Feature engineering and preprocessing
    │   ├── model_trainer.py       # Model training and evaluation
    │   └── pipeline/
    │       └── prediction_pipeline.py # Prediction pipeline
    └── utils/             # Utility functions
        ├── exception.py   # Custom exception handling
        ├── logger.py      # Logging configuration
        ├── model_evaluation.py # Model metrics calculation
        ├── object_fucntions.py  # Object serialization helpers
        └── visualizations.py    # Data visualization functions
```

## 🔄 Data Pipeline

1. **Data Ingestion**: Load and split data into training and testing sets
2. **Data Transformation**: Handle missing values, encode categorical variables, and scale numerical features
3. **Model Training**: Train and evaluate multiple regression algorithms 
4. **Model Selection**: Select the best performing model based on R² score
5. **Prediction**: Process new input data through the pipeline to make accurate price predictions

## 🤖 Model Details

The car price prediction model is built using **Gradient Boosting Regression** which outperformed other algorithms in our evaluation. The model was trained on the **CarDekho** dataset with the following features:

| Feature | Description |
|---------|-------------|
| Year | Year of manufacture |
| Km_driven | Total distance driven in kilometers |
| Name | Car model name |
| Fuel | Fuel type (Petrol, Diesel, CNG, etc.) |
| Seller_type | Type of seller (Individual, Dealer) |
| Transmission | Transmission type (Manual, Automatic) |
| Owner | Number of previous owners |

## 🌐 API Endpoints

- `GET /`: Home page
- `GET /prediction`: Prediction interface
- `GET /visualization`: Data visualization dashboard
- `GET /about`: About page
- `POST /api/predict`: REST API endpoint for car price prediction

## 📊 Model Performance

| Model | R² Score | MAE | RMSE |
|-------|----------|-----|------|
| Gradient Boosting | 0.92 | 0.87 | 1.21 |
| Random Forest | 0.90 | 0.92 | 1.45 |
| XGBoost | 0.89 | 0.95 | 1.52 |
| Linear Regression | 0.72 | 1.87 | 2.42 |

## 📸 Screenshots

<div align="center">
  <img src="https://via.placeholder.com/400x250?text=Home+Page" alt="Home Page" width="45%">
  <img src="https://via.placeholder.com/400x250?text=Prediction+Interface" alt="Prediction Interface" width="45%">
  <img src="https://via.placeholder.com/400x250?text=Data+Visualization" alt="Data Visualization" width="45%">
  <img src="https://via.placeholder.com/400x250?text=Results+Page" alt="Results Page" width="45%">
</div>

## 🔮 Future Enhancements

- [ ] Integrate additional data sources for more accurate predictions
- [ ] Add time-series analysis for price trend forecasting
- [ ] Implement user authentication and saved predictions
- [ ] Develop mobile application versions
- [ ] Add A/B testing framework for model improvements

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

- **Viraj** - Machine Learning Engineer

## 🙏 Acknowledgements

- [CarDekho](https://www.cardekho.com/) for the dataset
- [Krish Naik](https://github.com/krishnaik06) for guidance and mentorship
- The scikit-learn team for their incredible machine learning library
