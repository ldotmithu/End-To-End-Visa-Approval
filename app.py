from mlproject.config.config_entity import DataValidationConfig
from mlproject import logging
from mlproject.utility.common import Create_Folder,Read_yaml
import pandas as pd 

class DataValidation:
    def __init__(self):
        self.data_validation = DataValidationConfig()
        self.schema=Read_yaml(self.data_validation.schema_path)['COLUMNS']
        print(self.schema)