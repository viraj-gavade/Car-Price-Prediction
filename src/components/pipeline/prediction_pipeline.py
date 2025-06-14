
from src.utils.exception import CustomException
from src.utils.object_fucntions import load_object
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
            preprocessor_path = os.path.join(base_dir,'artifacts','preprocessor.pkl')

            preprocessor_obj = load_object(preprocessor_path)

            model_obj = load_object(model_path)

            scaled_data = preprocessor_obj.transform(features)

            prediction = preprocessor_obj.predict(scaled_data)



            return prediction
        
        except Exception as e:
            raise CustomException



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
            custom_data_input_dict = {
                'name':[self.name],
                'year':[self.year],
                'selling_price':[self.selling_price],
                'km_driven':[self.km_driven],
                'fuel':[self.fuel],
                'seller_type':[self.seller_type],
                'owner':[self.owner]

            }

            df = pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException
        

        