import os
import sys
import dill
from src.utils.exception import CustomException



def save_object(filepath,obj):
    try:  
        dir_path = os.path.dirname(filepath)

        os.makedirs(dir_path,exist_ok=True)

        with open(filepath,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
        