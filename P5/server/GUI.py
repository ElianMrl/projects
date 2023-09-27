from tkinter import *
from tkinter import ttk
import tkinter.font as font
import pickle
import json
import numpy as np

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
    prediction = abs(round(__model.predict([x])[0],2))
    label(prediction)

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

def label(prediction):
    txtResult = Label(frame3, text=prediction, bg='white')
    txtResult.grid(row=0, column=1, padx=10, pady=10)

win = Tk()
win.geometry("400x500+0+0")

# Add image file
bg = PhotoImage(file="image.png")

# Show image using label
label1 = Label(win, image=bg)
label1.place(x=0, y=0)

house_size = StringVar()
Bedrooms = StringVar()
Bathrooms = StringVar()
Result = StringVar()
ZipCode = StringVar()
Result = StringVar()

frameL1 = LabelFrame(win, text="Enter House Details", font="Times 13 bold")
frameL1.pack(padx=10, pady=10, fill="both", expand='yes')

frame1L2 = LabelFrame(win, text="Predictions", font="Times 13 bold")
frame1L2.pack(padx=10, pady=10, fill="both", expand='yes')

frame2 = Frame(frameL1)
frame2.grid(row=0, column=0)

frame3 = Frame(frame1L2)
frame3.grid(row=1, column=0)

lblHouseSize = Label(frame2, text='House Size (Square Feet)', font='lucida 8 bold')
lblHouseSize.grid(row=0, column=0, padx=10, pady=10)
HouseSize = Entry(frame2, textvariable=house_size)
HouseSize.grid(row=0, column=1, padx=10, pady=10)

lblBedrooms = Label(frame2, text='Bedrooms', font='lucida 8 bold')
lblBedrooms.grid(row=1, column=0, padx=10, pady=10)
txtBedrooms = Entry(frame2, textvariable=Bedrooms)
txtBedrooms.grid(row=1, column=1, padx=10, pady=10)

lblBathrooms = Label(frame2, text='Bathrooms', font='lucida 8 bold')
lblBathrooms.grid(row=2, column=0, padx=10, pady=10)
txtBathrooms = Entry(frame2, textvariable=Bathrooms)
txtBathrooms.grid(row=2, column=1, padx=10, pady=10)

predLabel = Label(frame3, text='Estimation:', font='lucida 8 bold')
predLabel.grid(row=0, column=0, padx=10, pady=10)
txtResult = Label(frame3, text='                       ', bg='white')
txtResult.grid(row=0, column=1, padx=10, pady=10)

load_saved_artifacts()
Label(frame2, text="Select zip code", font='lucida 8 bold').grid(row=3, column=0, padx=10, pady=10)
mycombo = ttk.Combobox(frame2, textvariable=ZipCode, width=30)
mycombo['values'] = get_zip_code() # I should change this to the column with zipcodes
mycombo.grid(row=3, column=1, padx=10, pady=10)

def add():
    hs = float(house_size.get())
    bed = float(Bedrooms.get())
    bath = float(Bathrooms.get())
    zip = float(ZipCode.get())
    Result.set(get_estimated_price(zip, hs, bed, bath))

esButton = Button(frame2, font='lucida 8 bold')
esButton['text'] = 'Estimate Price'
esButton['command'] = add
esButton.grid(row=4, column=0, padx=10, pady=10)

win.geometry("450x500")
win.title("House Price Prediction")

win.mainloop()