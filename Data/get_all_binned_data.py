# -*- coding: utf-8 -*-
"""
Script for binning the data for all 3 datasets, and storing the results in 
a .pkl file. This can be done for both the training (A) and testing (B) data.
@author: oscar
"""

import numpy as np
from scipy import io
import pickle

################### SELECT OPTION, PARAMETERS ############################

# Parameters
bin_vector = [1, 5, 10, 20, 50, 100]
datasets =['Flint','Sabes','Brochier']
train_or_test = 'test' # 'train' for training data (A), 'test' for testing data (B)

# Specify root directory (where all code is located)
root_directory = r'path to Hardware-efficient-MUA-compression directory'

##########################################################################

# Get path to Formatted data
data_directory = root_directory + '\\Data\\Formatted_data'


all_binned_data = []
for BP in bin_vector:
    both_datasets = []
    for dataset in datasets:
        
        # No train data for Brochier, it's all test (B) data
        if train_or_test == 'train':
            if dataset == 'Brochier':
                continue
        
        data = []
       
        # Find filenames
        file_names = root_directory + '\\filenames_' + dataset +'_' + train_or_test + '.txt'
        with open(file_names) as f:
            lines = f.readlines()

        # Iterate through formatted data, collate all channels across files together
        for rec in np.arange(len(lines)):
            file_name = lines[rec].replace('\n','')
            
            mat_filename = root_directory + '\\Data\\' + dataset +'_data\\' + file_name + '_BP_'+\
            str(int(BP)) + '_ms' + '.mat'         
            print ("Loading input features from file: "+mat_filename)
            f = io.loadmat(mat_filename)

            nb_channels = len(f['binned_MUA'][0,:])                
            for chan in np.arange(nb_channels):
                data.append(f['binned_MUA'][:,chan])

        # Add to both datasets list
        both_datasets.append(data)
        
    all_binned_data.append(both_datasets)


# Store binned data
file_name = data_directory + '\\all_binned_data_'+train_or_test+'.pkl'
with open(file_name, 'wb') as file:
                  
    results = {'all_binned_data': all_binned_data,
               'bin_vector': bin_vector,
               'datasets': datasets} # Shows how much of the validation data is used for assignment vs CR
    # A new file will be created
    pickle.dump(results, file)
    