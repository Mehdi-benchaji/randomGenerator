import csv
import time
from getters import *  # Importing all of functions from our library getters.py

start = time.time()
# Nom du fichier horodate
dateFile = time.strftime(getFileInfo("dateFormat"))
fileType = getFileInfo("fileType")
filename = "%s_%s.%s" % (getFileInfo("genre"), dateFile, fileType)

# les colonnes
fieldnames=getkeys("colonnes")


maxRecords = int(getFileInfo("maxRecords"))

with open(filename, 'w+', newline='') as f:
    file = csv.writer(f)
    file.writerow(fieldnames)

    for i in range(1, maxRecords):
        row = []
        for i in range(0,len(fieldnames)):
                row.append(getData(fieldnames[i]))
        file.writerow(row)
    '''for i in range(1, maxRecords):
        row = []
        for field in fieldnames:
            row.append(getData(field))
        file.writerow(row)'''



end = time.time()
print(end - start)