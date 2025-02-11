from mlproject.config.config_entity import DataValidationConfig
from mlproject import logging
from mlproject.utility.common import Create_Folder,Read_yaml
import pandas as pd 


class DataValidation:
    def __init__(self):
        self.data_validation = DataValidationConfig()
        self.schema = Read_yaml(self.data_validation.schema_path)['COLUMNS']
        Create_Folder(self.data_validation.root_dir)
        
    def check_all_columns(self):
        try:
            validation_status = True  
            data = pd.read_csv(self.data_validation.unzip_dir_path)
            all_columns = list(data.columns)
            required_columns = self.schema.keys()

           
            missing_columns = [col for col in required_columns if col not in all_columns]
            if missing_columns:
                validation_status = False  
                logging.error(f"Missing columns: {missing_columns}")
            
            
            with open(self.data_validation.status_file, 'w') as f:
                f.write(f"Validation Status: {validation_status}\n")
                if not validation_status:
                    f.write(f"Missing Columns: {missing_columns}\n")
            
            logging.info(f"Validation result: {validation_status}")        
            
            return validation_status
            
        except Exception as e:
            logging.error(f"An error occurred during column validation: {e}")
            raise e