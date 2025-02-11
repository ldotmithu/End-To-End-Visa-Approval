from mlproject.config.config_entity import ModelEvaluationConfig
from mlproject import logging
import pandas as pd 
import joblib
import os
import mlflow
import mlflow.sklearn
import numpy as np
from mlproject.utility.common import Read_yaml, Create_Folder, save_object
from sklearn.metrics import accuracy_score
from urllib.parse import urlparse

class ModelEvaluation:
    def __init__(self):
        self.model_evaluation = ModelEvaluationConfig()
        self.params = Read_yaml(self.model_evaluation.params_path)['model']
        
        
        Create_Folder(self.model_evaluation.root_dir)
        
       
        mlflow.set_tracking_uri("http://127.0.0.1:8080")
        mlflow.set_experiment("new_visa_approval_experiment")

    def evaluation_on_testdata(self):
        
        test_data = np.load(self.model_evaluation.test_data_path)
        X_test, y_test = test_data[:, :-1], test_data[:, -1]

       
        model = joblib.load(self.model_evaluation.model_path)

        
        with mlflow.start_run():
            predictions = model.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)

            
            mlflow.log_params(self.params)
            mlflow.log_metric("accuracy", accuracy)

            
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="RandomForestClassifier")
            else:
                mlflow.sklearn.log_model(model, "model")

        # Save accuracy locally
        save_object(accuracy, os.path.join(self.model_evaluation.root_dir, self.model_evaluation.metrics_path))
        logging.info(f"Model Accuracy: {accuracy}")
