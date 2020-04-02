import os
import pandas as pd
import numpy as np



def detect_outlier(df):
    
    data_1 = df['Daily sale']
    
    nan_index_values = data_1.index[data_1.apply(np.isnan)]
    nan_index_list = list(nan_index_values)
    
    data_1_series = pd.Series(data_1)
    
    val_index_check = data_1_series.to_numpy().nonzero()
    non_zero_with_nan_index_list = list(val_index_check[0])
    
    non_zero_minus_nan =[i for i in non_zero_with_nan_index_list if i not in nan_index_list]

    non_zeros_values = data_1_series.iloc[non_zero_minus_nan]

    threshold = 0.35
    

    # edge case
    if not data_1.any(axis=0):
        df["outlier_check"] = ''
        return df["outlier_check"]

    else:
        mean_1 = np.mean(non_zeros_values)
 
        if np.isnan(pd.Series.std(pd.Series(non_zeros_values))):
            std_1 = 0.0
        else:
            std_1 = pd.Series.std(non_zeros_values)


        print('std deviation: ',std_1)

        new_column = pd.Series([]) 
        
        for index,col_value in enumerate(data_1):
            
            if col_value == 0 or index in nan_index_list or std_1 == int(0):
                new_column[index] = ''
            
            else:
                if col_value != 0 or index not in nan_index_list:

                    z_score= (col_value - mean_1) / std_1

                    if np.abs(z_score) > threshold:
                        # col_value is outlier
                        new_column[index] = 0

                    else:
                        # col_value is not outlier
                        new_column[index] = ''

        return new_column
    
    
    
    
for folder in ['product','product1']:
    
    print(f'\n******************* Processing folder: {folder} ***********************')
    
    new_dir_name = folder+'_modified'
    
    if not os.path.exists(new_dir_name):
        os.makedirs(new_dir_name)
       
    for filename in os.listdir(folder):    
            
        df = pd.read_csv(folder+'\\'+filename)
        
        print(f'\n======= Processing file: {filename} from folder {folder}')

        if len(df) == 0:
            df['outlier_check'] = ''
        else:
            new_col_series = detect_outlier(df)
        
            df['outlier_check'] = new_col_series

        print(f'\n======= Writing file: {filename} in folder {folder}')

        df.to_csv(new_dir_name+'\\'+filename, index=False, header=True)
        
    print('\n ###########################################################################################')    
    
    print('ONE FOLDER PROCESSED COMPLETELY, NOW PROCESSING NEXT FOLDER  \n')
    