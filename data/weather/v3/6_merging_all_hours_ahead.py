
# coding: utf-8

# In[ ]:


import pandas as pd
import glob, os
from tqdm import tqdm

years = [2013, 2014, 2015, 2016, 2017]
for year in years:
	for hour in range(72 + 1):
		print('For year: ' + str(year))
		print('For h: ' + str(hour))
		directory = "./" + str(year) + '/' 
		os.chdir(directory)
		all_files = glob.glob("*csv")

		error_files = []
		merged = pd.DataFrame()
		hour_index = hour + 5
		
		for file in tqdm(all_files):
			try: 
				data = pd.read_csv(file)
				data = data.loc[data.index[hour_index]:data.index[hour_index]]        
				merged = pd.concat([merged, data])

				
			except:
				print('Error with file: ' +  file)
				error_files.append(file)

		merged = merged.sort_values(by = 'Time')
		merged.index = merged['Time']
		del merged['Time']
		merged_file_name = './merged/merged_' + str(year) + '_h' + str(hour) + '.csv'
		merged.to_csv(merged_file_name)
		
		dir_path = os.path.dirname(os.path.realpath(__file__))
		os.chdir(dir_path[:-4])




