from mlproject.components.data_ingestion import DataIngestion
from mlproject import logging


class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def Main(self):
        data_ingestion = DataIngestion()
        data_ingestion.Download_ZipFile()
        data_ingestion.Unzip_operation()