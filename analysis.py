#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:07:08 2019

@author: Manolomon
"""

import math
import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt

data = pd.read_csv('alumnos.csv')

def normalize(df, min_value, max_value):
    result = df.copy()
    result= (df - min_value) / (max_value - min_value)
    return result * 100

group_1 = pd.concat([
    normalize(data['Estatura'], 1.5, 2.0),
    normalize(data['peso'], 40, 100),
    normalize(data['calzado'], 20, 30)
    ], axis=1, sort=False)

group_2 = pd.concat([
    normalize(data['promedio'], 6, 10),
    normalize(data['materiasRepite'], 0, 10),
    normalize(data['dinero'], 0, 4000)
    ], axis=1, sort=False)

group_3 = pd.concat([
    normalize(data['nHermanos'], 0, 10),
    normalize(data['dinero'], 0, 4000),
    normalize(data['edad'], 15, 30)
    ], axis=1, sort=False)
    
def calculateDistance(pointA, pointB):
    return math.sqrt(
            (pointA[0]-pointB[0])**2 +
            (pointA[1]-pointB[1])**2 +
            (pointA[2]-pointB[2])**2)

def calculateNewCentroid(dataCentroid):
    meanValues = dataCentroid.mean()
    return [meanValues[0],meanValues[1],meanValues[2]]
    
def cluster2K(data):
    centroidA = np.random.randint(0,15)
    centroidB = np.random.randint(0,15)
    centroidA = data.iloc[centroidA].values
    centroidB = data.iloc[centroidB].values
    
    data["Clase"] = ""
    print("Centroid A")
    print(centroidA)
    print("Centroid B")
    print(centroidB)
    while True:
        for i in range(0,15):
            if calculateDistance(data.iloc[i].values, centroidA) > calculateDistance(data.iloc[i].values, centroidB):
                data.loc[i,["Clase"]] = "B"
            else:
                data.loc[i,["Clase"]] = "A"
        print(data)
        newCentroidA = calculateNewCentroid(data.iloc[:][data.Clase == "A"])
        newCentroidB = calculateNewCentroid(data.iloc[:][data.Clase == "B"])
        print(newCentroidA)
        print(newCentroidB)
        if np.array_equal(newCentroidA,centroidA) and np.array_equal(newCentroidB,centroidB):
            break
        else:
            centroidA = newCentroidA
            centroidB = newCentroidB
    print("End of 2K centroids")        
    
def cluster3K(data):
    centroidA = np.random.randint(0,15)
    centroidB = np.random.randint(0,15)
    centroidC = np.random.randint(0,15)
    centroidA = data.iloc[centroidA].values
    centroidB = data.iloc[centroidB].values
    centroidC = data.iloc[centroidC].values
    
    data["Clase"] = ""
    print("Centroid A")
    print(centroidA)
    print("Centroid B")
    print(centroidB)
    print("Centroid C")
    print(centroidC)
    while True:
        for i in range(0,15):
            distanceA = calculateDistance(data.iloc[i].values, centroidA)
            distanceB = calculateDistance(data.iloc[i].values, centroidB)
            distanceC = calculateDistance(data.iloc[i].values, centroidC)
            distances = [distanceA, distanceB, distanceC]
            if min(distances) == distanceA:
                data.loc[i,["Clase"]] = "A"
            elif min(distances) == distanceB:
                data.loc[i,["Clase"]] = "B"
            elif min(distances) == distanceC:
                data.loc[i,["Clase"]] = "C"
        print(data)
        newCentroidA = calculateNewCentroid(data.iloc[:][data.Clase == "A"])
        newCentroidB = calculateNewCentroid(data.iloc[:][data.Clase == "B"])
        newCentroidC = calculateNewCentroid(data.iloc[:][data.Clase == "C"])
        print(newCentroidA)
        print(newCentroidB)
        print(newCentroidC)
        if (np.array_equal(newCentroidA,centroidA) and np.array_equal(newCentroidB,centroidB) and np.array_equal(newCentroidC,centroidC)):
            break
        else:
            centroidA = newCentroidA
            centroidB = newCentroidB
            centroidC = newCentroidC
    print("End of 3K centroids")

cluster2K(group_1)
cluster3K(group_1)