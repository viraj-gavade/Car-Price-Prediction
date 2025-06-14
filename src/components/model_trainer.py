import sys
from src.utils.exception import CustomException
from src.utils.logger import logging
from dataclasses import dataclass
import os

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor



from src.utils.model_evaluation import evaluate_model
from src.utils.object_fucntions import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_path : str = os.path.join('artifacts','model.pkl')


class ModelTrainer:
    def __init__(self):
        logging.info('Trained model path configured')
        self.trained_model_path_config = ModelTrainerConfig()


    def initiate_model_training(self,train_array , test_array ):
        try:

            logging.info('Initiating the model training pipeline')
            logging.info('Splitting the data into train and test')
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],

                 test_array[:,:-1],
                test_array[:,-1],
            )

            logging.info('Data split completed')


            logging.info('Defining the models grid for training')
            models = {
                'RandomForestRegressor':RandomForestRegressor(),
                'Decision Tree':DecisionTreeRegressor(),
                'Gradient Boosting': GradientBoostingRegressor(),
                'Linear Regression': LinearRegression(),
                'K-Neighbour Regressor': KNeighborsRegressor(),
                'XGBRegressor':XGBRegressor(),
                'CatBoosting Regressor': CatBoostRegressor(),
                'AdaBoost Regressor': AdaBoostRegressor(),
            }

            logging.info('Grid models selected successfully!')
            logging.info(f'Total models to evaluate: {len(models)}')

            logging.info('Starting the model evaluation process')
            model_report: dict = evaluate_model(X_train,y_train,X_test,y_test,models)


            logging.info('Model evaluation process completed')
            logging.info(f'Model performance report: {model_report}')

            best_model_score = max(sorted(model_report.values()))
            logging.info(f'Best model score found: {best_model_score}')


            best_model_name = list(model_report.keys())[
            
                list(model_report.values()).index(best_model_score)
            ]
            
            logging.info(f'Best performing model: {best_model_name}')
            best_model = models[best_model_name]

            logging.info(f'Saving the best model to {self.trained_model_path_config.trained_model_path}')
            save_object(filepath=self.trained_model_path_config.trained_model_path,obj=best_model)
            logging.info(f'Best model saved successfully')

            return best_model, best_model_score

        except Exception as e:
            raise CustomException(e,sys)

