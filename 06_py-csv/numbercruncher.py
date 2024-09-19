# Naf (Nafiyu Murtaza), Tim (Tim NG)
# Tinfoils
# SoftDev
# K06 -- CSV
# 2024-09-19
# Time: N/A

def randomOcc(str):
    
    infoByLine = str.split("\n")
    
    #split by commas
    conInfo = []
    for info in infoByLine:
        if '"' in info:
            info = info[1:]
            conAdd = info.split('",')
        else:
            conAdd = info.split(",")
        for i in conAdd:
            conInfo.append(i)
    conInfo.remove("Job Class")
    conInfo.remove("Percentage")
    
    jobDict = {}
    
    print(conInfo)

with open("occupations.csv", "r") as file:
    f = file.read()
    randomOcc(f)
