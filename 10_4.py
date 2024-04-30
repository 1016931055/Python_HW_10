import pandas as pd

filename = "input.csv"

df = pd.read_csv(filename)

outfilename = "output.csv"
if(len(df) != 0):
    for i in range(len(df)):
        if (df.at[i,"Тип операции"] == "Вывоз"):
            #更改df单元格的值
            df.at[i,"Объем груза"] *= -1
    #去掉Тип операции列
    df.drop(["Тип операции"],axis = 1, inplace = True)

    #按照Фамилия водителя合并相同的，并将Объем груза相加
    merged_df = df.groupby('Фамилия водителя', as_index = False)['Объем груза'].sum()

    #根据Объем груза大小排序
    merged_df.sort_values(by = 'Объем груза', inplace = True, ascending = False)
    #print(merged_df)

                                  #不包含merged_df的索引列
    merged_df.to_csv(outfilename, index = False)
    out = pd.read_csv(outfilename)
    #print(out)
else:
    df.drop(["Тип операции"],axis = 1, inplace = True)
    df.drop(["ID"],axis = 1, inplace = True)
    df.to_csv(outfilename, index = False)