from mlproject.config.config_entity import DataTransfomationConfig
from sklearn.model_selection import train_test_split
import pandas as pd
from mlproject import logging
from mlproject.utility.common import *
import os
from imblearn.combine import SMOTEENN
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
import joblib
import numpy as np 

class DataTransfomation:
    def __init__(self):
        self.data_transfomation = DataTransfomationConfig()
        Create_Folder(self.data_transfomation.root_dir)
        self.schema = Read_yaml(self.data_transfomation.schema_path)
        self.params = Read_yaml(self.data_transfomation.params_path)['model']

    def preprocess(self):
        or_columns = ['has_job_experience', 'full_time_position', 'education_of_employee']
        oh_columns = ['continent', 'region_of_employment', "unit_of_wage"]
        num_features = ['prevailing_wage']

        
        numeric_transformer = StandardScaler()
        oh_transformer = OneHotEncoder(dtype=float)
        ordinal_encoder = OrdinalEncoder(dtype=float)

        preprocessor = ColumnTransformer(
            [
                ("OneHotEncoder", oh_transformer, oh_columns),
                ("Ordinal_Encoder", ordinal_encoder, or_columns),
                ("StandardScaler", numeric_transformer, num_features)
            ]
        )
        return preprocessor
    
    def apply_perprocess(self):
        try:
            with open(self.data_transfomation.status_file, 'r') as f:
                status = f.read().split(":")[-1].strip()
                
                if status == "True":
                    data = pd.read_csv(self.data_transfomation.data_dir_path)
                    
                    drop_columns = self.schema.get('drop_columns', [])

                    if isinstance(drop_columns, str):
                        drop_columns = drop_columns.split()
                    target_col = self.schema.get('TARGET_COLUMN')    
                        

                    data.drop(columns=drop_columns, axis=1, inplace=True)
                    X = data.drop(columns=[target_col], axis=1)
                    y = data[target_col]
                    
                    
                    y = y.map({'Certified': 0, 'Denied': 1})  
                    
                    
                    preprocess = self.preprocess()
                    X = preprocess.fit_transform(X)
                    
                    smt = SMOTEENN(random_state=42, sampling_strategy='auto')
                    X, y = smt.fit_resample(X, y)
                    
                    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=12)
                    
                    train_arr =np.c_[X_train,np.array(y_train)]
                    test_arr=np.c_[X_test,np.array(y_test)]
                    
                    np.save(os.path.join(self.data_transfomation.root_dir, 'train.npy'), train_arr)
                    np.save(os.path.join(self.data_transfomation.root_dir, 'test.npy'), test_arr)
                    
                    preprocess_path = os.path.join(self.data_transfomation.root_dir, self.data_transfomation.preprocess_name)
                    joblib.dump(preprocess, preprocess_path)
                    logging.info('Preprocess saved successfully')
                    
                    logging.info('Data loaded and split into 80% train and 20% test successfully.')
                else:
                    raise Exception('Columns not valid or status not True.')

        except Exception as e:
            logging.error(f"Error occurred during data transformation: {e}")
            raise e
