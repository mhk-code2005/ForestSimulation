from tkinter import *
import tkinter
import matplotlib.pyplot as plt

class statistics:
    def __init__(self, master, sample, varList):
        self.stat = {}
        self.populations = {}
        self.colors = {}

        for i in range (len(sample)):
                q=Label(master,text = sample[i].getSpecies()+": %d ; Total Males: %d ; Total Females %d" %(0,0,0) ,font=("Helvetica", 27), fg='white', bg='black', height=3, width = 50, borderwidth=1, relief="groove")
                q.grid(row = i)
                self.stat.update({sample[i].getSpecies():[q,[0,0,0],sample[i]]})
                self.populations.update({sample[i].getSpecies():[]})
                self.colors.update({sample[i].getSpecies():sample[i].getColor()})
        
        for i in varList:
            if varList[i] != None:
                self.stat[i.getGeneralClass().getSpecies()][1][1] += 1
        
        for l in self.stat:
            self.stat[l][0].configure(text = l +": %d ; Total Males: %d ; Total Females %d" %(0,0,0))
        


    def zeroed(self):
        for i in self.stat:
            self.stat[i][1] = [0,0,0]

    def updateStat(self, animals):
        self.zeroed()

        for instance in animals:
            if animals[instance] != None:
                self.stat[instance.getGeneralClass().getSpecies()][1][0] += 1
                if instance.sex == "Male":
                    self.stat[instance.getGeneralClass().getSpecies()][1][1] += 1
                else:
                    self.stat[instance.getGeneralClass().getSpecies()][1][2] += 1
        for l in self.stat:
            values = tuple(self.stat[l][1])
            self.populations[l].append(values[0])
            self.stat[l][0].configure(text = l +": %d ; Total Males: %d ; Total Females %d " %values)
    

    def graphPop(self, graph):

        graph.clear()

        for i in self.populations:
            plt.plot(self.populations[i], label = i)#color = self.colors[i])
        plt.legend()

        plt.pause(0.000001)
        plt.draw()


            
