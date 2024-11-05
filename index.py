#import statements
import os
from datetime import datetime

#folder path and prefix which uses current date
folder_path = './photos'
prefix =  datetime.now().date().strftime('%Y-%m-%d') + '_'
files = os.listdir(folder_path)

#loop through all files in the folder and rename them
for filename in range(0,len(files)):
    old_file_path = os.path.join(folder_path, files[filename])
    if os.path.isfile(old_file_path):
        new_filename = prefix +str(filename)+'.' +files[filename].split('.')[1]
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)
        print(f'Renamed: {filename} -> {new_filename}')
