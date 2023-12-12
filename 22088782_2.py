#acess data from yahoo through wbgapi
import wbgapi as wb
wb.source.info()
#choose database 2 as it is the climate change database
wb.db = 2
#to get names of columns in database
wb.series.info()

#storing one dataframe with dates as columns as asked
df1 = wb.data.DataFrame(['NY.GDP.PCAP.CD'],['ARG','AUS','BGR','CHN','CAN','IND','FIN','ISR','ZAF','PAK','USA']) 
df1

#storing one dataframe with country as columns
df2 = wb.data.DataFrame(wb.topic.members(19),['ARG','AUS','BGR','CHN','CAN','IND','FIN','ISR','ZAF','PAK','USA'], time = 2015) # most recent 5 years 
df2 = df2. transpose()
df2

wb.topic.members(19)
#This is to get the topic that is relevant to climate change in database

df11 = wb.data.DataFrame(['EN.ATM.GHGT.KT.CE'],['ARG','AUS','BGR','CHN','CAN','IND','FIN','ISR','ZAF','PAK','USA'], time =range(1990, 2020, 5)) 
df11 =df11.transpose()
df11

#importing all the packages
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

#This entire block talks about greenhouse gas emission across 11 countries from 1990 to 2020 with a gap of 5 years
df_temp_1 = wb.data.DataFrame(['EN.ATM.GHGT.KT.CE'],['ARG','AUS','BGR','CHN','CAN','IND','FIN','ISR','ZAF','PAK','USA'], time =range(1990, 2024, 5), labels = True) 
df_temp_1 = df_temp_1.transpose()
#renaming the original variables
df_temp_1.rename(columns = {'PAK':'Pakistan', 'ZAF':'South Africa','ISR':'Israel','FIN':'Finland','CAN':'Canada','IND':'India','CHN':'China','BGR':'Bulgaria','AUS':'Australia','ARG':'Argentina'}, inplace = True)
df_temp_1 = df_temp_1.transpose()
df_temp_1

#plotting the bar plot
df_temp_1.plot(kind="bar", figsize = (15,8), width = 0.7)
plt.title("Country wise Greenhouse Gas emission")
plt.xlabel("Country")
plt.ylabel("Greenhouse Gas emission")
df_temp_1


#this is for find the correlation materix to check what is affecting the greenhouse gases so much for china
df_temp_2 = wb.data.DataFrame(['EN.ATM.GHGT.KT.CE','EN.ATM.CO2E.KT','NY.GDP.PCAP.CD','AG.LND.ARBL.ZS','AG.LND.FRST.ZS','EG.USE.ELEC.KH.PC','EG.ELC.ACCS.ZS','EG.USE.PCAP.KG.OE','EN.ATM.METH.AG.ZS','EG.ELC.RNEW.ZS','SP.POP.TOTL', 'SP.URB.TOTL.IN.ZS'],['CHN'], time =range(1990,2021,5))
df_temp_2 = df_temp_2.transpose()
df_temp_2.rename(columns = {'SP.URB.TOTL.IN.ZS':'Urban population % ','EN.ATM.GHGT.KT.CE':'Greenhouse Gas emission','SP.POP.TOTL':'Population, total','SP.URB.GROW':'Urban population growth annual %','EN.ATM.CO2E.KT':'CO2 emissions in kt','NY.GDP.PCAP.CD':'GDP per capita','AG.LND.ARBL.ZS':'Arable land %','EG.ELC.RNEW.ZS':'Renewable electricity output in %','AG.LND.FRST.ZS':'Forest area %','EG.USE.ELEC.KH.PC':'Electric power consumption','EG.ELC.ACCS.ZS':'Access to electricity %','EG.USE.PCAP.KG.OE':'Energy use','EN.ATM.METH.AG.ZS':'Agricultural methane emissions'}, inplace = True)
import seaborn as sns
correlation_mat = df_temp_2.corr()
f = plt.figure(figsize=(19, 15))
sns.heatmap(correlation_mat,annot = True)
plt.title("China", fontsize=16) 
plt.xlabel("Factors impacting greenhouse gases", fontsize = 16)
plt.ylabel("Factors impacting greenhouse gases", fontsize = 16)
plt.show()
df_temp_2

#This block shows the GDP per capita of 11 countries from 1990 to 2020 at interval of 5 years
df_temp_3 = wb.data.DataFrame(['NY.GDP.MKTP.CD'],['ARG','AUS','BGR','CHN','CAN','IND','FIN','ISR','ZAF','PAK','USA'], time =range(1990, 2024, 5), labels = True) 
df_temp_3 = df_temp_3.transpose()
df_temp_3.rename(columns = {'PAK':'Pakistan', 'ZAF':'South Africa','ISR':'Israel','FIN':'Finland','CAN':'Canada','IND':'India','CHN':'China','BGR':'Bulgaria','AUS':'Australia','ARG':'Argentina'}, inplace = True)
df_temp_3 = df_temp_3.transpose()
df_temp_3
df_temp_3.plot(kind="bar", figsize = (15,8), width = 0.7)
plt.title("Country wise GDP per capita")
plt.xlabel("Country")
plt.ylabel("GDP per capita")
df_temp_3

#This block is used to calculate the growth rate of urban population between 1990 and 2021
df_temp_4 = wb.data.DataFrame(['SP.URB.TOTL.IN.ZS'],['ARG','AUS','BGR','CHN','CAN','IND','FIN','ISR','ZAF','PAK','USA'], time =range(1990, 2022,31), labels = True) 
df_temp_4 = df_temp_4.transpose()
df_temp_4.rename(columns = {'PAK':'Pakistan', 'ZAF':'South Africa','ISR':'Israel','FIN':'Finland','CAN':'Canada','IND':'India','CHN':'China','BGR':'Bulgaria','AUS':'Australia','ARG':'Argentina'}, inplace = True)
df_temp_4 = df_temp_4.transpose()
#Adding another column which depicts the growth rate in percentage
df_temp_4['growth rate'] =  (df_temp_4['YR2021'] - df_temp_4['YR1990'])/df_temp_4['YR1990'] *100
df_temp_4
#plotting the horizontal bar chart
df_temp_4['growth rate'].plot(kind="barh", figsize = (15,8), width = 0.7)
plt.title("Urban Population growth rate")
plt.xlabel("% Growth rate from 1990")
plt.ylabel("Country")
df_temp_4

#This block shows the arable land in hectares between 1990 and 2021 and the changes
df_temp_5 = wb.data.DataFrame(['AG.LND.ARBL.HA'],['ARG','AUS','BGR','CHN','CAN','IND','FIN','ISR','ZAF','PAK','USA'], time =range(1990, 2022,1)) 
df_temp_5 = df_temp_5.transpose()
df_temp_5.rename(columns = {'PAK':'Pakistan', 'ZAF':'South Africa','ISR':'Israel','FIN':'Finland','CAN':'Canada','IND':'India','CHN':'China','BGR':'Bulgaria','AUS':'Australia','ARG':'Argentina'}, inplace = True)
df_temp_5.plot(kind="line", figsize = (15,8))
plt.title("Arable Land in hectares")
plt.xlabel("Year")
plt.ylabel("Arable land")

df_temp_5

#This blocks shows the decline in arable land between 1990 and 2021 for all the countries
df_temp_5 = df_temp_5.transpose()
df_temp_5['land decline rate'] =  (df_temp_5['YR2021'] - df_temp_5['YR1990'])/df_temp_5['YR1990'] *100
df_temp_5['land decline rate']

#This block is used to find the correlation matrix of what is affecting the green house emission of India
df_temp_6 = wb.data.DataFrame(['EN.ATM.GHGT.KT.CE','NY.GDP.PCAP.CD','AG.LND.ARBL.ZS','AG.LND.FRST.ZS','EG.USE.ELEC.KH.PC','EG.USE.PCAP.KG.OE'],['IND'], time =range(1990,2021,5))
df_temp_6 = df_temp_6.transpose()
df_temp_6.rename(columns = {'EN.ATM.GHGT.KT.CE':'Greenhouse Gas emission','NY.GDP.PCAP.CD':'GDP per capita','AG.LND.ARBL.ZS':'Arable land %','AG.LND.FRST.ZS':'Forest area %','EG.USE.ELEC.KH.PC':'Electric power consumption','EG.USE.PCAP.KG.OE':'Energy use'}, inplace = True)
correlation_mat = df_temp_6.corr()
f = plt.figure(figsize=(19, 15))
sns.heatmap(correlation_mat,annot = True)
plt.title("India", fontsize=16) 
plt.xlabel("Factors impacting greenhouse gases", fontsize = 16)
plt.ylabel("Factors impacting greenhouse gases", fontsize = 16)
plt.show()
df_temp_6

#This block is to check if methane production form any agriculture or non agricultural sources is dependent on any other paramters for India
df_temp_7 = wb.data.DataFrame(['EN.ATM.METH.AG.ZS','EN.ATM.METH.EG.ZS','EG.USE.PCAP.KG.OE','EG.ELC.ACCS.ZS'],['IND'], time =range(1990,2021,5))
df_temp_7 = df_temp_7.transpose()
df_temp_7.rename(columns = {'EN.ATM.METH.AG.ZS':'Agricultural methane emissions %','EN.ATM.METH.EG.ZS':'Non agri methan emission %','EG.USE.PCAP.KG.OE':'Energy use','EG.ELC.ACCS.ZS':'Access to electricity %'}, inplace = True)
import seaborn as sns
correlation_mat = df_temp_7.corr()
f = plt.figure(figsize=(19, 15))
sns.heatmap(correlation_mat,annot = True)
plt.title("India", fontsize=16) 
plt.xlabel("Factors impacting methane production", fontsize = 16)
plt.ylabel("Factors impacting methane production", fontsize = 16)
plt.show()
df_temp_7


#This blocks shows the forest area  in sq kms of different countries and the changes over time
df_temp_8 = wb.data.DataFrame(['AG.LND.FRST.K2'],['ARG','AUS','BGR','CHN','CAN','IND','FIN','ISR','ZAF','PAK','USA'], time =range(1990, 2022,1)) 
df_temp_8 = df_temp_8.transpose()
df_temp_8.rename(columns = {'PAK':'Pakistan', 'ZAF':'South Africa','ISR':'Israel','FIN':'Finland','CAN':'Canada','IND':'India','CHN':'China','BGR':'Bulgaria','AUS':'Australia','ARG':'Argentina'}, inplace = True)
df_temp_8.plot(kind="line", figsize = (15,8))
plt.title("Forest Area in sq kms")
plt.xlabel("Year")
plt.ylabel("Forest area")

df_temp_8

#This block is used to calcualte the increase/decrease in forest rate across countries over time
df_temp_8 = df_temp_8.transpose()
df_temp_8['forest increase rate'] =  (df_temp_8['YR2021'] - df_temp_8['YR1990'])/df_temp_8['YR1990'] *100
df_temp_8['forest increase rate']

#This block depicts the correlation matrix of what is affecting the green house emission in USA
df_temp_9 = wb.data.DataFrame(['EN.ATM.GHGT.KT.CE','NY.GDP.PCAP.CD','AG.LND.ARBL.ZS','AG.LND.FRST.ZS','EG.USE.ELEC.KH.PC','EG.USE.PCAP.KG.OE'],['USA'], time =range(1990,2021,5))
df_temp_9 = df_temp_9.transpose()
df_temp_9.rename(columns = {'EN.ATM.GHGT.KT.CE':'Greenhouse Gas emission','NY.GDP.PCAP.CD':'GDP per capita','AG.LND.ARBL.ZS':'Arable land %','AG.LND.FRST.ZS':'Forest area %','EG.USE.ELEC.KH.PC':'Electric power consumption','EG.USE.PCAP.KG.OE':'Energy use'}, inplace = True)
correlation_mat = df_temp_9.corr()
f = plt.figure(figsize=(19, 15))
sns.heatmap(correlation_mat,annot = True)
plt.title("USA", fontsize=16) 
plt.xlabel("Factors impacting greenhouse gases", fontsize = 16)
plt.ylabel("Factors impacting greenhouse gases", fontsize = 16)
plt.show()
df_temp_9

#This block depicts the methane production from different sources and how it is affected by other parameters
df_temp_10 = wb.data.DataFrame(['EN.ATM.METH.AG.ZS','EN.ATM.METH.EG.ZS','EG.USE.PCAP.KG.OE'],['USA'], time =range(1990,2021,5))
df_temp_10 = df_temp_10.transpose()
df_temp_10.rename(columns = {'EN.ATM.METH.AG.ZS':'Agricultural methane emissions %','EN.ATM.METH.EG.ZS':'Non agri methan emission %','EG.USE.PCAP.KG.OE':'Energy use'}, inplace = True)
correlation_mat = df_temp_10.corr()
f = plt.figure(figsize=(19, 15))
sns.heatmap(correlation_mat,annot = True)
plt.title("USA", fontsize=16) 
plt.xlabel("Factors impacting methane production", fontsize = 16)
plt.ylabel("Factors impacting methane production", fontsize = 16)
plt.show()
df_temp_10
