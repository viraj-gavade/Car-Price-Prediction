import sys
import os
import logging


def error_message_details(error_message,error_deatils:sys):
    _,_,error_tab = error_deatils.exc_info()
    error_filename = error_tab.tb_frame.f_code.co_filename
    error_line = error_tab.tb_lineno
    error_message =f'Error occurred : {error_tab} \n Error File:{error_filename} \n Error Line No : {error_line}'
    return error_message

class CustomException(Exception):
    def __init__(self, error_message,error_deatils:sys):
        super().__init__(error_message)
        self.error_message =error_message_details(error_message,error_deatils)

    def __str__(self):
         return self.error_message
    


if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e :
        logging.info('Divide by zero error')
        raise CustomException(e,sys)