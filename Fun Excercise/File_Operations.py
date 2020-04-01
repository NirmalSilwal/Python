import os, glob, csv
import pandas as pd

all_folders = glob.glob('product*')

for folder in all_folders:
    print(f'Processing folder: {folder}')
    print('======================')
    
    new_dir_name = folder+'_modified'
    
    if not os.path.exists(new_dir_name):
        os.makedirs(new_dir_name)
    
        
    for filename in os.listdir(folder):
        print(f'Processing file: >>> {filename}')
        print('-----------------------')
        df = pd.read_csv(folder+'\\'+filename)
        
        # DO ALL PROCESSING/ MODIFICATION IN FILE HERE AND STORE IN DATAFRAME (df) 
        
        df.to_csv(new_dir_name+'\\'+filename, index=False, header=True)          
        