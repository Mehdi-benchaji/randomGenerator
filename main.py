import csv
import time
from getters import * # Importing all of functions from our library getters.py
import os
import traceback

# Nom du fichier horodaté
dateFile = time.strftime(getFileInfo("dateFormat"))
fileType = getFileInfo("fileType")
filename = "%s_%s.%s" % (getFileInfo("genre"), dateFile, fileType)

# le nombre d'enregistrement à partir de la section FileInfo
maxRecords = int(getFileInfo("maxRecords"))

with open(filename, 'w', newline='') as f:
    file = csv.writer(f)
    file.writerow(fieldnames)
    current_id = 1
    try:
        for i in range(1, maxRecords):
            row = [current_id]
            for field in fieldnames:
                row.append(getData(field))
            file.writerow(row)
            current_id += 1
        print("csv created successfuly")
    except:
        os.remove(filename) # Remove file if any error occurs
        traceback.print_exc()
