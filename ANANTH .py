#!/usr/bin/env python
# coding: utf-8

# First, create a function, import a library, and read a dataset before producing a line graph, a correlation matrix, a bar graph, and a time series graph.

# In[1]:


import pandas as pd 
from matplotlib import pyplot as matplot 
import numpy as np 


# #we are creating  function 

# In[2]:



def read_data(filename):
    data=pd.read_csv(filename,skiprows=4) # read csv file 
    data1=data.fillna(data.median(numeric_only=True)) # fill null values 
    data2=data1.drop(['Country Code', 'Indicator Name', 'Indicator Code', 'Unnamed: 66'],axis=1) # drop unused columns 
    data3=data2.set_index("Country Name") # set index name 
    data4=data3.T # transpose data
    data4.reset_index(inplace=True) # reset index name 
    data4.rename(columns = {'index':'Year'}, inplace = True)  # re name index name 
    return data,data4 # 


# In[3]:


filename="/content/API_19_DS2_en_csv_v2_4700503.csv" # read csv path 
df1,df2=read_data(filename) # reading data 
df1.head() # showing dataset 


# In[4]:


df2.head() # showing dataset 


# In[5]:


df2.describe() # describe dataset 


# # Showing data Country Name and Year With  Urban population Growth (annual %) 

# In[6]:


dataset_corr = df1[df1['Indicator Name']=='Urban population growth (annual %)']  # We are extracting data for 'urban population growth'. 

# We are creating pivot table in which index set as country name and values as years.
dataset_corr_1 = dataset_corr.pivot_table(index=['Country Name'], values = ['1965', '1990', '2000', '2005', '2021'])  
dataset_corr_1.head(10)  # showing top 10 rows of data.
 


# #Plotting Line Graph For Aruba Country (Indicator Name vs Year)

# In[7]:


df_line=df1.loc[df1['Country Name'] == "Aruba"]# extracting data for Aruba country. 
df_line1=df_line[['Indicator Name', '1960','1965','1970','1975','1980']]


# In[8]:


# all the variable taken in the table.
df_line2=df_line1.pivot_table(index=['Indicator Name'], values=['1960', '1965', '1970', '1975', '1980'])   
matplot.rcParams.update({'font.size': 20})# define font size.

matplot.figure(figsize = (20,8)) # define figure size 
matplot.plot(df_line2.head(50))  # set dataset 
matplot.xticks(rotation=90) # rotate axis name 
# define legend for graph.
matplot.legend(['1960', '1965', '1970','1975','1980']) 
# set x and y labels.
matplot.xlabel('Indicator Name')
matplot.ylabel('Comparison')
# define title name
matplot.title('Aruba (Indicator Name vs Year)')  
matplot.show() # showing graph 


# Our team is plotting Aruba's indicator line graph between 1960 and 1980. 1975 had the most people on Earth, according to the statistics.

# #Plotting Line Graph For India Country (Indicator Name vs Year)

# In[9]:


df_line3=df1.loc[df1['Country Name'] == "India"]# extracting data for India country.
df_line4=df_line3[['Indicator Name','1960','1965','1970','1975','1980']]


# In[10]:


# all the variable taken in the table.
df_line5=df_line4.pivot_table(index=['Indicator Name'], values=['1960', '1965', '1970', '1975', '1980'])   
matplot.figure(figsize = (20,8)) # define figure size 
matplot.xticks(rotation=90) # rotation axis name 
matplot.plot(df_line5.head(50)) # set dataset 
# set legend for graph.
matplot.legend(['1960', '1965', '1970', '1975', '1980'],bbox_to_anchor =(1.1, 1.1), ncol = 1) 
# x and y labels we set.
matplot.xlabel('Indicator Name')
matplot.ylabel('Comparison')
# define title name. 
matplot.title('India (Indicator Name vs Year)') 
matplot.show() # showing graph 


# in the midst of producing a graph for the nation of India between the years 1960 and 1980 about their indicative name. Based on the statistics presented, we may infer that 1980 was the most populous year overall.

# #Co2 Emissions With Country Name And  Year

# In[11]:


# Using pivot table data set for making the graph.
df_bar=df1.pivot_table(index=['Country Name'], values=['1970', '1980', '1990', '2000']) 
# define figure size
matplot.rcParams['figure.figsize']=(22,7)   
# print top 20 country.
df_bar1= df_bar.head(20)
# set color name 
df_bar1.plot.bar(color=['#33ccff', 'red', 'green',  'Blue', '#ff8080']) 
# set x label for graph.
matplot.xlabel('Country Name')
# set y label for graph.
matplot.ylabel('Comparision')
# define title name. 
matplot.title('Co2 Emissions With Country Name And  Year  ')  
matplot.show();


# #Agricultural land (% of land area)With Country Name  And   Year

# In[12]:


df_bar2= df1[df1['Indicator Name'] == 'Agricultural land (% of land area)']# data extracting for Agricultural land.


# In[13]:


df_bar3=df_bar2.pivot_table(index=['Country Name'], values=['1970', '1980', '1990', '2000']) 
# define figure size
matplot.rcParams['figure.figsize']=(22,7)  
# showing top 20 countries. 
df_bar4= df_bar3.head(20)  
# define color for figure.
df_bar4.plot.bar(color=['BlueViolet','red','Chartreuse','DarkOrange','Olive']) 
# x and y label set.
matplot.xlabel('Country Name')
matplot.ylabel('Comparision')
# set title for graph.
matplot.title('Agricultural land (% of land area)With Country Name  And   Year  ') 
matplot.show();


# #plotting correlation matrix for Nepal

# In[14]:


#creating function to extract data.
def fc(Country):
  df_mat = df1[df1['Country Name']==f'{Country}'] 
  df_mat = df_mat.drop(['Country Name', 'Country Code', 'Indicator Code'],axis=1) # drop some columns.
  df_mat = df_mat.T # transpose all data. 
  df_mat1=df_mat.iloc[0] 
  df_mat=df_mat[1:] 
  df_mat.columns=df_mat1
  df_mat = df_mat.reset_index(drop=True)
  return df_mat


# In[15]:


data_ct=fc('Nepal') # fatch country name 


# In[16]:


data_ct.to_csv('data_New.csv') # create new data set file 


# In[17]:


df3=pd.read_csv('/content/data_New.csv') # read dataset for Nepal country 
data=df3.drop(['Unnamed: 0'],axis=1) # drop unnamed columns 


# In[18]:


# set labels 
df_matrix = data[['Urban population (% of total population)',
            'Foreign direct investment, net inflows (% of GDP)', 
            'CO2 emissions from liquid fuel consumption (kt)',
            'CO2 emissions (kt)',
            'CO2 emissions (kg per 2015 US$ of GDP)',
            'Arable land (% of land area)',
            'Agricultural land (% of land area)',
            'Urban population growth (annual %)',
            'Population, total',
            'Population growth (annual %)',]]  


# In[19]:


df_corr=df_matrix.corr() #correlation
df_corr.head() # showing correlation 


# In[21]:



# importing  numpy 
arr=df_corr.to_numpy()
# converting in array
labs=df_matrix.columns
# getting columns
fig, Axis = matplot.subplots(figsize=(20,12))
# making subplots 
im = Axis.imshow(df_corr,cmap="gist_ncar")

Axis.set_xticks(np.arange(len(labs)))
# x_ticks
Axis.set_yticks(np.arange(len(labs)))
#  y_ticks
Axis.set_xticklabels(labs)
# x_ticks labels
Axis.set_yticklabels(labs)
# y_ticks labels
# Rotate the tick labels and align them.
matplot.setp(Axis.get_xticklabels(), rotation=60, ha="right",rotation_mode="anchor") 

# # Create text annotations by looping through data dimensions.
for i in range(len(labs)):
  #for loop for label
    for j in range(len(labs)):
        text = Axis.text(j, i, round(arr[i, j],2), ha="center", va="center", color="b") 
#setting title
Axis.set_title("Nepal") 
#setting show
matplot.show() 


# We're creating a heatmap graphic for Nepal that correlates CO2 emissions (kt) with urban population growth (annual%) and liquid fuel usage (kt).

# #Plotting correlation matrix for India 

# In[22]:


data_ct1=fc('India')


# In[23]:


data_ct1.to_csv('data_New1.csv')
#saving csv


# In[24]:


data_New1=pd.read_csv('/content/data_New1.csv') # read dataset for india country
data1=data_New1.drop(['Unnamed: 0'],axis=1) # drop unnamed columns 


# In[25]:


# set labels 
df4 = data1[['Urban population (% of total population)','Foreign direct investment, net inflows (% of GDP)', 'CO2 emissions from liquid fuel consumption (kt)','CO2 emissions (kt)','CO2 emissions (kg per 2015 US$ of GDP)','Arable land (% of land area)','Agricultural land (% of land area)','Urban population growth (annual %)','Population, total','Population growth (annual %)',]]  


# In[26]:


df_corr1=df4.corr()
 # correlation 
df_corr1.head()
#visuaizing first five rows


# In[27]:



arr=df_corr1.to_numpy()
#converting in numpy 
labs=df4.columns
fig, Axis = matplot.subplots(figsize=(20,12))  
#  set figure size 
im = Axis.imshow(df_corr1,cmap="Blues") 
# define figure color  

#  show all labels length 
Axis.set_xticks(np.arange(len(labs)))
#x ticks
Axis.set_yticks(np.arange(len(labs)))
#y_ticks
Axis.set_xticklabels(labs)
#x_ticks label
Axis.set_yticklabels(labs)
#y_ticks label

# Rotate the tick labels and set their alignment.
matplot.setp(Axis.get_xticklabels(), rotation=60, ha="right",rotation_mode="anchor") 

# Create text annotations by looping through data dimensions.
for i in range(len(labs)):
    for j in range(len(labs)):
        text = Axis.text(j, i, round(arr[i, j],2), ha="center", va="center", color="black") 

Axis.set_title("India") 
 # set title name 
matplot.show() 
 # showing correlation


# From the graph, we can conclude that CO2 emissions (kt) are positively correlated with CO2 emissions (kg per 2015 US$ of GDP) and urban population increase (annual %).

# # Plotting tine series graph  for Urban population (% of total population)

# In[28]:


# data extracting for urban population.
dataset_time= df1[df1['Indicator Name']=='Urban population (% of total population)'] 
dataset_time1=dataset_time.set_index("Country Name") 
dataset_time2=dataset_time1.drop(['Country Code', 'Indicator Name', 'Indicator Code', 'Unnamed: 66'],axis=1)
dataset_time3=dataset_time2.T
dataset_time4 = dataset_time3.reset_index() 


# In[29]:


dataset_time5=dataset_time4.pivot_table(index=['index'], values=['Caribbean small states', 'Cuba', 'Curacao', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark'])  
matplot.figure(figsize = (20,8)) # define figure size 
matplot.plot(dataset_time5.head(20))
matplot.xticks(rotation=90) # thickness rotate with 90. 
matplot.legend(['Caribbean small states', 'Cuba', 'Curacao', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark'],bbox_to_anchor =(1.0, 1.1), ncol = 1) 
# x and y label we define.
matplot.xlabel('Year')
matplot.ylabel('Comparison ') 
# define title name.
matplot.title('Urban population growth (annual %)  ') 
matplot.show() # showing graph 


# # Plotting time series graph  for Agricultural land (% of land area)

# In[30]:


# We are extracting data for Agricultural land.
dataset_time6= df1[df1['Indicator Name']=='Agricultural land (% of land area)']  
dataset_time7=dataset_time6.set_index("Country Name") 
dataset_time8=dataset_time7.drop(['Country Code', 'Indicator Name', 'Indicator Code', 'Unnamed: 66'],axis=1)
dataset_time9=dataset_time8.T
dataset_time9 = dataset_time9.reset_index()


# In[31]:


dataset_time11=dataset_time9.pivot_table(index=['index'], values=['Caribbean small states', 'Cuba', 'Curacao', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark'])  
matplot.figure(figsize = (20,8)) # define figure size 
matplot.plot(dataset_time11.head(90))
matplot.xticks(rotation=90) 
matplot.legend(['Caribbean small states', 'Cuba', 'Curacao', 'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark'],bbox_to_anchor =(1.0, 1.1), ncol = 1) 
# define x and ylabels.
matplot.xlabel('Year')
matplot.ylabel('Comparison ') 
# define title name 
matplot.title('Agricultural land (% of land area)') 
matplot.show() # showing graph 


# In[31]:




