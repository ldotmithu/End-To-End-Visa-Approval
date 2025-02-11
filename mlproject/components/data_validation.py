from mlproject.config.config_entity import DataValidationConfig
from mlproject import logging
from mlproject.utility.common import Create_Folder,Read_yaml
import pandas as pd 
from sklearn.model_selection import train_test_split


class DataValidation:
    def __init__(self):
        self.data_validation = DataValidationConfig()
        self.schema = Read_yaml(self.data_validation.schema_path)['COLUMNS']
        Create_Folder(self.data_validation.root_dir)
        
    def check_all_columns(self):
        try:
            #validation_status = True  
            data = pd.read_csv(self.data_validation.unzip_dir_path)
            all_columns = list(data.columns)
            required_columns = self.schema.keys()
            
            miss_col = [col for col in required_columns if col not in all_columns]
            
            if miss_col:
                validation_status = False
                logging.info(f'Validation Status : {validation_status}')
                logging.error(f'missing columns :{miss_col}')
                with open (self.data_validation.status_file,'w') as f:
                    f.write(f'Validation Status : {validation_status}')
            else:
                validation_status = True
                logging.info(f'Validation Status : {validation_status}')
                with open (self.data_validation.status_file,'w') as f:
                    f.write(f'Validation Status : {validation_status}')      
                
                 
            return validation_status        
        except Exception as e:
            raise e             
                    
                    

if __name__=="__main__":
    valid = DataValidation()
    valid.check_all_columns()        