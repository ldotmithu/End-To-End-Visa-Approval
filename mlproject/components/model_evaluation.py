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
        self.params = Read_yaml(self.model_train.params_path)['model']
        
        Create_Folder(self.model_evaluation.root_dir)
    
    def evaluation_on_testdata(self):
        test_data = np.load(self.model_evaluation.test_data_path)
        
        
        X_test = test_data[:, :-1] 
        y_test = test_data[:, -1]
        mlflow.set_registry_uri(self.model_evaluation.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        
        model = joblib.load(self.model_evaluation.model_path)
        with mlflow.start_run():
            prd = model.predict(X_test)
            accuracy = accuracy_score(y_test,prd)
            mlflow.log_params(self.self.params)
            mlflow.log_metric("accuracy", accuracy)
            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="RandomForestClassifier")
            else:
                mlflow.sklearn.log_model(model, "model")

        save_object(accuracy,os.path.join(self.model_evaluation.root_dir,self.model_evaluation.metrics_path))
        logging.info(f"accuracy: {accuracy}")

        
        