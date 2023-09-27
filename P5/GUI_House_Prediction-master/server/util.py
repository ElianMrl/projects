import pickle
import json
import numpy as np
from tkinter import *

__zipcode = None
__data_columns = None
__model = None

def get_estimated_price(zipcode,sqft,bed,bath):
    try:
        loc_index = __data_columns.index(float(zipcode))
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = bed
    x[1] = bath
    x[2] = sqft
    if loc_index>=0:
        x[loc_index] = 1

    return abs(round(__model.predict([x])[0],2))

def get_zip_code():
    return __zipcode

def load_saved_artifacts():
    global  __data_columns
    global __zipcode
    global __model

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __zipcode = __data_columns[3:]

    with open('./artifacts/house_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_zip_code())
    print(get_estimated_price(1001.0,1000, 1, 1))
    print(get_estimated_price(1001.0,2000, 2, 2))
    print(get_estimated_price(1013.0,1000, 2, 2))
    print(get_estimated_price(19802.0,1000, 2, 2))
