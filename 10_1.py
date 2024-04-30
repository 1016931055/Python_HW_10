import numpy as np
import pandas as pd

filename = "input.csv"
data_file = pd.read_csv(filename)
data_file.dropna(subset=['name'], inplace=True) #删除name列的NaN
column_name = "score"
column = data_file[column_name].mean()

data_file.fillna(column, inplace = True)  #填补NaN

data_file.to_csv("output.csv") #结果输出到"output.csv"
#print(pd.read_csv("output.csv"))
