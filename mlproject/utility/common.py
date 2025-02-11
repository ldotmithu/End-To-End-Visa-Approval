from mlproject import logging
import os 
import yaml
import json

def Create_Folder(file_path):
    try:
        os.makedirs(file_path,exist_ok=True)
        logging.info(f'{file_path} Folder successfully Created')
    except Exception as e:
        raise e 
    

import yaml
import logging

def Read_yaml(file_path):
    try:
        with open(file_path, 'r') as f:
            yaml_content = yaml.safe_load(f)  
        logging.info('YAML file loaded successfully')
        return yaml_content
    except FileNotFoundError:
        logging.error('YAML file not found')
        
def save_object(obj,file_path):
    try:
        with open(file_path,'w') as f:
            json.dump(f"accuracy :{obj}",f,indent=4)
            logging.info(f'Save the accuracy on {file_path}')
    except Exception as e:
        raise e        
            
  
            