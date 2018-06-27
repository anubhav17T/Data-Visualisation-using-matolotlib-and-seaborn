#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 18:22:43 2018

@author: om
"""
#Aim- The purpose of this project is to explore data visualization techniques utilizing the Iris dataset.
#the dataset conains the sepal and petals length and width
# This project seeks to reproduce, and to visually modify the given code.

#Conclusion-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.metrics as sm
import warnings
warnings.filterwarnings("ignore")

#importing the dataset
iris = pd.read_csv('Iris.csv')
#To view Iris data below:
iris.head()
# Samples from each species
iris["Species"].value_counts()

#PART-1
# The pandas plot extenstion can be used to make a scatterplot and we have used sepallength vs sepalwidth graph
# Display your plot with plt .show
iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")
plt.show()

#To change color and size, add the following:
iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm",color="green",s=70 )
plt.show()

 #PART-2
 #Use seaborn jointplot, to make bivariate scatterplots and  histograms in one graph
sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=iris, size=5)
plt.show()

#PART-3
# Modify the graph above by assigning each species an individual color.
sns.FacetGrid(iris, hue="Species", size=5) \
   .map(plt.scatter, "SepalLengthCm", "SepalWidthCm") \
   .add_legend()
plt.show()

#PART-4
#using seaborn stripPlots
# Assing ax.axis a variable name, and insert the box number into the corresponding brackets
ax= sns.boxplot(x="Species", y="PetalLengthCm", data=iris)
ax= sns.stripplot(x="Species", y="PetalLengthCm", data=iris, jitter=True, edgecolor="gray")

boxtwo = ax.artists[2]
boxtwo.set_facecolor('red')
boxtwo.set_edgecolor('black')
boxthree=ax.artists[1]
boxthree.set_facecolor('yellow')
boxthree.set_edgecolor('black')

plt.show()

#PART-5
# seaborn's kdeplot, plots univariate or bivariate density estimates.
#Size can be changed by tweeking the value used
sns.FacetGrid(iris, hue="Species", size=5) \
   .map(sns.kdeplot, "PetalLengthCm") \
   .add_legend()
plt.show()

#PART-6
#Use pairplot to analyze the relationship between species for all characteristic combinations. 
# An observable trend shows a close relationship between two of the species
sns.pairplot(iris.drop("Id", axis=1), hue="Species", size=3)
plt.show()

#Conclusion- We have used Python to apply data visualization tools to the Iris dataset. Color and size changes were made to the data points in scatterplots 