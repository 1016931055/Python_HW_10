import pandas as pd

# 读取 input.csv 文件
df = pd.read_csv("input.csv")

# 使用分组和 nunique() 方法统计每个 "Номер борта" 的唯一值数量
result = df.groupby('Номер борта').size().reset_index(name='Уникальных маршрутов')

# 按照 'Уникальных маршрутов' 和 'Номер борта' 进行排序
result = result.sort_values(by=['Уникальных маршрутов', 'Номер борта'], ascending=[False, True])

# 将结果写入 output.csv 文件
result.to_csv("output.csv", index=False, encoding="utf8")