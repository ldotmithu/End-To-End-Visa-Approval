from mlproject import logging
import os 
import yaml

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
            # Load the YAML content into a Python dictionary
            yaml_content = yaml.safe_load(f)  # Return YAML content as a dictionary
        logging.info('YAML file loaded successfully')
        return yaml_content
    except FileNotFoundError:
        logging.error('YAML file not found')
    except Exception as e:
        logging.error(f"An error occurred while loading the YAML file: {e}")
  
            