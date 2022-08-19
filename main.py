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

# le nombre d'enregistrement à partir de la section FileInfo
maxRecords = int(getFileInfo("maxRecords"))

with open(filename, 'w', newline ='') as f:
    file = csv.writer(f)
    file.writerow(fieldnames)
    try:
        for i in range (0,maxRecords+1) :
            row = []
            for field in fieldnames:
                row.append(getData(field))
            file.writerow(row)
    except:
        os.remove(filename) # Remove file if any error occurs
        traceback.print_exc()

end = time.time()
print("CSV généré en "+ str(end - start) +" secondes")