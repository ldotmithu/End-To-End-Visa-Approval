from mlproject.config.config_entity import ModelEvaluationConfig
from mlproject import logging
import pandas as pd 
import joblib,os
from mlproject.utility.common import *
from sklearn.metrics import accuracy_score
import numpy as np 
from imblearn.combine import SMOTEENN


class ModelEvaluation:
    def __init__(self):
        self.model_evaluation = ModelEvaluationConfig()
        
        Create_Folder(self.model_evaluation.root_dir)
    
    def evaluation_on_testdata(self):
        test_data = np.load(self.model_evaluation.test_data_path)
        
        
        X_test = test_data[:, :-1] 
        y_test = test_data[:, -1]
        
        model = joblib.load(self.model_evaluation.model_path)
        prd = model.predict(X_test)
        accuracy = accuracy_score(y_test,prd)
        save_object(accuracy,os.path.join(self.model_evaluation.root_dir,self.model_evaluation.metrics_path))
        logging.info(f"accuracy: {accuracy}")

        
        