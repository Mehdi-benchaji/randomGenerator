import random
import datetime
import time
import os
import configparser
from dict import DICTIONNAIRE
import re
import sys

# le chemin absolu du fichier
absPath = os.path.dirname(os.path.realpath(__file__))
configFile = os.path.join(absPath, 'config.conf')
data = configparser.ConfigParser()
# charger le fichier de conf
data.read(configFile)
maxRecords = data["fileInfos"]["maxRecords"]


# fonction pour obtenir les infos sur le fichier
def getFileInfo(undersection):
    field = data['fileInfos'][undersection]
    return field


# Fonctions pour la conversion des types
def date(year):
    y=year.split("/")
    sdate = datetime.date(int(y[2]),int(y[1]),int(y[0]))
    # generer les timestamps
    return time.mktime(sdate.timetuple())
def getRandomPhone(val,form=""):
    ph_no = []
    # the first number should be in the range of 6 to 7
    ph_no.append(random.randint(6, 7))
    # the for loop is used to append the other 9 numbers.
    # the other 9 numbers can be in the range of 0 to 9.
    for i in range(1,9):
        ph_no.append(random.randint(0, 9))

    return ''.join(str(e) for e in ph_no)


# retourner une liste du type souhaite
def typeapproved(inData, dtype):
    i = 0
    y = []
    for x in inData.split("-"):
        if re.search(DICTIONNAIRE[dtype], x):
            y.append(x)
        else:
            y=print("valeur",i+1,"est incorrecte veuillez saisir un",dtype)
        i = i+1
    return y

'''# obtenir un id incrementable
def getid(num):
    increment = int(num) + 1
    return increment'''

# obtenir un entier aleatoire
def getRandomInt(intSet, form=""):
    try:
        i=typeapproved(intSet,"int")
        start=i[0]
        end=i[1]
        return random.randint(int(start), int(end))
    except:
        sys.exit("erreur int")

# obtenir un double aleatoire
def getRandomFloat(intSet, form=""):
    try:
        i = typeapproved(intSet, "float")
        start = i[0]
        end = i[1]
        randomDouble = lambda x, y: random.uniform(x, y)
        return randomDouble(float(start), float(end))
    except:
        sys.exit("erreur float")

# string aleatoire
def getRandomString(intSet, form=""):
    try:
        strings = typeapproved(intSet, "str")
        return random.choice(strings)
    except:
        sys.exit("erreur str")

# retourner une date aleatoire entre 2 annees (ex: entre 2002 et 2021)
def getRandomDate(dateTime, form=""):
    try:
        i = typeapproved(dateTime, "datetime")
        start = i[0]
        end = i[1]  # date c'est une fonction
        randomDate = random.randint(int(date(start)), int(date(end)))
        return datetime.datetime.fromtimestamp(randomDate).strftime(form)
    except:
        sys.exit("erreur date")

def getTimestamp(Time, form=""):
    try:
        i = typeapproved(Time, "timestamp")
        start,end = i[0],i[1]
        randomDate = random.randint(int(date(start)), int(date(end)))  # date c'est une fonction
        return datetime.datetime.fromtimestamp(randomDate).strftime(form)
    except:
        sys.exit("erreur getTimestamp")

def getRandomBoolean(val,form=""):
    try:
        i = typeapproved(val, "bool")
        return random.choice(i)
    except:
        sys.exit("erreur boolean")

# les types possibles
dataTypes = {
    'int': getRandomInt,
    'str': getRandomString,
    'timestamp': getTimestamp,
    'float': getRandomFloat,
    "datetime": getRandomDate,
    "bool":getRandomBoolean,
    "num":getRandomPhone}

# fonction pour obtenir les cles
def getkeys(section):
    vals = []
    for key in dict(data.items(section)):
        vals.append(key)
    return vals
# fonction pour obtenir les vals des cles
def getvalues(section, key):
    nom = data[section][key].split(",")
    return nom
# fonction pour obtenir les sections
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