import pandas as pd

df = pd.read_csv('input.csv')

# 检查文件是否为空
if not df.empty:
    # 创建一个新列，合并出发城市和到达城市
    df['Маршрут'] = df['Город отправления'] + ' - ' + df['Город прибытия']

    # 计算每个飞机编号的唯一航线数量
    summary = df.groupby('Номер борта')['Маршрут'].nunique()

    # 将Series转换为DataFrame并排序
    result = summary.reset_index()
    result.columns = ['Номер борта', 'Уникальных маршрутов']
    result = result.sort_values(by=['Уникальных маршрутов', 'Номер борта'], ascending=[False, True])
else:
    # 如果输入文件为空，则创建一个带有必要标头的空 DataFrame
    result = pd.DataFrame(columns=['Номер борта', 'Уникальных маршрутов'])

# 结果保存到文件中
result.to_csv('output.csv', encoding='utf8', index=False)
