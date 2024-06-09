import joblib
from django.conf import settings

def load_model():
    model_path = settings.BASE_DIR/'AI_model'/'model.pkl'
    model = joblib.load(model_path)
    return model