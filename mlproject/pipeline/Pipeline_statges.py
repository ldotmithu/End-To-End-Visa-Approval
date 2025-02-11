from mlproject.components.data_ingestion import DataIngestion
from mlproject import logging
from mlproject.components.data_validation import DataValidation
from mlproject.components.data_transfomation import DataTransfomation
from mlproject.components.model_train import ModelTrain
from mlproject.components.model_evaluation import ModelEvaluation

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
        data_transform.apply_perprocess()  

class ModelTrainPipeline:
    def __init__(self):
        pass
    
    def Main(self):
        model_train = ModelTrain()
        model_train.apply_preprocess()            
      
class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def Main(self):
        model_evaluation = ModelEvaluation()
        model_evaluation.evaluation_on_testdata()            