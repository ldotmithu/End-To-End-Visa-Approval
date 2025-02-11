from mlproject.pipeline.Pipeline_statges import DataIngestionPipeline
from mlproject import logging

try:
    logging.info('>>>>Data Ingestion>>>>>>')
    data_ingestion = DataIngestionPipeline()
    data_ingestion.Main()
    logging.info('--------------------------')
    
except Exception as e:
    raise e    