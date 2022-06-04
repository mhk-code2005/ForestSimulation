import tkinter
from tkinter import *
from terrain import Terrain
from stats import statistics
import matplotlib.pyplot as plt
        

def visualizingTheSimulation(sample, samples, isVisualized):
    
    #CREATING THE STATISTICS WINDOW
    statWindow = tkinter.Tk()
    statWindow.title("Statistics of the Forest")
    statWindow['bg'] = "black"
    statWindow.geometry("+0+0")

    #CREATING AND ASSIGNING THE TERRAIN
    a = Terrain(30)
    a.assignTerrain(0,0,100,0)
    def generator(sample, forest):
        for i in sample:
            forest.animalGenerator(i, sample[i])
    generator(sample,a)

    if isVisualized == "Yes":
        master = tkinter.Tk()
        master.geometry("660x600+800+0")
        a.visualizeTerrain(master)
        master.update()

    statisticsOfForest = statistics(statWindow,samples,a.animalList)

    

    turn = 0
    fig = plt.figure()
    plt.xlabel("Time")
    plt.ylabel("Population")

    while True:
        turn += 1
        a.oneTurn()
        if isVisualized == "Yes":
            a.update(master)
            master.update()
            
        statisticsOfForest.updateStat(a.animalList)
        statWindow.update()
        statisticsOfForest.graphPop(fig)


