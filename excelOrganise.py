import pandas as pd
import xlrd
import openpyxl

df = pd.read_excel("Genshin Statistics.xlsx")


startingCharIndex = 2
endingCharIndex = 33
print(df.iloc[endingCharIndex, 0])
characterLst = []
elementLst = []
weaponLst = []
starsLst = []
regionLst = []
genderLst = []

for i in range(startingCharIndex, endingCharIndex + 1):
    character = df.iloc[i, 0]
    characterLst.append(character)
    element = None
    if df.iloc[i, 1] == 1:
        element = "Pyro"
    if df.iloc[i, 2] == 1:
        element = "Cryo"
    if df.iloc[i, 3] == 1:
        element = "Hydro"
    if df.iloc[i, 4] == 1:
        element = "Electro"
    if df.iloc[i, 5] == 1:
        element = "Anemo"
    if df.iloc[i, 6] == 1:
        element = "Geo"
    elementLst.append(element)
    weapon = None
    if df.iloc[i, 8] == 1:
        weapon = "Sword"
    if df.iloc[i, 9] == 1:
        weapon = "Claymore"
    if df.iloc[i, 10] == 1:
        weapon = "Lance"
    if df.iloc[i, 11] == 1:
        weapon = "Bow"
    if df.iloc[i, 12] == 1:
        weapon = "Catalyst"
    weaponLst.append(weapon)
    stars = None
    if df.iloc[i, 14] == 1:
        stars = 5
    if df.iloc[i, 15] == 1:
        stars = 4
    starsLst.append(stars)
    region = None
    if df.iloc[i, 17] == 1:
        region = "Mondstadt"
    if df.iloc[i, 18] == 1:
        region = "Liyue"
    regionLst.append(region)
    gender = None
    if df.iloc[i, 20] == 1:
        gender = "Male"
    if df.iloc[i, 21] == 1:
        gender = "Female"
    genderLst.append(gender)

dfNew = {"character": characterLst, "element": elementLst, "weapon": weaponLst, "stars": starsLst, "region": regionLst, "gender": genderLst}

dfPan = pd.DataFrame(data = dfNew)
print(dfPan)
dfPan.to_excel("revisedGenshinStats.xlsx")