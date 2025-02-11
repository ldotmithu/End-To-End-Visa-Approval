from mlproject.config.config_entity import DataIngestionConfig
from mlproject import logging
import zipfile,os
from urllib.request import urlretrieve
from mlproject.utility.common import Create_Folder

class DataIngestion:
    def __init__(self):
        self.data_ingestion = DataIngestionConfig()
        
        Create_Folder(self.data_ingestion.root_dir)    
        
    def Download_ZipFile(self):
        if self.data_ingestion.URL.endswith('.zip'):
            try:
                if not os.path.exists(self.data_ingestion.local_data_path):
                    urlretrieve(self.data_ingestion.URL,self.data_ingestion.local_data_path)
                    logging.info('ZipFlie Downloaded')
                else:
                    logging.info('File Already Exisit')    
            except Exception as e:
                raise e
        else:
            logging.info('File Extention is Not Valid Check the URL')
    
    def Unzip_operation(self):
        try:
            with zipfile.ZipFile(self.data_ingestion.local_data_path,'r') as f:
                f.extractall(self.data_ingestion.unzip_dir)
                logging.info('Unzip Operation Completed') 
                      
        except Exception as e:
            raise e 