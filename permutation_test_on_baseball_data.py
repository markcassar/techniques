import pandas as pd
import numpy as np
import random
from ggplot import *

df = pd.read_csv('c:\\users\\bonnie\\desktop\\mark_work\\nanodegree\\intro_to_data_science\\baseball_data\\baseball_data.csv')

df_L = df[ df['handedness'] == 'L' ]
df_R = df[ df['handedness'] == 'R' ]
df_L_avg = df_L['avg']
df_R_avg = df_R['avg']

L_avg = np.mean(df_L_avg)
R_avg = np.mean(df_R_avg)

df_L_R = df_L.add(df_R)

delta_avg = L_avg - R_avg

lst_of_averages = []

for i in range(10000):

    rows_L = random.sample(df_L_avg.index, 150)
    df_L_avg_sample = df_L_avg.ix[rows_L]
    df_L_avg_sample = df_L_avg_sample.reset_index()
    
    df_L_avg_remainder = df_L_avg.drop(rows_L)
    df_L_avg_remainder = df_L_avg_remainder.reset_index()
    
    rows_R = random.sample(df_R_avg.index, 150)
    df_R_avg_sample = df_R_avg.ix[rows_R]
    df_R_avg_sample = df_R_avg_sample.reset_index()
    df_R_avg_remainder = df_R_avg.drop(rows_R)
    df_R_avg_remainder = df_R_avg_remainder.reset_index()
    
    dfL = df_L_avg_remainder.add(df_R_avg_sample)
    dfR = df_R_avg_remainder.add(df_L_avg_sample)
    new_L_avg = np.mean(dfL['avg']) 
    new_R_avg = np.mean(dfR['avg'])
    new_delta_avg = new_L_avg - new_R_avg
    
    lst_of_averages.append(new_delta_avg)

averages = pd.DataFrame(lst_of_averages, columns=['averages'])
print ggplot(aes(x='averages'), data=averages) + geom_histogram() + geom_vline(xintercept = delta_avg, color=
'blue')



