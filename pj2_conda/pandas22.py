import pandas as pd 
from numpy import NaN, nan, NAN
import numpy as np

# 과제 (20-12-31)
# CATEGORY를 코드번호, 코드명으로 분리
df = pd.read_csv('data/h.csv')
df = df[df['CATEGORY'].notnull()]

df['CODE'] = df['CATEGORY'].str.findall('[1-9][a-z]?')
df['CODE'] = df['CODE'].apply(lambda x: ', '.join(map(str, x)))

dic = {
    '1':'Urgences | Emergency', 
    '1a': 'Highly vulnerable',
    '1b': 'Urgence medicale | Medical Emergency',
    '1c': 'Personnes prises au piege | People trapped',
    '1d': 'Incendie | Fire',
    '2': 'Urgences logistiques | Vital Lines',
    '2a': "Penurie d'aliments | Food Shortage",
    '2b': "Penurie d'eau | Water shortage",
    '2c': 'Probleme de securite | Security Concern',
    '2d': 'Refuge | Shelter needed',
    '2e': 'Penurie de carburant | Fuel shortage',
    '2f': 'Sans courant | Power Outage',
    '3': 'Public Health',
    '3a': 'Infectious human disease',
    '3b': 'Chronic care needs',
    '3c': 'Besoins en materiels et medicaments | Medical equipment and supply needs',
    '3d': "OBGYN/Women's Health",
    '3e': 'Psychiatric need',
    '4': 'Menaces | Security Threats',
    '4a': 'Pillage | Looting',
    '4c': 'Group violence',
    '4e': 'Assainissement eau et hygiene | Water sanitation and hygiene promotion',
    '5': 'Infrastructure Damage',
    '5a': 'Structure effondres | Collapsed structure',
    '5b': 'Structures a risque | Unstable Structure',
    '5c': 'Route barree | Road blocked',
    '5d': 'Compromised bridge',
    '5e': 'Communication lines down',
    '6': 'Natural Hazards',
    '6a': 'Deces | Deaths',
    '6b': 'Personnes Disparues | Missing Persons',
    '6c': 'Demandant de transmettre un message | Asking to forward a message',
    '6c': 'Seisme et repliques | Earthquake and aftershocks',
    '7': 'Secours | Services Available',
    '7a': "Distribution d'aliments | Food distribution point",
    '7b': "Distribution d'eau | Water distribution point",
    '7c': 'Denrees non alimentaires | Non-food aid distribution point',
    '7d': 'Services de sante | Hospital/Clinics Operating',
    '7g': 'Morgue | Human remains management',
    '7h': 'Deblayage de gravats | Rubble removal',
    '8': 'Autre | Other',
    '8a': 'IDP concentration',
    '8c': 'Price gouging',
    '8d': 'Recherche et sauvetage | Search and Rescue',
    '8e': 'Nouvelles de Personnes | Persons News',
    '8f': 'Other'
    }

list = list(dic.keys())

def getCodename(x):
    x = x.split(",")
    cn = ''
    for i in range(len(x)):
        for j in range(len(list)):
            x[i]=x[i].strip()
            if list[j] == x[i]:
                cn = cn+''+ dic[x[i]] 
    return cn

df['CODENAME'] = df['CODE'].apply(getCodename)
df = df.drop('CATEGORY', axis=1)
print(df)
