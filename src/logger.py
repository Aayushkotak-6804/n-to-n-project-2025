## logger is for the purpose that where any excution happens ;
## u should logg all the information in some of the files :
 ## so here we can track it : 
## if any exception occurs we wiill convert this into the text file over here : 


import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  ## this is basically a text file in this naming config it will be get created : 
logs_path = os.path.join(os.getcwd(),"logs","LOG_FILE")
os.makedirs(logs_path,exist_ok=True)


LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)



#if __name__ == 'main':
#    logging.info("Logginf has started : ")



## getcwd == get correct working library : 
## every log folder will be cretad over here and the 
## and every file name start with the log and the file name of the log as well : 
## Even though there is the folder/file keep on appending the logs folder over here : 



## Now the whole procedure : 
## 1. and now i will find the new exception :
## 2. i will take that exception :
## 3. logging witht the logger file : 
## 4. and will used the loggedin.info to put the file into the it : 