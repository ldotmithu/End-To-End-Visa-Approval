from mlproject.pipeline.Pipeline_statges import (DataIngestionPipeline,DataValidationPipeline,
DataTransfomationPipeline,ModelTrainPipeline,ModelEvaluationPipeline)
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

try:
    logging.info('>>>>Data Transform>>>>>>')
    data_transform = DataTransfomationPipeline()
    data_transform.Main()
    logging.info('--------------------------')
    
except Exception as e:
    raise e  

try:
    logging.info('>>>>Model Train>>>>>>')
    model_train = ModelTrainPipeline()
    model_train.Main()
    logging.info('--------------------------')
    
except Exception as e:
    raise e  

try:
    logging.info('>>>>Model Evaluation>>>>>>')
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.Main()
    logging.info('--------------------------')
    
except Exception as e:
    raise e  