import csv
import time
from getters import * # Importing all of functions from our library getters.py
import os
import traceback

start = time.time()
# Nom du fichier horodaté
dateFile = time.strftime(getFileInfo("dateFormat"))
fileType = getFileInfo("fileType")
filename = "%s_%s.%s" % (getFileInfo("genre"), dateFile, fileType)

# les colonnes
section=getsection()
fieldnames=getkeys(section[0])


maxRecords = int(getFileInfo("maxRecords"))

with open(filename, 'w+', newline='') as f:
    file = csv.writer(f)
    file.writerow(fieldnames)

    for j in range(0, maxRecords):
        row = []
        for i in range(0,len(fieldnames)):
            if fieldnames[i]=="id":
                row.append(int(getData(fieldnames[i]))+j)
            else:
                row.append(getData(fieldnames[i]))
        file.writerow(row)

end = time.time()
print("CSV généré en "+ str(end - start) +" secondes")