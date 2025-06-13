import sys 
import os 
import numpy as np 
import pandas as pd
from dataclasses import dataclass
from src.utils.exception import CustomException
from src.utils.logger import logging
from src.utils.object_fucntions import save_object
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

@dataclass
class DataTransformerConfig:
    data_processor_object_file_path: str = os.path.join('artifacts', 'processor.pkl')

class DataTransformer:
    def __init__(self):
        self.data_processor_object = DataTransformerConfig()
    
    def get_data_transformer_object(self):
        try:
            numerical_features = ['year', 'km_driven']
            categorical_features = ['name', 'fuel', 'seller_type', 'transmission', 'owner']
            
            # Numerical pipeline with imputer
            numeric_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('StandardScaler', StandardScaler())
                ]
            )
            
            # Categorical pipeline with imputer and fixed OneHotEncoder
            categorical_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('OneHotEncoder', OneHotEncoder(
                        drop='first',
                        handle_unknown='ignore',  # This fixes the unknown categories error
                        sparse_output=False  # Updated parameter name for newer sklearn versions
                    ))
                ]
            )
            
            preprocessor = ColumnTransformer(
                [
                    ('numeric_pipeline', numeric_pipeline, numerical_features),
                    ('categorical_pipeline', categorical_pipeline, categorical_features)
                ],
                remainder='drop'  # Changed from 'passthrough' to 'drop' for cleaner output
            )
            
            logging.info(f"Numerical features: {numerical_features}")
            logging.info(f"Categorical features: {categorical_features}")
            
            return preprocessor
            
        except Exception as e:
            logging.error(f"Error in get_data_transformer_object: {str(e)}")
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            # Read the data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            target_column = 'selling_price'
            
            logging.info("Read train and test data completed")
            logging.info(f"Train dataframe shape: {train_df.shape}")
            logging.info(f"Test dataframe shape: {test_df.shape}")
            
            # Separate features and target
            input_feature_train_df = train_df.drop([target_column], axis=1)
            target_feature_train_df = train_df[target_column]
            
            input_feature_test_df = test_df.drop([target_column], axis=1)
            target_feature_test_df = test_df[target_column]
            
            logging.info(f"Input features columns: {input_feature_train_df.columns.tolist()}")
            logging.info(f"Target feature shape - Train: {target_feature_train_df.shape}, Test: {target_feature_test_df.shape}")
            
            # Get the preprocessor object
            preprocessor_object = self.get_data_transformer_object()
            
            logging.info("Applying preprocessing object on training dataframe")
            
            # Transform the data
            input_feature_train_array = preprocessor_object.fit_transform(input_feature_train_df)
            
            logging.info("Applying preprocessing object on testing dataframe")
            
            input_feature_test_array = preprocessor_object.transform(input_feature_test_df)
            
            # Combine features and target - FIXED the bug here
            train_array = np.c_[
                input_feature_train_array, np.array(target_feature_train_df)
            ]
            test_array = np.c_[
                input_feature_test_array, np.array(target_feature_test_df)  # Fixed: was using train array
            ]
            
            logging.info(f"Train array shape: {train_array.shape}")
            logging.info(f"Test array shape: {test_array.shape}")
            
            # Save the preprocessor object
            save_object(
                filepath=self.data_processor_object.data_processor_object_file_path,
                obj=preprocessor_object
            )
            
            logging.info("Preprocessing object saved successfully")
            
            return (
                train_array,
                test_array,
                self.data_processor_object.data_processor_object_file_path
            )
            
        except Exception as e:
            logging.error(f"Error in initiate_data_transformation: {str(e)}")
            raise CustomException(e, sys)