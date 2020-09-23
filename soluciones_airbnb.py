# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:28:24 2020

@author: hp
"""


import numpy as np
import pandas as pd


airbnb = pd.read_csv("RUTA DONDE GUARDASTE TU ARCHIVO/airbnb_cdmx.csv")

print(airbnb.head())

#%%

print(airbnb.columns)

#%%

problema_2 = airbnb[(airbnb["id"] == 43856289) | (airbnb["id"] == 107078)]

#%%

'''
minimo_noches_disponibles == 6 

Num_habitaciones >= 2
Num_criticas > 10
puntuacion > 4

Se debe ordenar de mayor a menor puntuacion. En caso de empate, ordenar por
num_criticas descendiente

'''

alicia = airbnb[((airbnb["maximum_nights"] >= 6) & (airbnb["minimum_nights"] <=6)) \
   & (airbnb["bedrooms"] >=2) & (airbnb["number_of_reviews"] > 10) \
   & (airbnb["review_scores_accuracy"] > 4)].sort_values(by = ["review_scores_accuracy","number_of_reviews"], \
                                                             ascending = [False,False])


problema2 = alicia.head(round(alicia.shape[0]/3))


df = airbnb[(airbnb["maximum_nights"] < 5) & (airbnb["minimum_nights"] >= 3)]

'''
6 esté en [min,max]
'''







