import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def ReadCSV(fName=None):
    csvShape = []
    csvHead = []
    csvTail = []
    if fName == "" or fName == None:
        dir = os.getcwd()
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(".csv"):
                    data = pd.read_csv(file)
                    csvShape = csvShape + data.shape
                    csvHead = csvHead + data.Head()
                    csvTail = csvTain + data.Tail()
                    #print("Shape of {0} = {1}".format(file, data.shape))  
    else:
        data = pd.read_csv(fName) 
        #print("Shape of {0} = {1}".format(fName, data.shape)) 
        csvShape = csvShape + data.shape
        csvHead = csvHead + data.Head()
        csvTail = csvTain + data.Tail()
    return csvShape, csvHead, csvTail

