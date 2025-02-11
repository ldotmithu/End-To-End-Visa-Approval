from mlproject.components.data_ingestion import DataIngestion
from mlproject import logging
from mlproject.components.data_validation import DataValidation
from mlproject.components.data_transfomation import DataTransfomation


class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def Main(self):
        data_ingestion = DataIngestion()
        data_ingestion.Download_ZipFile()
        data_ingestion.Unzip_operation()
        
class DataValidationPipeline:
    def __init__(self):
        pass
    
    def Main(self):
        data_validation = DataValidation()
        data_validation.check_all_columns()
        
class DataTransfomationPipeline:
    def __init__(self):
        pass
    
    def Main(self):
        data_transform = DataTransfomation()
        data_transform.split_data()     
      