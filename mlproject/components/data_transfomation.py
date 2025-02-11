from mlproject.config.config_entity import DataTransfomationConfig
from sklearn.model_selection import train_test_split
import pandas as pd 
from mlproject import logging 
from mlproject.utility.common import *
import os 


class DataTransfomation:
    def __init__(self):
        self.data_transfomation = DataTransfomationConfig()
        Create_Folder(self.data_transfomation.root_dir)
        
    def split_data(self):
        try:
            with open(self.data_transfomation.status_file,'r') as f:
                status = f.read().split(":")[-1].strip()
                
                if status == "True" :  
                    data = pd.read_csv(self.data_transfomation.data_dir_path)
            
                    train_data,test_data = train_test_split(data,test_size=0.2,random_state=12)   
            
                    train_data.to_csv(os.path.join(self.data_transfomation.root_dir,'train.csv'),index=False)
                    test_data.to_csv(os.path.join(self.data_transfomation.root_dir,'test.csv'),index = False)
            
                    logging.info('Load the data and split the data 80 and 20 for train test')
                else:
                    raise Exception('columns not valid')
        except Exception as e:
            raise e    
        
    
            