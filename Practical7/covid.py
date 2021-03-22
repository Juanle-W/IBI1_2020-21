import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("Users/user/Downloads")
os.getcwd()
os.listdir()
covid_data=pd.read_csv("full_data.csv")
covid_data.iloc[0:11:2,:]
L=[]
for i in range (0,7996):
	if covid_data.iloc[i,1]=="Afghanistan":
		L.append(True)
	else:
		L.append(False)

covid_data.loc[L,"total_cases"]
L1 = []
for i in range (0,7996):
     if covid_data.iloc[i,1]=="World":
             L1.append(True)
     else:
             L1.append(False)

world_dates=covid_data.loc[L1,"date"]
world_new_deaths=covid_data.loc[L1,"new_deaths"]
world_new_cases=world_new_cases=covid_data.loc[L1,"new_cases"]
np.mean(world_new_cases)
np.median(world_new_cases)
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
plt.show()
plt.plot(world_dates, world_new_cases, 'b+')
plt.plot(world_dates, world_new_deaths, 'ro')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.xlabel(world_dates)
plt.show()
L2=[]
for i in range (0,7996):
	if covid_data.iloc[i,1]=="Spain":
		L2.append(True)
	else:
		L2.append(False)

Spain_new_cases=covid_data.loc[L2,"new_cases"]
Spain_total_cases=covid_data.loc[L2,"total_cases"]
Spain_dates=covid_data.loc[L2,"date"]
plt.plot(Spain_dates, Spain_new_cases, 'bo')
plt.plot(Spain_dates, Spain_total_cases, 'r+')
plt.xticks(Spain_dates.iloc[0:len(Spain_dates):4],rotation=-90)
plt.show()
 
