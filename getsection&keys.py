import configparser


config = configparser.ConfigParser()


filename="config.conf"
config.read(filename)
# Reading Data ([[],[],[],[]])=>([ , , , ])
def getkeys():
    vals = []
    for section in config.sections():
        for key in dict(config.items(section)):
            vals.append(key)
    return vals

def getsection():
    vals = []
    for section in config.sections():
            vals.append(section)
    return vals
def getvalues(section,key):
    nom=config[section][key].split()
    return nom
s=0
key=getsection()
keys = getkeys()
vl = getvalues(key[0],keys[0])

print(keys)