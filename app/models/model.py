import joblib

class ForecastModel:
    def __init__(self, model_path: str):
        self.model = joblib.load(model_path)

    def predict(self, features: list):
        return self.model.predict(features)
