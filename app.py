from mlproject.utility.common import Create_Folder,Read_yaml
from mlproject.config.config_entity import ModelTrainConfig
from sklearn.ensemble import RandomForestClassifier
class ModelTrian:
    def __init__(self):
        self.model_train = ModelTrainConfig()
        self.schema = Read_yaml(self.model_train.schema_path)
        self.params = Read_yaml(self.model_train.params_path)['model']
        
        drop_columns = self.params.get('n_estimators')
        print(self.params['n_estimators'])

if __name__=="__main__":
    ob= ModelTrian()