from mlproject.pipeline.Pipeline_statges import DataIngestionPipeline,DataValidationPipeline
from mlproject import logging

try:
    logging.info('>>>>Data Ingestion>>>>>>')
    data_ingestion = DataIngestionPipeline()
    data_ingestion.Main()
    logging.info('--------------------------')
    
except Exception as e:
    raise e    

try:
    logging.info('>>>>Data Validation>>>>>>')
    data_validation = DataValidationPipeline()
    data_validation.Main()
    logging.info('--------------------------')
    
except Exception as e:
    raise e   