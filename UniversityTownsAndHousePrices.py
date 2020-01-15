# By Ryan Vickramasinghe

# The following code will prove the hypothesis: "University towns have their mean housing prices less effected by recessions."
# Data is pulled from the following locations:
# - From the Zillow research data site there is housing data for the United States. In particular the datafile for all homes 
#   at a city level, City_Zhvi_AllHomes.csv, has median home sale prices at a fine grained level.
# - From the Wikipedia page on college towns is a list of university towns in the United States which has been copy and pasted 
#   into the file university_towns.txt.
# - From Bureau of Economic Analysis, US Department of Commerce, the GDP over time of the United States in current dollars 
#   (use the chained value in 2009 dollars), in quarterly intervals, in the file gdplev.xls. For this assignment, only look at
#    GDP data from the first quarter of 2000 onward.


# The following function will return

import pandas as pd
import numpy as np
import re

states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', \
    'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska',\
    'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', \
    'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', \
    'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan',\
    'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', \
    'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', \
    'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', \
    'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', \
    'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California',\
    'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', \
    'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', \
    'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

def cleanUniversityTownData():
    uniTownsDf = pd.read_table('university_towns.txt',header=None)
    uniTownsDf.columns = ['Col1']

    # iterate through the rows, and build a new DataFrame
    cleanUniTownDF = []
    state = ''
    for rawLine in uniTownsDf['Col1']:
        # check to see if line contains '[edit]', this means line is a state
        isState = 'edit' in rawLine

        # if is a state, parse as a state, store, and continue looping
        if (isState):
            state = re.sub(r'\[.*\]', '', rawLine).strip()
        # if not a state, parse and add to new DF
        else:
            newLine = re.sub(r'\[.*\]', '', rawLine).strip()
            newLine = re.sub(r'\(.*\)', '', newLine).strip()
            cleanUniTownDF.append((state, newLine))

    return pd.DataFrame(cleanUniTownDF, columns=['State', 'RegionName'])

print(cleanUniversityTownData().groupby('State').size())