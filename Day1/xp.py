import numpy as np
import pandas as pd
import matplotlib.pyplot as pl

# # 1

# def num_arr(start):
#     arr = np.arange(start=start, stop=100, step=4)
#     return arr
# num_arr(6)
#
# print(num_arr(6))

# # 2

# a = np.array([1,2,3,np.nan,5,6,7,np.nan])
# a = a[~np.isnan(a)]
# print(a)


# # 3

from random import random

# array_rand = np.random.randint(101, size=5*6).reshape((5,6))
# print(array_rand)


# # 4

# series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
# print(series.unique())
#
# print(series.value_counts())


# # 5

from dateutil.parser import parse

# data = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])
# for x in data:
#     print(parse(x).month, parse(x).day, parse(x).weekday())


# # 6

# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
# print(df)

# print(df.shape[1])

# df_changename = df.rename(columns={"Type":"TypeOfCar"})
# print(df_changename)

# print(df.isnull().sum())

# print(df.isnull().sum().max())


# # 7

# del df["EngineSize"]
# del df["Length"]
# df.drop('EngineSize', inplace=True, axis=1)
# df.drop('Length', inplace=True, axis=1)


# # 8

# df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
#                     'weight': ['high', 'medium', 'low'] * 3,
#                     'price': np.random.randint(0, 15, 9)})
#
# df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
#                     'kilo': ['high', 'low'] * 3,
#                     'price': np.random.randint(0, 15, 6)})

# print(df1)
# print(df2)

# remov_dup = df1.merge(df2,left_on=('fruit','weight'),right_on=('pazham','kilo'),how='inner',suffixes=('_left','_right')).head(10)
# print(remov_dup)


# # 9

import pandas as pd

# df = pd.DataFrame(["STD,City\tState",
# "33,Kolkata\tWest Bengal",
# "44,Chennai\tTamil Nadu",
# "40,Hyderabad\tTelengana",
# "80,Bangalore\tKarnataka"], columns=['row'])
# print(df)

# df = pd.DataFrame(["STD, City    State",
# "33, Kolkata    West Bengal",
# "44, Chennai    Tamil Nadu",
# "40, Hyderabad    Telengana",
# "80, Bangalore    Karnataka"], columns=['row'])
# out = pd.DataFrame(df.row.str.split(' ',2).tolist(),columns=['STD','City','State'])
# out.drop(index=0,inplace=True)
# print(out)

import matplotlib.pyplot as plt
#
# names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
# df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)
# # print(df_mpg)
#
#
# # # 10
#
# def scatter_plot(df):
#     plt.scatter(df['displacement'], df['acceleration'])
#     plt.xlabel('displacement cm³')
#     plt.ylabel('acceleration m/s²')
#     plt.grid()
#
#
# (scatter_plot(df_mpg))
#
#
# def bar_plot(df):
#     plt.figure(figsize=(12,5))
#     plt.bar(df['model_year'], df['cylinders'])
#     plt.xlabel("Model Year")
#     plt.ylabel("Cylinders")
#     plt.title("Cylinders over Years")
#     plt.show()
#
# (bar_plot(df_mpg))
#
#
# def line_plot(df):
#     x = (df['model_year'])
#     y = (df['weight'])
#     plt.plot(x, y)
#
#     plt.xlabel('model year')
#     plt.ylabel('weight')
#     plt.show()
#
#
# line_plot(df_mpg)
#
#
# def my_func(df):
#     x = (df['weight'])
#     y = (df['mpg'])
#     plt.scatter(x, y)
#
#     plt.xlabel('weight')
#     plt.ylabel('mpg')
#     plt.show()
#
#
# my_func(df_mpg)