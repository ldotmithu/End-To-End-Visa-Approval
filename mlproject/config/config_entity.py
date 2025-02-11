from dataclasses import dataclass
from pathlib import Path
import os 

@dataclass
class DataIngestionConfig:
    root_dir:Path = 'atrifacts/data_ingestion'
    URL:str = "https://github.com/ldotmithu/Dataset/raw/refs/heads/main/Visadataset.zip"
    local_data_path:Path="atrifacts/data_ingestion/data.zip"
    unzip_dir:Path= 'atrifacts/data_ingestion'
    