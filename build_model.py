from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.layers.convolutional import Conv1D
from keras.models import Sequential
from keras.optimizers import Adam
import time

def build_model(features, seq_len, out):
    model = Sequential()

    model.add(LSTM(100, input_shape = (seq_len, features), return_sequences=False))
    #model.add(Dropout(0.5))
    
	
    #model.add(LSTM(10,return_sequences = True))

    #model.add(LSTM(20,return_sequences = False))
    model.add(Dropout(0.5))

    model.add(Dense(units = out))
    #model.add(Activation("linear"))

    start = time.time()
    adam = Adam(lr = 0.5, beta_1 = 0.9, beta_2 = 0.999, epsilon = 1e-08, decay = 0.0)

    model.compile(loss = "mse", optimizer = adam)
    print("> Compilation Time : ", time.time() - start)
    return model

