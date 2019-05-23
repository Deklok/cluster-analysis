#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:07:08 2019

@author: Manolomon
"""

import pandas as pd
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
