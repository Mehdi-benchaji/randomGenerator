import configparser


config = configparser.ConfigParser()


dn_last_loc_overall_d1="fichiers_conf/dn_last_loc_overall_d1.conf"

# Reading Data ([[],[],[],[]])=>([ , , , ])
def getkeys(filename, config):
    vals = []
    config.read(filename)
    for section in config.sections():
        for key in dict(config.items(section)):
            vals.append(key)
    return vals

def getsection(filename, config):
    vals = []
    config.read(filename)
    for section in config.sections():
            vals.append(section)
    return vals
def getvalues(section,key, config):
    nom=config[section][key].split()
    return nom
s=0
key=getsection(DN_PARC_PREP_D1, config)
keys = getkeys(DN_PARC_PREP_D1, config)
vl = getvalues(key[0],keys[0], config)

print(key)