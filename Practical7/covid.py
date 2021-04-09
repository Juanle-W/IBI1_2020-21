#import some python libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/user/Downloads") #change the working directory to where the file "full_data.csv" is stored
os.getcwd() #similar function as pwd in Unix system
os.listdir() #similar function as ls in Unix system
covid_data=pd.read_csv("full_data.csv") #use Pandas library to read the content of the .csv file
covid_data.iloc[0:11:2,:] #access values for row 0, 2, 4, 6, 8, 10 and all columns

L=[] #set an empty list 
for i in range (0,7996):
	if covid_data.iloc[i,1]=="Afghanistan":
		L.append(True) #use a Boolean to access entries
	else:
		L.append(False) #so that we can get values for Afghanistan

covid_data.loc[L,"total_cases"] #show the total cases of Afghanistan
L1 = []
for i in range (0,7996):
     if covid_data.iloc[i,1]=="World":
             L1.append(True)
     else:
             L1.append(False) #so that we can get values for world range

world_dates=covid_data.loc[L1,"date"] #make an object called "world_dates" to store dates for the entire world
world_new_deaths=covid_data.loc[L1,"new_deaths"] #make an object to store the data on new deaths for the entire world
world_new_cases=world_new_cases=covid_data.loc[L1,"new_cases"] #make an object to store tha data on new cases for the entire world
np.mean(world_new_cases) #use numpy library to get the mean of tha data stored in "world_new_cases"
np.median(world_new_cases) #use numpy library to get the median of the data stored in "world_new_cases"

#make a boxplot for world_new_cases
score = world_new_cases
plt.boxplot(score,
             vert = True,
             whis = 1.5,
             patch_artist = True,
             meanline = False,
             showbox = True,
             showcaps = True,
             showfliers = True,
             notch = False
             )
#label x and y axises
plt.xlabel('world_dates')
plt.ylabel('world_new_cases')
plt.title('worldwide situation')
plt.show()

#plot both new cases and new deaths for the entire world in one graph
plt.plot(world_dates, world_new_cases, 'y-', label='world new cases')
plt.plot(world_dates, world_new_deaths, 'g-', label='world new deaths')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.xlabel('world_dates')
plt.ylabel('human_number')
plt.legend()
plt.title('new cases and new deaths for the entire world')
plt.show()

#try to answer the question by using Boolean
L2=[]
for i in range (0,7996):
	if covid_data.iloc[i,1]=="Spain":
		L2.append(True)
	else:
		L2.append(False) #so that we can select the data only for Spain

Spain_new_cases=covid_data.loc[L2,"new_cases"] #make an object to store new cases of Spain
Spain_total_cases=covid_data.loc[L2,"total_cases"] #make an object to store total cases of Spain
Spain_dates=covid_data.loc[L2,"date"] #make an object to store dates of Spain

#plot new cases and total cases of Spain in one graph
plt.plot(Spain_dates, Spain_new_cases, 'r-', label='Spain new cases')
plt.plot(Spain_dates, Spain_total_cases, 'y-', label='Spain total cases')
plt.xticks(Spain_dates.iloc[0:len(Spain_dates):4],rotation=-90)
plt.xlabel('Spain_dates')
plt.ylabel('human_number')
plt.legend()
plt.title('new cases and total cases of Spain')
plt.show()
 
