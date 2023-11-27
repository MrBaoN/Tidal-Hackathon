import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from tkinter import filedialog as fd
import pandas as pd
import statistics as st

# Load the model (replace 'predict.h5' with the actual path to your model)
model = tf.keras.models.load_model('predict.h5')

def main(k):
    data = pd.read_csv(k)
    data['Do you like your professor?'] = data['Do you like your professor?'].astype('int')
    x = pd.get_dummies(data.drop(['Do you like your professor?'], axis=1))
    y = data['Do you like your professor?']
    p = np.mean(predict)
    if p > 0.5:
        True
    else:
        False

main()

