#import needed modules
import matplotlib.pyplot as plt 
import pandas as pd 
import sys
import datetime
import numpy as np
from scipy import stats

#read in csv file and store as a dataframe
file = pd.read_csv('clean_output.csv')

file["Runtime (in hours)"] = np.nan

print(file)

for index in file.index:
    temp_ind = file["Processing_Time"][index]
    #print(temp_ind)
    timelist = temp_ind.split(':')
    hours = float(timelist[0]) + float(timelist[1])/60 + float(timelist[2])/3600
    #print(hours)
    #file["Runtime"][index] = hours
    file.loc[index,"Runtime (in hours)"] = hours
#print(file)

#float(testtime)
#print(type(datetime.datetime(testtime)))
#print(testtime.total_seconds())

#Generating figure for NumSeqs versus run time
file.plot.scatter(x="Number of sequences cleaned",y="Runtime (in hours)")

plt.savefig("NumSeqs.pdf",format="pdf",bbox_inches="tight")

plt.close()

#Generating figure for Memory versus run time
file.plot.scatter(x="Memory (MB)",y="Runtime (in hours)")

plt.savefig("Memory.pdf",format="pdf",bbox_inches="tight")

plt.close()

#Generating figure for Starting File Size versus run time
x_data ="Starting File Size (MB)"
y_data="Runtime (in hours)"
file.plot.scatter(x=x_data,y=y_data)

plt.savefig("StartingFileSize.pdf",format="pdf",bbox_inches="tight")

plt.close()