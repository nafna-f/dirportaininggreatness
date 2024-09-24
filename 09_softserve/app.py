# Naf, Daniel, Cliare
# ??
# SoftDev
# K09 -- Soft Serve
# 2024-09-24
# Time: N/A

# Sourced from Work #06

# flask
import random

from flask import Flask
app = Flask(__name__)

@app.route("/")

def randomOcc():
    
    with open("occupations.csv", "r") as file:
        str = file.read()
        infoByLine = str.split("\n")
    
        #split by commas
        conInfo = []
        for info in infoByLine:
            if '"' in info: # If quotation mark, only add the string starting from after that 
                info = info[1:]
                conAdd = info.split('",') # split by quotation mark and comma 
            else:
                conAdd = info.split(",")
            for i in conAdd:
                conInfo.append(i)
        conInfo.remove("Job Class") # Remove the unneeded information from csv
        conInfo.remove("Percentage")
        conInfo.remove("Total")
        conInfo.remove("99.8")
    
        jobDict = {}

        for x in range(0, len(conInfo) - 1, 2):
            jobDict[conInfo[x]] = float(conInfo[x+1])
    
        return random.choices(list(jobDict), weights=[6.1, 5.0, 2.7, 1.7, 0.9, 1.6, 0.8, 6.1, 1.7, 5.5, 2.8, 2.3, 8.3, 3.7, 4, 10.2, 15.1, 0.6, 4.3, 3.8, 6.1, 6.5])
        #^^ chooses a random key (occupation) from jobDict
    
app.debug = True
app.run()