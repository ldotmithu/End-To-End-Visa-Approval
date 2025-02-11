from mlproject.config.config_entity import ModelTrainConfig
from mlproject import logging
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from imblearn.combine import SMOTEENN
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from mlproject.utility.common import Create_Folder, Read_yaml
import os, joblib, pickle
from xgboost import XGBClassifier
import numpy as np 

class ModelTrain:
    def __init__(self):
        self.model_train = ModelTrainConfig()
        self.schema = Read_yaml(self.model_train.schema_path)
        self.params = Read_yaml(self.model_train.params_path)['model']
        Create_Folder(self.model_train.root_dir)


    def apply_preprocess(self):
        try:
            train_data = np.load(self.model_train.train_data_path)
            
            X_train = train_data[:, :-1] 
            y_train = train_data[:, -1] 
            
            #target_col = self.schema['TARGET_COLUMN']
            #train_X = train_data.drop(columns=[target_col], axis=1)
            #train_y = train_data[target_col]
            #y_train= np.where(y_train =='Denied', 1,0)

            n_estimators = self.params['n_estimators']
            max_features = self.params['max_features']
            

            rf = RandomForestClassifier(
                n_estimators=n_estimators,
                max_features=max_features,
                max_depth=None,
                min_samples_leaf=2,
                min_samples_split=5,
                random_state=42
            )
            #rf = KNeighborsClassifier(weights= 'distance', n_neighbors= 4, algorithm= 'auto')
            rf.fit(X_train, y_train)
            


            model_path = os.path.join(self.model_train.root_dir, self.model_train.model_name)
            

            joblib.dump(rf, model_path)
            logging.info('Train Model saved successfully')

            #joblib.dump(preprocess_obj, preprocess_path)
            logging.info('Preprocess saved successfully')
            logging.info(rf.score(X_train,y_train))

        except Exception as e:
            logging.error(f"Error occurred during model training: {e}")
            raise e