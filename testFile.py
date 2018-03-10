# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_file(file_name):

    data_set = pd.read_csv(file_name,sep=',',index_col=4)
    
    desired_index = data_set.index

    datetime_index = pd.to_datetime(desired_index)
    
    data_set.index = datetime_index
    
    return data_set


def normalize(df):
    return (df - df.min())/(df.max()-df.min())
    
dataframe = read_file("C:/Users/BOB/Desktop/7 Project/Data-driven Building Project/Open DataSets/DataSets/spanish datadriven building/DataSet/data1new.csv")


dataframe_selected = dataframe[['3:Temperature_Comedor_Sensor','4:Temperature_Habitacion_Sensor', '13:Meteo_Exterior_Crepusculo',
     '14:Meteo_Exterior_Viento', '15:Meteo_Exterior_Sol_Oest','16:Meteo_Exterior_Sol_Est',
     '17:Meteo_Exterior_Sol_Sud','18:Meteo_Exterior_Piranometro','22:Temperature_Exterior_Sensor']]  
dataframe_Normalized = normalize(dataframe_selected)

dataframe_Normalized['2012-03-20 00:00:00':'2012-03-21 23:59:00'].plot()
plt.xlabel('Time')
plt.ylabel('variables')
plt.show()

import seaborn as sns
fig = plt.figure()
plot = fig.add_axes()
plot = sns.heatmap(dataframe_selected.corr(), annot=False)
plot.xaxis.tick_top() 
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.show()
 


dataframe_Normalized = normalize(dataframe_selected)

data_selected = dataframe_Normalized['2012-03-20 00:00:00':'2012-03-21 23:59:00']

Data_Selected_lastest = data_selected[['3:Temperature_Comedor_Sensor',
                        '14:Meteo_Exterior_Viento','18:Meteo_Exterior_Piranometro']]

Data_Selected_lastest.plot()
plt.xlabel('Time')
plt.ylabel('variables')
plt.show()


Data_Selected_lastest['SOLARIrra_14hours'] = Data_Selected_lastest['18:Meteo_Exterior_Piranometro'].shift(16)
Data_Selected_lastest['Wind_28hours'] = Data_Selected_lastest['14:Meteo_Exterior_Viento'].shift(40)
Data_Selected_lastest.dropna()


Data_Selected_lastest.plot()
plt.xlabel('Time')
plt.ylabel('variables')
plt.show()



data_selected = dataframe_normalized['2012-03-20 00:00:00':'2012-03-21 23:59:00']

Data_selected_lastest = data_selected[['3:Temperature_Comedor_Sensor',
                        '14:Meteo_Exterior_Viento','18:Meteo_Exterior_Piranometro']]
Data_selected_lastest['SOLARIrra_14hours'] = Data_selected_lastest['18:Meteo_Exterior_Piranometro'].shift(14)
Data_selected_lastest['Wind_28hours'] = Data_selected_lastest['14:Meteo_Exterior_Viento'].shift(28)
Data_selected_lastest.dropna()

#Data_electedNEW = data_selected[['3:Temperature_Comedor_Sensor','4:Temperature_Habitacion_Sensor',
                       # '14:Meteo_Exterior_Viento','18:Meteo_Exterior_Piranometro']]

#Data_electedNEW['SOLARIrra_12hour'] = Data_electedNEW['18:Meteo_Exterior_Piranometro'].shift(12)
#Data_electedNEW.dropna()

#dataframe['T6_36hour'] = dataframe['T6'].shift(36)
#dataframe['T_out_24hour'] = dataframe['T_out'].shift(24)
#dataframe['T_out_36hour'] = dataframe['T_out'].shift(36)


Data_selected_lastest.plot()
plt.xlabel('Time')
plt.ylabel('variables')
plt.show()
