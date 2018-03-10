import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

DataFolderPath = 'C:/Users/Akwesi/Desktop/Our_Project/OpenEi -Lab-Long-term energyenvironment data for a Research House/0 DataSet'
DataFile = 'ornlbtricdatafromcc3fy2014.csv'
DataFilePath= DataFolderPath+"/"+DataFile  #to call the folder path containing the  file
DF_Dataset = pd.read_csv(DataFilePath,sep=",",index_col=0) 
#DF_EnergyData.index
NewparsedIndex = pd.to_datetime(DF_Dataset.index)  ## using to_datatime convert the date index to real date
DF_Dataset.index=NewparsedIndex  # to assign the new index with the old index
#apply dropna() to take of all Nan
#DF_cleanDataset = DF_Dataset.dropna()


Chosen_dataset = DF_Dataset['2014-08-20':'2014-08-31']
SelectedParameters = Chosen_dataset[['main_Tot','PV_generated_Tot','NWallcav_HFT_Avg', 'SlrW_PV_Avg', 'Tstat1_tmp_Avg','garage_tmp_Avg','Outside_RH_Avg']]
SelectedParameters.dropna()


fig = plt.figure()
plot = fig.add_axes()
plot = sns.heatmap(SelectedParameters.corr(), annot=False)
plot.xaxis.tick_top() 
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.show()

'''A function to normalize dataset's columns values to provide a ranged insight'''
def normalize(df):
    return (df-df.min())/(df.max()-df.min())

#Plotting the normalized dataframe with selected columns
DF_normalized=normalize(SelectedParameters)
PlotDF=DF_normalized[["PV_generated_Tot","Tstat1_tmp_Avg"]]
PlotDF.plot()
plt.title("Normalized plot")
plt.show()


