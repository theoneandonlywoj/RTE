
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import keras
from build_model import build_model

data_x = pd.read_csv('./data/weather/v3/2013/merged/merged_2013_h0.csv', index_col = 'Time')
data_x.columns


# In[ ]:


x = data_x[['temperature-460', 'cloudiness-460',
            'temperature-481', 'cloudiness-481',
            'temperature-645', 'cloudiness-645',]]


# In[ ]:


data_y = pd.read_csv('./data/energy/v5/2013/Consumption_2013.csv', index_col = 'Time')
data = x.copy()
data['cons'] = data_y['Auvergne-Rhone-Alpes']
data.head()


# In[ ]:


data.drop(data.index[0], inplace = True)


# In[ ]:


data.head()


# In[ ]:


data.isnull().values.any()


# In[ ]:


data.isnull().sum()


# In[ ]:


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
data = scaler.fit_transform(data)


# In[ ]:


data = pd.DataFrame(data)
data.head()


# In[ ]:


data = data.values

'''
from sklearn.preprocessing import scale

data = scale( data, axis=0, with_mean=True, with_std=False, copy=True )
data.head()
'''

x_data = data[:, 0:6]
y_data = data[:, 6]
x_data.shape


import tensorflow as tf


# In[ ]:


seq_len = 1000
def data_to_sequence(data, n_prev = seq_len):  

    docX, docY = [], []
    for i in range(len(data)-n_prev):
        docX.append(data[i:i+n_prev, 0:6])
        docY.append(data[i+n_prev, 6])
    alsX = np.array(docX)
    alsY = np.array(docY)

    return alsX, alsY

x_data, y_data = data_to_sequence(data)

print(x_data.shape)
print(y_data.shape)


# In[ ]:


model = build_model(features = 6, seq_len = seq_len, out = 1)
model.summary()


# In[ ]:


from keras.callbacks import TensorBoard , ModelCheckpoint, ReduceLROnPlateau


tbCallBack = TensorBoard(log_dir ='./logs/', 
                         histogram_freq = 0, 
                         write_graph = True)

filepath = "best_model.hdf5"
best_model = ModelCheckpoint(filepath = filepath, 
                             monitor = 'val_loss', 
                             verbose = 1, 
                             save_best_only = True, 
                             save_weights_only = False, 
                             mode = 'auto', period = 1)


reduce_lr = ReduceLROnPlateau(monitor = 'val_loss', factor = 0.5, patience = 2)


# In[ ]:


model.fit(x_data,
          y_data,
          batch_size = 100,
          epochs = 800,
          validation_split = 0.05,
          callbacks = [best_model, tbCallBack, reduce_lr])


# In[ ]:




