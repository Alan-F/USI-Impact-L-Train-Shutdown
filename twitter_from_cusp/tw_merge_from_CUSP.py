# CUSP Jupyterhub
__author__ = "Dongjie Fan"

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import os
import csv
import yaml

fnames = os.listdir("/gws/open/SocMedia/tweets")

d = []
n = 0
for n, fn in enumerate(fnames):
    n += 1
    print "\r{:.2f}%".format(100.0*n/len(fnames)),
    name = "/gws/open/SocMedia/tweets/" + fn
    with open(name, 'r') as fi:
        reader = csv.DictReader(fi)
        try:
            for row in reader:
                if row['Geo'] != 'None' and row['Geo'] != None:
                    temp = yaml.load(row['Geo'])["u'coordinates'"]
                    row['geometry'] = Point((temp[0], temp[1]))
                    d.append(row)
        except: 
            pass
print "\n", len(d)

tw = pd.DataFrame(d)
col = [u'UserID', u'Username', u'Tweeted_At', \
	   u'Tweet ID', u'Location', u'Geo',  \
	   u'Place', u'Profile_Create_at',\
       u'Retweeted_Count', u'Text', u'geometry']
tw = tw.loc[:, col]
tw.reset_index(drop=True, inplace=True)
tw.to_csv("./tw/tw.csv")
# tw_geo = gpd.GeoDataFrame(tw, geometry=tw.geometry)
# tw_geo.to_file("./tw/tw")

tw2 = pd.read_csv("./tw/tw.csv")
tw2 = tw2.loc[:,"UserID":]
tw2.drop_duplicates(inplace=True)
tw2.to_csv("./tw/tw_without_duplication.csv")