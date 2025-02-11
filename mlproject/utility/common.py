from mlproject import logging
import os 

def Create_Folder(file_path):
    try:
        os.makedirs(file_path,exist_ok=True)
        logging.info(f'{file_path} Folder successfully Created')
    except Exception as e:
        raise e 
            