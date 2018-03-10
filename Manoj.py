# -*- coding: utf-8 -*-
"""
Created on Thu Jan 04 14:19:12 2018

@author: MANOJ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_file(file_name):
    data_set = pd.read_csv(file_name,sep=',',index_col=0)
    
    desired_index = data_set.index

    datetime_index = pd.to_datetime(desired_index)
    
    data_set.index = datetime_index
    
    return data_set


def normalize(df):
    return (df - df.min())/(df.max()-df.min())
    
dataframe = read_file("C:/Users/MANOJ/Desktop/Data-driven Building Project/Open DataSets/DataSets/UCI Appliance Energy Prediction Dataset/0 Data/energydata_complete.csv")

    
#normalize(dataframe[['Appliances','T2']])['2016-05-23':'2016-05-26'].plot()

'''creating time related features'''

dataframe['hour'] = dataframe.index.hour
dataframe['day_of_week'] = dataframe.index.dayofweek
dataframe['month'] = dataframe.index.month

#dataframe['weekend'] = np.where(((dataframe['day_of_week']==5) or (dataframe['day_of_week']==6)), 1, 0)
dataframe['day_night'] = np.where((dataframe['hour']>=10)&(dataframe['hour']<=19), 1, 0)

def weekend_detector(day):
    if (day==5 or day==6):
        weekend = 1
    else:
        weekend = 0
    return weekend
    
    
dataframe['weekend'] = [weekend_detector(s) for s in dataframe['day_of_week']]

'''lag of features'''

dataframe['T6_24hour'] = dataframe['T6'].shift(24)
dataframe['T6_36hour'] = dataframe['T6'].shift(36)
dataframe['T_out_24hour'] = dataframe['T_out'].shift(24)
dataframe['T_out_36hour'] = dataframe['T_out'].shift(36)

#def lag_column(df,column_names,lag_times=1):
##df              > pandas dataframe
##column_names    > names of column/columns as a list
##lag_period      > number of steps to lag ( +ve or -ve) usually postive 
##to include past values for current row 
#    for column_name in column_names:
#        column_name = str(column_name)
#        for i in np.arange(1,lag_times+1,1):
#            new_column_name = column_name+'_'+str(i)+'hour'
#            #new_column_name = [col +'_'+str(i)+'hour' for col in column_name]
#            df[new_column_name]=(df[column_name]).shift(i)
#    return df
#
#df_lagged = lag_column(dataframe,['T6','T_out'],lag_times=6*4)

dataframe.dropna(inplace=True)

#import seaborn as sns
#fig = plt.figure()
##plot = fig.add_axes()
#plot = sns.heatmap(dataframe.corr(), annot=False)
#plot.xaxis.tick_top() 
#plt.yticks(rotation=0)
#plt.xticks(rotation=90)
#plt.show()
# 

dataframe_selected = dataframe[['Appliances','lights', 'T2', 'T3', 'T6','T_out', 'Windspeed', 'hour', 'day_night', 'T6_24hour']]

target = dataframe_selected[['Appliances']]
features = dataframe_selected[['lights', 'T2', 'T3', 'T6','T_out', 'Windspeed', 'hour', 'day_night', 'T6_24hour']]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=123524)

from sklearn import linear_model
linear_reg = linear_model.LinearRegression()

linear_reg.fit(X_train,y_train)

prediction = linear_reg.predict(X_test)

predict_series = pd.Series(prediction.ravel(),index=y_test.index).rename('Prediction appliance')
joined = pd.DataFrame(predict_series).join(y_test).dropna()



    
    