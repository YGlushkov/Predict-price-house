import pickle
from celery import Celery


celery_app = Celery('tasks', backend='redis://redis', broker='redis://redis')
model = pickle.load(open('model.pkl', 'rb'))

@celery_app.task(name='tasks.predict')
def predict(data):
    # Run the model and make a prediction for each house in the homes_to_value array
    predicted_home_values = model.predict(data)
    return predicted_home_values[0]