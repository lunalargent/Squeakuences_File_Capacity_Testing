#import needed modules
import matplotlib.pyplot as plt 
import pandas as pd 
import sys
import datetime

#read in csv file and store as a dataframe
file = pd.read_csv('clean_output.csv') 
#print(file.columns)
testtime = file['Processing_Time'][0]
float(testtime)
#print(type(datetime.datetime(testtime)))
#print(testtime.total_seconds())
file.plot.scatter(x='Number_of_sequences_cleaned',y='Processing_Time')

plt.savefig("Output.pdf",format="pdf",bbox_inches="tight")


sys.exit()

x_axis = file['Number of sequences cleaned'] 
y_axis = file['Processing Time (Hours: Minutes: Seconds)'] 
plt.figure(figsize=(10,10))
plt.style.use('seaborn')
plt.scatter(x,y,marker="*",s=100,edgecolors="black",c="yellow")
plt.title("Processing Time Compared to Number of Sequences Cleaned")
plt.xlabel("Number of Sequences Cleaned") 
plt.ylabel("Processing Time (Hours:Minutes:Seconds)") 
plt.show()
