
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import keras
from build_model import build_model

data_x = pd.read_csv('./data/weather/v3/2013/merged/merged_2013_h0.csv', index_col = 'Time')
data_x.columns

x = data_x[['temperature-460', 'cloudiness-460',
            'temperature-481', 'cloudiness-481',
            'temperature-645', 'cloudiness-645',]]

data_y = pd.read_csv('./data/energy/v5/2013/Consumption_2013.csv', index_col = 'Time')
data = x.copy()
data['cons'] = data_y['Auvergne-Rhone-Alpes']


data.drop(data.index[0], inplace = True)

print(data.isnull().values.any())

print(data.isnull().sum())


# In[ ]:


data_train = data.values
x_train = data_train[:, 0:6]
y_train = data_train[:, 6]


# In[ ]:


x_train[:5, :]


# In[ ]:


y_train[:5]


# In[ ]:


#data.isnull().values.any()
#data.isnull().sum()


# In[ ]:


# Before
x_min = np.min(x_train)
print(x_min)

x_max = np.max(x_train)
print(x_max)

#x_train = (x_train - np.min(x_train)) / (np.max(x_train) - np.min(x_train))

# After 
x_min = np.min(x_train)
print(x_min)

x_max = np.max(x_train)
print(x_max)


# In[ ]:


'''y_train = (y_train - np.min(y_train)) / (np.max(y_train) - np.min(y_train))'''


# # Test data

# In[ ]:


data_x = pd.read_csv('./data/weather/v3/2014/merged/merged_2014_h0.csv', index_col = 'Time')
data_x.columns

x = data_x[['temperature-460', 'cloudiness-460',
            'temperature-481', 'cloudiness-481',
            'temperature-645', 'cloudiness-645',]]

data_y = pd.read_csv('./data/energy/v5/2014/Consumption_2014.csv', index_col = 'Time')
data = x.copy()
data['cons'] = data_y['Auvergne-Rhone-Alpes']


#data.drop(data.index[0], inplace = True)

print(data.isnull().values.any())

print(data.isnull().sum())

data_test = data.values
x_test = data_test[:, 0:6]
y_test = data_test[:, 6]

#x_test = (x_test - np.min(x_test)) / (np.max(x_test) - np.min(x_test))
#x_test = (x_test / (np.max(x_train))

# In[ ]:


seq_len = 100
def data_to_sequence(data, n_prev = seq_len):  
    
    docX, docY = [], []
    for i in range(len(data)-n_prev):
        docX.append(data[i:i+n_prev, 0:6])
        docY.append(data[i+n_prev, 6])
    alsX = np.array(docX)
    alsY = np.array(docY)

    return alsX, alsY


# In[ ]:


x_train, y_train = data_to_sequence(data_train)


# In[ ]:


x_test, y_test = data_to_sequence(data_test)


# In[ ]:


model = build_model(features = 6, seq_len = seq_len, out = 1)
print(model.summary())

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


model.fit(x_train,
          y_train,
          batch_size = 100,
          epochs = 100,
          validation_data = [x_test, y_test],
          callbacks = [best_model, tbCallBack, reduce_lr])


# In[ ]:




