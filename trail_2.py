import numpy as np,pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt, seaborn as sns

#We import the pandas module, including ExcelFile. The method read_excel() reads the data 
#into a Pandas Data Frame, where the first parameter is the filename and the second parameter is the sheet.


DataFolderPath = 'C:/Users/Akwesi/Documents/bezhad/Open DataSets/DataSets/OpenEi Long-term electricity and gas consumption for LBNL Building 74/0 Data'
DataFilePath= DataFolderPath+"/"+'lbnlb74electricity.xlsx'  #to call the folder path containing the  file
DF_Dataset = pd.read_excel(DataFilePath, sheetname='Sheet1',index_col=0)

DF_Dataset.columns
DF_Dataset.index
DF_Dataset.describe() #summary of the Data frame
DF_Dataset.describe().loc['mean']
DF_Dataset.tail() #see the last five values
DF_Dataset.head() #see the first five values
#DF_Dataset.index=pd.to_datetime(DF_Dataset.index)
DF_Dataset.isnull()
DF_Dataset.isnull().sum()
DF_Dataset.shape


#DF_Dataset.plot()
'''creating time related features'''
DF_Dataset['hour'] = DF_Dataset.index.hour
DF_Dataset['day_of_week'] = DF_Dataset.index.dayofweek
DF_Dataset['month'] = DF_Dataset.index.month
DF_Dataset['day_night'] = np.where((DF_Dataset['hour']>=10)&(DF_Dataset['hour']<=19), 1, 0)

#for weekend we use function
def weekend_detector(day):
    if (day==5 or day==6):
        weekend = 1
    else:
        weekend = 0
    return weekend
    
    
DF_Dataset['weekend'] = [weekend_detector(s) for s in DF_Dataset['day_of_week']]

#DF_Dataset.columns
DF_Dataset.dropna(inplace=True)
SelectedData =DF_Dataset['2014-01-01 00:00:00':'2014-01-01 23:00:00'] 

#Plotting energy consumed for 24hr period
SelectedData.rename(columns={'Building 74 - kWh Total Electricity (kWh)':'Energy_Consumed[kWh]'},inplace=True)
S#electedData.columns
Energy_data = SelectedData['Energy_Consumed[kWh]']

Energy_data.plot().savefig('Energy_consumptn.png')
#Energy_data.savefig('Energy_consumptn.png',bbox_inches='tight',orientation='portrait',pad_inches=0.1)


fig = plt.figure("Figure for providing insight about Correlations")
plot = fig.add_axes()
plot = sns.heatmap(SelectedData.corr(), annot=False)
plot.xaxis.tick_top() 
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.show()

SelectedData.columns
SelectedData.plot('hour','day_night')
SelectedData.plot('hour','Energy_Consumed[kWh]')


