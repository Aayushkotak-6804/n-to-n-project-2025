### here we going to write our own custom exception : 
### if there is any exceptioon is there it will auto store in the variable sys :
import sys 
import logging

## wheenever there is any exception get raised i want to push into the 
## my own custom message 
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() ## on which line/file the exception has occur
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occur in the Python script name [{0}] line number [{1}] error meassage[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message
        
    

## so whenever probably my error raises i will call this fxn as follows : 

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
if __name__ == 'main':
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)
   




## so here first of all when i raise the custom exception : 
## fisrt of all it will inheriting the custom exception :
## what ever the particular error message will come will come over here : 
