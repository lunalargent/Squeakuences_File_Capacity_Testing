#%%
import matplotlib.pyplot as plt 
import pandas as pd 
file = pd.read_excel('output.xlsx') 
x_axis = file['Number of sequences cleaned'] 
y_axis = file['Processing Time (Hours: Minutes: Seconds)'] 
plt.bar(x_axis, y_axis, width=5) 
plt.xlabel("Number of Sequences Cleaned") 
plt.ylabel("Processing Time (Hours:Minutes:Seconds)") 
plt.show()