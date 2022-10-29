'''
This is the start of the code for the first repo by Anton Kruse
This project aims to get an overlook of perfomances of ETF´s, including a investment strategy & to examine if the choice of my own ETF has been a good one.

We keep it first of simple and use a given "best of" from https://www.etf.com/sections/features-and-news/best-performing-etfs-year. This list shows the best performing ETF within the first half of the year 2022. Due to the market circumstances, this set includes mainly commodity and energy ETF. Since my scope is is to examine my own decision to buy certain ETF, I will and the to this set. Furtmore, the set excludes leveraged and inversed ETF´s.
'''
# import needed packages
#import pandas as pd
#import numpy as pd
import matplotlib.pyplot as plt
#import seaborn as sns
from PIL import Image

# zeige die Übersicht der ETF´s
img= Image.open("Übersicht_ETFs.png")
plt.imshow(img)

plt.show()