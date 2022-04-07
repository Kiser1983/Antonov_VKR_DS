import numpy as np
import tensorflow as tf
from tensorflow import keras

#

df = pd.read_csv('Datasets/X_clear.csv', encoding = 'cp1251' )
#model = keras.models.load_model('Models/model11.h5')


def get_model(X_test):
    model = keras.models.load_model('Models/model11.h5')
    prediction = model.predict(X_test)[0]
    return prediction
