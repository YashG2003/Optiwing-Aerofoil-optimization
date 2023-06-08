#!/usr/bin/python3
from subprocess import call 
import csv

def createCp(NACA,R,a):
    with open(f'temp.txt','w') as temp:
        temp.write(f"NACA\n{NACA}\noper\nr {R}\na {a}\ncpwr ./cpFiles/cpPlot_{NACA}_{R}_{a}.txt\n\n")
        temp.flush()
        call("xfoil < temp.txt", shell=True)

with open('database.csv', newline='') as db :
    f = csv.reader(db)
    next(f)
    l = []
    for i in f:
        l.append(i)

for i,j,k in l:
   createCp(i,j,k) 
