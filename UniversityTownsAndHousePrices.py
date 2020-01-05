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

# Cleans, formats and returns a DataFrame of towns states they are in, from the university_towns.txt file
def get_list_of_university_towns():
    uniTownsDf = pd.read_table('university_towns.txt',header=None)
    uniTownsDf.columns = ['Col1']

    # remove strings in brackets or parentheses
    uniTownsDf['Col1'] = uniTownsDf['Col1'].str.replace(r"\(.*\)","").str.strip()
    uniTownsDf['Col1'] = uniTownsDf['Col1'].str.replace(r"\[.*\]","").str.strip()

    # iterate through the file and format correctly by appending to the cleanUniTownsDf list
    state = ''
    cleanUniTownsDf = []
    for line in uniTownsDf['Col1']:
        # convert line to a string
        lineStr = str(line)
        # check that the value is a state:
        isState = lineStr in states.values()
        # if this is a state, store it, if not, add to the list
        if(isState):
            state = lineStr
        else:
            cleanUniTownsDf.append((state, lineStr))
        
    return pd.DataFrame(cleanUniTownsDf, columns=['State', 'RegionName']).head(20)

print(get_list_of_university_towns())