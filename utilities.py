import numpy as np
import pandas as pd
from datetime import datetime

def split_data(stock, lookback):
    data_raw = stock.to_numpy() 
    data = []
    
    # create all possible sequences of length seq_len
    for index in range(len(data_raw) - lookback): 
        data.append(data_raw[index: index + lookback])
    
    data = np.array(data)
    test_set_size = int(np.round(0.2*data.shape[0]))
    train_set_size = data.shape[0] - (test_set_size)
    
    x_train = data[:train_set_size,:-1,:]
    y_train = data[:train_set_size,-1,:]
    
    x_test = data[train_set_size:,:-1]
    y_test = data[train_set_size:,-1,:]
    
    return [x_train, y_train, x_test, y_test]

def string_to_time(date):
    
    date = datetime.strptime(date, '%Y-%m-%d')
    date = datetime.timestamp(date)
    return date 

def normalize(x, min, max):
    return (x - min)/(max - min)

def reverse_normalize(y, min, max):
    return y*(max - min) + min

def min_max_dic(dataset):
    dic = {}
    for col in dataset.columns:
        dic[col] = [dataset[col].min(), dataset[col].max()]
        dataset[col] = dataset[col].apply(lambda x: normalize(x, dic[col][0], dic[col][1]))
    return dic
