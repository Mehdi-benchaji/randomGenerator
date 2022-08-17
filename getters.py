import random
import datetime
import time
import os
import configparser

# le chemin absolu du fichier
absPath = os.path.dirname(os.path.realpath(__file__))
configFile = os.path.join(absPath, 'config.conf')
data = configparser.ConfigParser()
# charger le fichier de conf
data.read(configFile)


# fonction pour obtenir les infos sur le fichier
def getFileInfo(undersection):
    field = data['fileInfos'][undersection]
    return field


# Fonctions pour la conversion des types
def date(year):
    sdate = datetime.date(int(year), 1, 1)
    # generer les timestamps
    return time.mktime(sdate.timetuple())


# retourner une liste du type souhaite
def convertTo(inData, dtype):
    return [dtype(x) for x in inData.split("-")]


# obtenir un entier aleatoire
def getRandomInt(intSet, form=""):
    start, end = convertTo(intSet, int)
    return random.randint(start, end)


# obtenir un double aleatoire
def getRandomFloat(intSet, form=""):
    start, end = convertTo(intSet, float)
    randomDouble = lambda x, y: random.uniform(x, y)
    return randomDouble(start, end)


# string aleatoire
def getRandomString(intSet, form=""):
    strings = convertTo(intSet, str)
    return random.choice(strings)


def getRandomBool(intSet, form=""):
    boolean = convertTo(intSet, str)
    return random.choice(boolean)


# decimal aleatoire
def getRandomDecimal(inDecimals, form=""):
    start, end = convertTo(inDecimals, float)
    randomDecimal = lambda x, y: random.uniform(x, y)
    return round(randomDecimal(start, end), 2)


# retourner une date aleatoire entre 2 annees (ex: entre 2002 et 2021)
def getRandomDate(dateTime, form=""):
    start, end = convertTo(dateTime, date)  # date c'est une fonction
    randomDate = random.randint(start, end)
    return datetime.datetime.fromtimestamp(randomDate).strftime(form)


def getTimestamp(dateTime, form=""):
    start, end = convertTo(dateTime, date)  # date c'est une fonction
    randomDate = random.randint(int(start), int(end))
    return datetime.datetime.fromtimestamp(randomDate).strftime(form)

'''x = getTimestamp("2000-2001","%d-%m-%Y_%H:%M:%S")
print(x)'''


# les types possibles
dataTypes = {
    'int': getRandomInt,
    'string': getRandomString,
    'boolean': getRandomBool,
    'timestamp': getTimestamp,
    'float': getRandomFloat,
    "datetime": getRandomDate
}


def getkeys(section):
    vals = []
    for key in dict(data.items(section)):
        vals.append(key)
    return vals


def getvalues(section, key):
    nom = data[section][key].split(",")
    return nom

def getsection():
    vals = []
    for section in data.sections():
            vals.append(section)
    return vals

# fonction pour obtenir/generer les ranges
def getData(fieldname):
    section=getsection()
    field = getvalues(section[0], fieldname)
    dtype = field[0]
    if dtype in dataTypes:
        return dataTypes[dtype](field[2], form=field[1])
    return field[2]