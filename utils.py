import pandas as pd
import numpy as np
import math


def get_top10_1():
    df = pd.read_excel('files/test.xlsx')
    gnmk = df["功能模块"][df['功能项'].isna()]
    gnx = df["功能项"][df['功能模块'].isna()]
    mknum = df["数量"][df["功能项"].isna()].astype(str)
    xnum = df["数量"][df["功能模块"].isna()].astype(str)
    return np.array(gnmk), np.array(gnx), np.array(mknum), np.array(xnum)


# print(get_top10_1())
