import pandas as pd

data = {
    "name": ["张飞", "关羽", "刘备"],
    "age": [32, 36, 45],
    "province": ["四川阆中", "山西", "河北"],
    "nickname": ["张翼德", "关云长", "刘玄德"]
}
df = pd.DataFrame(data)
df.to_csv("pandas_to_csv.csv", index=False, encoding="utf-8")
df.to_excel("pandas_to_csv.xlsx", index=False)

# print(pd.read_csv("pandas_to_csv.csv"))

print(pd.read_excel("pandas_to_csv.xlsx", sheet_name="Sheet1"))
