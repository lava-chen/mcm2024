import pandas as pd
for i in range(2,10,2):
    print(i)

df = pd.read_excel("A1_position.xlsx")
print(df[f'{1} s'][0])
