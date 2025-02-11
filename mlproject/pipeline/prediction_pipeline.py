import joblib
import numpy as np 
import pandas as pd 
from pathlib import Path

class prediction_pipeline:
    def __init__(self):
        self.model = joblib.load(Path("atrifacts\model_train\model.pkl"))
        
    def prediction(self,data):
        prediction = self.model.predict(data)
        return prediction