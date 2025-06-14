from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from src.utils.exception import CustomException
import sys


import numpy as np








def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
       
       model_report = {}

       for  i in range(len(list(models))):
           model = list(models.values())[i]

           model.fit(X_train,y_train)

           y_pred_train = model.predict(X_train)
           y_pred_test = model.predict(X_test)

           train_score = r2_score(y_train,y_pred_train)
           test_score = r2_score(y_test,y_pred_test)

           train_MSE = mean_squared_error(y_train,y_pred_train)
           test_MSE = mean_squared_error(y_test,y_pred_test)

           train_MAE = mean_absolute_error(y_train,y_pred_train)
           test_MAE = mean_absolute_error(y_test,y_pred_test)

           train_RMSE = np.sqrt(train_MSE)
           test_RMSE =  np.sqrt(test_MSE)
           
           model_report[list(models.keys())[i]] = {
                "train_r2": train_score,
                "test_r2": test_score,
                "train_mse": train_MSE,
                "test_mse": test_MSE,
                "train_mae": train_MAE,
                "test_mae": test_MAE,
                "train_rmse": train_RMSE,
                "test_rmse": test_RMSE
            }
           
           return model_report
           
    except Exception as e:
        raise CustomException(e,sys)
