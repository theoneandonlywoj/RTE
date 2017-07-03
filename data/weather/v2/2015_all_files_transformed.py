
# coding: utf-8

# In[1]:


import pandas as pd
import glob, os
from tqdm import tqdm
directory = "./data as csv/2015/" 
os.chdir(directory)
#print(glob.glob("*csv"))


# In[2]:


all_files = glob.glob("*csv")


# In[3]:


all_files[0]


# In[4]:


error_files = []


# In[5]:


broken_files_13 = ['P4503501.201301180800 .csv',
 'P4503501.201301250900 .csv',
 'P4503501.201302101100 .csv',
 'P4503501.201301180400 .csv',
 'P4503501.201302101000 .csv',
 'P4503501.201301261200 .csv',
 'P4503501.201302140700 .csv',
 'P4503501.201303130900 .csv',
 'P4503501.201301171200 .csv',
 'P4503501.201301170800 .csv',
 'P4503501.201302140900 .csv',
 'P4503501.201302101300 .csv',
 'P4503501.201302140500 .csv',
 'P4503501.201301171000 .csv',
 'P4503501.201301181300 .csv',
 'P4503501.201301180300 .csv',
 'P4503501.201301161200 .csv',
 'P4503501.201302140800 .csv',
 'P4503501.201302101200 .csv',
 'P4503501.201301250800 .csv',
 'P4503501.201301181000 .csv',
 'P4503501.201302141100 .csv',
 'P4503501.201302140400 .csv',
 'P4503501.201301180600 .csv',
 'P4503501.201301180700 .csv',
 'P4503501.201301170700 .csv',
 'P4503501.201301171400 .csv',
 'P4503501.201303131000 .csv',
 'P4503501.201301261100 .csv',
 'P4503501.201302140300 .csv',
 'P4503501.201301180200 .csv',
 'P4503501.201301181400 .csv',
 'P4503501.201302100900 .csv',
 'P4503501.201301251000 .csv',
 'P4503501.201301171100 .csv',
 'P4503501.201301170900 .csv',
 'P4503501.201302141200 .csv',
 'P4503501.201301181100 .csv',
 'P4503501.201301250600 .csv',
 'P4503501.201301250700 .csv',
 'P4503501.201301171300 .csv',
 'P4503501.201302100800 .csv',
 'P4503501.201301180900 .csv',
 'P4503501.201301181200 .csv',
 'P4503501.201301261000 .csv',
 'P4503501.201301180500 .csv',
 'P4503501.201301261300 .csv',
 'P4503501.201302141000 .csv',
 'P4503501.201302140600 .csv',
 'P4503501.201301171500 .csv']
broken_files_14 = ['P4503501.201412291100 .csv',
 'P4503501.201412310800 .csv',
 'P4503501.201412301200 .csv',
 'P4503501.201412311000 .csv',
 'P4503501.201412291000 .csv',
 'P4503501.201412290900 .csv',
 'P4503501.201412310700 .csv',
 'P4503501.201412310400 .csv',
 'P4503501.201412300800 .csv',
 'P4503501.201412301300 .csv',
 'P4503501.201412301000 .csv',
 'P4503501.201412311400 .csv',
 'P4503501.201412290800 .csv',
 'P4503501.201412301400 .csv',
 'P4503501.201412300900 .csv',
 'P4503501.201412310600 .csv',
 'P4503501.201412311300 .csv',
 'P4503501.201412310500 .csv',
 'P4503501.201412311100 .csv',
 'P4503501.201412301100 .csv',
 'P4503501.201412291200 .csv',
 'P4503501.201412311200 .csv',
 'P4503501.201412310900 .csv']
broken_files_15 = []
broken_files_16 = ['P4503501.201601181000 .csv',
 'P4503501.201601181200 .csv',
 'P4503501.201601180700 .csv',
 'P4503501.201601180900 .csv',
 'P4503501.201601181100 .csv',
 'P4503501.201601180800 .csv']
broken_files_17 = ['P4503501.201701071300 .csv',
 'P4503501.201701070300 .csv',
 'P4503501.201701070800 .csv',
 'P4503501.201701151300 .csv',
 'P4503501.201701070100 .csv',
 'P4503501.201701070600 .csv',
 'P4503501.201701220900 .csv',
 'P4503501.201701211100 .csv',
 'P4503501.201701160600 .csv',
 'P4503501.201701210700 .csv',
 'P4503501.201701161100 .csv',
 'P4503501.201701170800 .csv',
 'P4503501.201701211000 .csv',
 'P4503501.201701180700 .csv',
 'P4503501.201701161000 .csv',
 'P4503501.201701201300 .csv',
 'P4503501.201701190500 .csv',
 'P4503501.201701261000 .csv',
 'P4503501.201701170900 .csv',
 'P4503501.201701210800 .csv',
 'P4503501.201701170200 .csv',
 'P4503501.201701220800 .csv',
 'P4503501.201701180000 .csv',
 'P4503501.201701070900 .csv',
 'P4503501.201701181400 .csv',
 'P4503501.201701171100 .csv',
 'P4503501.201701061300 .csv',
 'P4503501.201701200900 .csv',
 'P4503501.201701211200 .csv',
 'P4503501.201701221300 .csv',
 'P4503501.201701180600 .csv',
 'P4503501.201701070200 .csv',
 'P4503501.201701271100 .csv',
 'P4503501.201701151000 .csv',
 'P4503501.201701070500 .csv',
 'P4503501.201701170400 .csv',
 'P4503501.201701200600 .csv',
 'P4503501.201701170700 .csv',
 'P4503501.201701231200 .csv',
 'P4503501.201701180800 .csv',
 'P4503501.201701151200 .csv',
 'P4503501.201701061100 .csv',
 'P4503501.201701151400 .csv',
 'P4503501.201701171200 .csv',
 'P4503501.201701061200 .csv',
 'P4503501.201701231100 .csv',
 'P4503501.201701171000 .csv',
 'P4503501.201701190400 .csv',
 'P4503501.201701150900 .csv',
 'P4503501.201701190800 .csv',
 'P4503501.201701170300 .csv',
 'P4503501.201701181100 .csv',
 'P4503501.201701201100 .csv',
 'P4503501.201701221200 .csv',
 'P4503501.201701180400 .csv',
 'P4503501.201701231000 .csv',
 'P4503501.201701071200 .csv',
 'P4503501.201701181300 .csv',
 'P4503501.201701070700 .csv',
 'P4503501.201701180100 .csv',
 'P4503501.201701181000 .csv',
 'P4503501.201701160800 .csv',
 'P4503501.201701190700 .csv',
 'P4503501.201701170600 .csv',
 'P4503501.201701071000 .csv',
 'P4503501.201701261100 .csv',
 'P4503501.201701260800 .csv',
 'P4503501.201701180200 .csv',
 'P4503501.201701260700 .csv',
 'P4503501.201701260500 .csv',
 'P4503501.201701160900 .csv',
 'P4503501.201701180900 .csv',
 'P4503501.201701171400 .csv',
 'P4503501.201701180500 .csv',
 'P4503501.201701181200 .csv',
 'P4503501.201701230900 .csv',
 'P4503501.201701261200 .csv',
 'P4503501.201701160700 .csv',
 'P4503501.201701170100 .csv',
 'P4503501.201701161300 .csv',
 'P4503501.201701260400 .csv',
 'P4503501.201701070400 .csv',
 'P4503501.201701170500 .csv',
 'P4503501.201701161400 .csv',
 'P4503501.201701180300 .csv',
 'P4503501.201701201200 .csv',
 'P4503501.201701171300 .csv',
 'P4503501.201701201000 .csv',
 'P4503501.201701071100 .csv',
 'P4503501.201701260600 .csv',
 'P4503501.201701161200 .csv',
 'P4503501.201701200700 .csv',
 'P4503501.201701261300 .csv',
 'P4503501.201701170000 .csv',
 'P4503501.201701231300 .csv',
 'P4503501.201701260900 .csv',
 'P4503501.201701210900 .csv',
 'P4503501.201701221000 .csv',
 'P4503501.201701151100 .csv',
 'P4503501.201701190600 .csv',
 'P4503501.201701221100 .csv']


# In[6]:


for file in tqdm(all_files):
    try:
        data = pd.read_csv(file, usecols = ['station', 'date.validite', 'temperature', 'nebulosite'])
        data.columns = ['station','Time', 'temperature', 'cloudiness']

        data.index = data['Time'] 

        weather_data = pd.DataFrame()
        temp = pd.DataFrame()

        if file in broken_files_15:
            # Some files have broken naming
            stations = ['002', '005', '015', '027', '070', '110', '120', '130', '145', '149', '156','168', 
                        '180', '190', '222', '240', '255', '260', '280', '299', '434', '460', '481', '497', 
                        '510', '579', '588', '621', '630', '643', '645', '650', '675', '690', '747']
            #print(file)

            for station in stations: 
                temp = data.loc[data['station'] == station]
                temperature_index = 'temperature-' + str(station)
                cloudiness_index = 'cloudiness-' + str(station)
                weather_data[temperature_index] = temp['temperature']
                weather_data[cloudiness_index] = temp['cloudiness']

        else:
            stations = [2, 5, 15, 27, 70, 110, 120, 130, 145, 149, 156,
                    168, 180, 190, 222, 240, 255, 260, 280, 299, 434,
                    460, 481, 497, 510, 579, 588, 621, 630, 643, 645,
                    650, 675, 690, 747]

            for station in stations:
                if station in stations[0:2]:
                    temp = data.loc[data['station'] == station]
                    temperature_index = 'temperature-00' + str(station)
                    cloudiness_index = 'cloudiness-00' + str(station)
                    weather_data[temperature_index] = temp['temperature']
                    weather_data[cloudiness_index] = temp['cloudiness']

                elif station in stations[2:5]:
                    temp = data.loc[data['station'] == station]
                    temperature_index = 'temperature-0' + str(station)
                    cloudiness_index = 'cloudiness-0' + str(station)
                    weather_data[temperature_index] = temp['temperature']
                    weather_data[cloudiness_index] = temp['cloudiness']
                else:
                    temp = data.loc[data['station'] == station]
                    temperature_index = 'temperature-' + str(station)
                    cloudiness_index = 'cloudiness-' + str(station)
                    weather_data[temperature_index] = temp['temperature']
                    weather_data[cloudiness_index] = temp['cloudiness']

        current_weather = pd.DataFrame(columns = weather_data.columns)
        #current_weather = weather_data.loc[weather_data.index[5]:weather_data.index[6]]
        current_weather = weather_data.loc[:]
        #current_weather.drop(current_weather.index[1], inplace = True)
        if current_weather.empty:
            print('DataFrame is empty!')
        current_weather.to_csv(file)
        #print(file)
    except:
        print('Error with file: ' +  file)
        error_files.append(file)


# In[ ]:





# In[ ]:




