import pandas as pd
import openpyxl
from pandas.core.frame import DataFrame

df = pd.read_excel("revisedGenshinStats.xlsx")


elementDistrib = [0, 0, 0, 0]
weaponDistrib = [0, 0, 0, 0]
regionDistrib = [0, 0, 0, 0]
genderDistrib = [0, 0, 0, 0]

#element stats
#in format [5 star, 4 star Male, Female]
elements = {"Pyro": [0, 0, 0, 0], "Cryo": [0, 0, 0, 0], "Hydro": [0, 0, 0, 0], "Electro": [0, 0, 0, 0], "Anemo": [0, 0, 0, 0], "Geo": [0, 0, 0, 0]}
for i in elements:
    for x in range(len(df)):
        if df.iloc[x, 2] == i:
            if df.iloc[x, 4] == 5:
                elements[i][0] = elements[i][0] + 1
            if df.iloc[x, 4] == 4:
                elements[i][1] = elements[i][1] + 1
            if df.iloc[x, 6] == "Male":
                elements[i][2] = elements[i][2] + 1
            if df.iloc[x, 6] == "Female":
                elements[i][3] = elements[i][3] + 1
dfElem = DataFrame(data= elements, index=["5 star", "4 star", "Male", "Female"])
print(dfElem)
dfElem.to_excel("elementStats.xlsx")
#weapon stats
#in format [5 star, 4 star Male, Female]
weapons = {"Sword": [0, 0, 0, 0], "Claymore": [0, 0, 0, 0], "Lance": [0, 0, 0, 0], "Bow": [0, 0, 0, 0], "Catalyst": [0, 0, 0, 0]}
for i in weapons:
    for x in range(len(df)):
        if df.iloc[x, 3] == i:
            if df.iloc[x, 4] == 5:
                weapons[i][0] = weapons[i][0] + 1
            if df.iloc[x, 4] == 4:
                weapons[i][1] = weapons[i][1] + 1
            if df.iloc[x, 6] == "Male":
                weapons[i][2] = weapons[i][2] + 1
            if df.iloc[x, 6] == "Female":
                weapons[i][3] = weapons[i][3] + 1
dfWeap = DataFrame(data= weapons, index=["5 star", "4 star", "Male", "Female"])

print(dfWeap)
dfWeap.to_excel("weaponStats.xlsx")