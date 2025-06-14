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
        self.trained_model_path_config = ModelTrainerConfig()


    def initiate_model_training(self,train_array , test_array ):
        try:

            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],

                 test_array[:,:-1],
                test_array[:,-1],
            )


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

            model_report: dict = evaluate_model(X_train,y_train,X_test,y_test,models)

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            print(best_model_name)

            best_model = models[best_model_name]

            save_object(filepath=self.trained_model_path_config.trained_model_path,obj=best_model)

            
            return best_model, best_model_score

        except Exception as e:
            raise CustomException(e,sys)
        
