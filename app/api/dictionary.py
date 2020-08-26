import os
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings(action='ignore', category=FutureWarning, module='numpy')
pd.options.mode.chained_assignment = None

filepath = os.path.join(os.path.dirname(__file__), "..",
                                     "assets",
                                     "AB_NYC_2019.csv")
df = pd.read_csv(filepath)

df.rename(columns={'neighbourhood_group': 'Borough', 'neighbourhood': 'Neighbourhood', 'room_type': 'Room_type', 'minimum_nights': 'Minimum_nights', 'availability_365': 'Availability_365', 'price': 'Price'}, inplace=True)

features = ["Borough",
            "Neighbourhood",
            "Room_type",
            "Minimum_nights",
            "Availability_365"]

X = df[features]

# Factorize the Borough column and return a dictionary with the
# Brough names as keys and the number representing the Borough
# as the value
blist1 = X['Borough'].unique()

X['Borough'] = pd.factorize(X['Borough'], sort=True)[0] + 1

blist2 = X['Borough'].unique()

BoroughDict = {}
for i in range(len(blist1)):
    BoroughDict[blist1[i]] = blist2[i]

# Factorize the Neighbourhood column and return a dictionary with the
# Brough names as keys and the number representing the Neighbourhood
# as the value
nlist1 = X['Neighbourhood'].unique()

X['Neighbourhood'] = pd.factorize(X['Neighbourhood'], sort=True)[0] + 1

nlist2 = X['Neighbourhood'].unique()

NeighbourhoodDict = {}
for i in range(len(nlist1)):
    NeighbourhoodDict[nlist1[i]] = nlist2[i]

# Factorize the Room_type column and return a dictionary with the
# Brough names as keys and the number representing the Room_type
# as the value
rlist1 = X['Room_type'].unique()

X['Room_type'] = pd.factorize(X['Room_type'], sort=True)[0] + 1

rlist2 = X['Room_type'].unique()

RoomTypeDict = {}
for i in range(len(rlist1)):
    RoomTypeDict[rlist1[i]] = rlist2[i]

print(BoroughDict["Brooklyn"])
print(NeighbourhoodDict["Kensington"])
print(RoomTypeDict["Private room"])