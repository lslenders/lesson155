# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 08:55:59 2016

@author: J&L - Team Puma
"""
import os
import osgeo.ogr, osgeo.osr
import geocoder
import munpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import shapefile
#Set working directory
os.getcwd()
os.chdir("/home/user/Desktop/geoscripting/lesson15")
os.getcwd()

# Create output file
output = "./output"
if not os.path.exists(output):
    os.makedirs(output)

## WRITE TO SHAPEFILE
out_file = './output/Places.shp'

#create exmpty lists for coordinates
long=[]
lat=[]
city=[]

#Read city names from text file 
with open("cities.csv", "rb") as input_csv:    
    reader = csv.reader(input_csv, delimiter=',')
    for i in reader:
        city +=(i)
city


for i in city:
    g = geocoder.google(str(i))
    lat.append(g.latlng[0])
    long.append(g.latlng[1])

city
lat
long

shapefile.writer(CityLoc.shp, 'w')