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
    