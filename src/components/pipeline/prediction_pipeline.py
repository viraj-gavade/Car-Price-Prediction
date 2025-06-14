from src.utils.exception import CustomException
from src.utils.object_fucntions import load_object
from src.utils.logger import logging
import os
import sys
import pandas as pd



class PredictionPipeline :
    def __init__(self):
        pass

    def predict(self , features):
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
            model_path = os.path.join(base_dir,'artifacts','model.pkl')
            preprocessor_path = os.path.join(base_dir,'artifacts','processor.pkl')  # Fixed filename to match what's in artifacts

            logging.info(f"Loading preprocessor from {preprocessor_path}")
            preprocessor_obj = load_object(preprocessor_path)
            
            logging.info(f"Loading model from {model_path}")
            model_obj = load_object(model_path)

            logging.info("Transforming features using preprocessor")
            scaled_data = preprocessor_obj.transform(features)

            logging.info("Making prediction with model")
            prediction = model_obj.predict(scaled_data)  # Fixed: using model_obj instead of preprocessor_obj

            logging.info(f"Prediction result: {prediction}")
            return prediction
        
        except Exception as e:
            raise CustomException(e, sys)



class CustomData :
    def __init__(self,name:str,year:int,selling_price:int,km_driven:int,fuel:str,seller_type:str,transmission:str,owner:str):
        self.name = name
        self.year = year
        self.selling_price=selling_price
        self.km_driven = km_driven
        self.fuel=fuel
        self.seller_type = seller_type
        self.transmission = transmission
        self.owner = owner

    

    def get_data_as_dataframe(self):
        try:
            logging.info("Creating dataframe from provided data")
            custom_data_input_dict = {
                'name':[self.name],
                'year':[self.year],
                'selling_price':[self.selling_price],
                'km_driven':[self.km_driven],
                'fuel':[self.fuel],
                'seller_type':[self.seller_type],
                'transmission':[self.transmission],
                'owner':[self.owner]
            }

            df = pd.DataFrame(custom_data_input_dict)
            logging.info(f"Created dataframe with shape: {df.shape}")
            return df
        except Exception as e:
            logging.error("Error occurred while creating dataframe")
            raise CustomException(e, sys)


