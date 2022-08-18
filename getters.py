import random
import datetime
import time
import decimal
import os
from configparser import ConfigParser

# le chemin absolu du fichier
absPath = os.path.dirname(os.path.realpath(__file__))
configFile = os.path.join(absPath, 'config.conf')
data = ConfigParser()
# charger le fichier de conf
data.read(configFile)

# fonction pour obtenir les infos sur le fichier
def getFileInfo(undersection):
    field = data['fileInfos'][undersection]
    return field

# Fonctions pour la conversion des types

def date(year):
    sdate = datetime.date(int(year),1,1)
    # generer les timestamps
    return time.mktime(sdate.timetuple())

# retourner une liste du type souhaite
def convertTo(inData, dtype):
    return [dtype(x) for x in inData.split()]

# retourner une date aleatoire entre 2 annees (ex: entre 2002 et 2021)
def getRandomDate(dateTime,form=""):
    start , end = convertTo(dateTime,date) # date c'est une fonction
    randomDate =random.randint(start, end)
    return datetime.datetime.fromtimestamp(randomDate).strftime(form)

# obtenir un entier aleatoire
def getRandomInt(intSet,form=""):
    start , end = convertTo(intSet, int)
    return random.randint(start, end)

# list aleatoire
def getRandomSample(inSet, number=2,form=""):
    return random.sample(inSet.split(), number)

# string aleatoire
def getRandomString(intSet,form=""):
    strings = convertTo(intSet, str)
    return random.choice(strings)

# decimal aleatoire
def getRandomDecimal(inDecimals, form=""):
    start , end = convertTo(inDecimals, int)
    randomDecimal = lambda x,y : float(decimal.Decimal(random.randrange(x,y))/100)
    return randomDecimal(start, end)

# timestamp aleatoire
def getTimestamp(dateTime,form=""):
    start , end = convertTo(dateTime, int)
    randomDate =random.randint(start, end)
    return datetime.datetime.fromtimestamp(randomDate).strftime(form)


# les types possibles
dataTypes = {'int': getRandomInt,
             'string': getRandomString,
             'timestamp': getTimestamp,
             'decimal': getRandomDecimal,
             "datetime": getRandomDate,
             'list': getRandomSample
             }

# fonction pour obtenir/generer les ranges
def getData(fieldname):
    field = data[fieldname]
    dtype = field['type']
    if dtype in dataTypes:
        return dataTypes[dtype](field['values'],form=field['format'])
    return field['values']

sectionName = list(data.sections())
fieldnames = list(data[sectionName[0]].keys())


print(fieldnames)