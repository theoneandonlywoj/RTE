from keras.layers.core import Dense, Activation, Dropout, Flatten
from keras.layers.recurrent import LSTM, GRU
from keras.layers.convolutional import Convolution1D
from keras.layers.normalization import BatchNormalization
from keras.models import Sequential
from keras.optimizers import Adam, RMSprop
import time

def build_model(features, seq_len, out):
    model = Sequential()

    model.add(LSTM(100, input_shape = (seq_len, features), return_sequences = True))
    model.add(Activation("tanh"))
   
    
    model.add(Convolution1D(50, 10, border_mode='valid'))
    model.add(Activation("relu"))
    
    model.add(Flatten())
    
    model.add(Dense(units = out))
    model.add(Activation("linear"))

    start = time.time()
    adam = Adam(lr = 0.25, beta_1 = 0.9, beta_2 = 0.999, epsilon = 1e-08, decay = 0.0)

    #model.compile(loss = "mean_absolute_percentage_error", optimizer = 'RMSprop')
    model.compile(loss = "mean_absolute_percentage_error", optimizer = adam)
    print("> Compilation Time : ", time.time() - start)
    return model

