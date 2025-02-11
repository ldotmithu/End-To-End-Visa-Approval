from dataclasses import dataclass
from pathlib import Path
import os 

@dataclass
class DataIngestionConfig:
    root_dir:Path = 'atrifacts/data_ingestion'
    URL:str = "https://github.com/ldotmithu/Dataset/raw/refs/heads/main/Visadataset.zip"
    local_data_path:Path="atrifacts/data_ingestion/data.zip"
    unzip_dir:Path= 'atrifacts/data_ingestion'
    
@dataclass
class DataValidationConfig:
    root_dir: Path = 'atrifacts/data_validation'
    unzip_dir_path: Path = "atrifacts/data_ingestion/Visadataset.csv"
    status_file: Path = 'atrifacts/data_validation/status.txt'
    schema_path: dict = 'schema.yaml'
    
@dataclass
class DataTransfomationConfig:
    root_dir:Path = 'atrifacts/data_transfomation'
    data_dir_path: Path = "atrifacts/data_ingestion/Visadataset.csv"
    status_file: Path = 'atrifacts/data_validation/status.txt'
    preprocess_name :str="preprocess.pkl"
    schema_path: dict = 'schema.yaml'
    params_path : dict = "params.yaml"
    
@dataclass
class ModelTrainConfig:
    root_dir:Path = 'atrifacts/model_train'
    train_data_path:Path = "atrifacts/data_transfomation/train.npy"
    model_name :str ="model.pkl"
    schema_path: dict = 'schema.yaml'
    params_path : dict = "params.yaml"
    
@dataclass
class ModelEvaluationConfig:
    root_dir:Path = 'atrifacts/data_evaluation'
    test_data_path:Path = "atrifacts\data_transfomation/test.npy"
    model_path:Path = "atrifacts\model_train\model.pkl"    
    preprocess_path:Path ="atrifacts\data_transfomation\preprocess.pkl"
    metrics_path:str = "metrics.json"
    schema_path: dict = 'schema.yaml'
    
    
    
    
    