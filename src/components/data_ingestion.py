import sys
import os
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

# Now import local modules
from src.components.data_transformation import DataTransformer,DataTransformerConfig
from src.utils.logger import logging
from src.utils.exception import CustomException


@dataclass
class DataIngestionConfig:
    train_data_path : str  = os.path.join('artifacts','train.csv')
    test_data_path : str = os.path.join('artifacts','test.csv')
    raw_data_path : str = os.path.join('artifacts','raw.csv')



class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    
    def initiate_data_ingestion(self):
        try:
            logging.info('Initiating the data ingestion process')
            logging.info('Reading the data from the source')

            df = pd.read_csv('Notebook/cars.csv')
            logging.info('Data read successfully!')


            logging.info('Making the directories')
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            logging.info('Directories made successfully')


            logging.info('Applying the train test split')
            train_data , test_data = train_test_split(df,test_size=0.2,random_state=42)
            logging.info('Train test split applied successfully!')

            logging.info('Saving the train , test and raw data in respective files')
            train_data.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)
            df.to_csv(self.data_ingestion_config.raw_data_path)
            logging.info('Data saved successfully in the respective files')

            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )

        except Exception as e :
            print(e)
            logging.info(f'Exception Occurred : {e}')
            raise CustomException(e,sys)


if __name__ == "__main__":
    ingestion_obj = DataIngestion()
    train_data  ,test_data  = ingestion_obj.initiate_data_ingestion()
    data_transformation = DataTransformer()
    train_array,test_array,_= data_transformation.initiate_data_transformation(train_data,test_data)