from mlproject.components.data_ingestion import DataIngestion
from mlproject import logging
from mlproject.components.data_validation import DataValidation


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
      