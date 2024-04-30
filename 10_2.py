import pandas as pd

filename = "input.csv"
df = pd.read_csv(filename)  #读取csv文件

b = (df["temperature_c"].apply(lambda row: round(row*9/5) + 32))
      #apply函数对数据对象进行批量处理,后面跟lambda表达式

df['temperature_f'] = b  #添加新列

df.to_csv("output.csv")
#print(pd.read_csv("output.csv"))