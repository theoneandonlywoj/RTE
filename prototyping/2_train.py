
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import keras


# In[ ]:


data_x = pd.read_csv('./data/weather/v3/2013/merged/merged_2013_h0.csv', index_col = 'Time')
x = data_x[data_x.columns[0:2]]
data_y = pd.read_csv('./data/energy/v5/2013/Consumption_2013.csv', index_col = 'Time')
data = x.copy()
data['cons'] = data_y['Auvergne-Rhone-Alpes']


data = data.values
data = np.delete(data, (0), axis=0)


# In[ ]:

'''
from sklearn.preprocessing import scale

data = scale( data, axis=0, with_mean=True, with_std=False, copy=True )
data
'''

# In[ ]:


x_data = data[:, 0:2]
y_data = data[:, 2]
x_data.shape


# In[ ]:


import tensorflow as tf


# In[ ]:


#x_data = np.reshape(x_data, (x_data.shape[0], 1, x_data.shape[1]))
#x_data = np.reshape(x_data, (x_data.shape[0], x_data.shape[1], 1))


seq_len = 1000
def load_data(data, n_prev = seq_len):  

    docX, docY = [], []
    for i in range(len(data)-n_prev):
        docX.append(data[i:i+n_prev, 0:2])
        docY.append(data[i+n_prev, 2])
    alsX = np.array(docX)
    alsY = np.array(docY)

    return alsX, alsY

x_data, y_data = load_data(data)


# In[ ]:


print(x_data.shape)
print(y_data.shape)


# In[ ]:





# In[ ]:


from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.layers.convolutional import Conv1D
from keras.models import Sequential
import time

def build_model(features, seq_len, out):
    model = Sequential()

    model.add(LSTM(100, input_shape = (seq_len, features), return_sequences=False))
    #model.add(Dropout(0.5))
    
	
    #model.add(LSTM(10,return_sequences = True))

    #model.add(LSTM(20,return_sequences = False))
    #model.add(Dropout(0.2))

    model.add(Dense(units = out))
    #model.add(Activation("linear"))

    start = time.time()
    adam = keras.optimizers.Adam(lr = 0.5, beta_1 = 0.9, beta_2 = 0.999, epsilon = 1e-08, decay = 0.0)

    model.compile(loss = "mse", optimizer = adam)
    print("> Compilation Time : ", time.time() - start)
    return model


# In[ ]:


model = build_model(features = 2, seq_len = seq_len, out = 1)
model.summary()


# In[ ]:


tbCallBack = keras.callbacks.TensorBoard(log_dir ='./logs/', 
                                         histogram_freq = 0, 
                                         write_graph = True)
filepath = "best_model.hdf5"
best_model = keras.callbacks.ModelCheckpoint(filepath = filepath, 
                                             monitor = 'val_loss', 
                                             verbose = 1, 
                                             save_best_only = True, 
                                             save_weights_only = False, 
                                             mode = 'auto', period = 1)

reduce_lr = keras.callbacks.ReduceLROnPlateau(monitor = 'val_loss', factor = 0.5, patience = 2)
# In[ ]:


model.fit(
    x_data,
    y_data,
    batch_size = 100,
    epochs = 800,
    validation_split = 0.05,
    callbacks = [best_model, tbCallBack, reduce_lr])


# In[ ]:





# In[ ]:




