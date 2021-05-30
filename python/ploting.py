from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
class drawPlot():
     # the figure that will contain the plot
    fig=Figure(figsize = (5, 5), dpi = 100)

    # constructor
    def __init__(self,window):
        self.window=window
    def draw(self):       
        #frame to position plot and its toolbar
        self.plotFrame=Frame(master=self.window)
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig,master = self.plotFrame)  
        self.canvas.draw()
    
        # placing the canvas on the Tkinter window
        self.canvas.get_tk_widget().grid(column=0,row=0)
        # creating the Matplotlib toolbar and putting it into the frame
        self.toolbarFrame = Frame(master=self.plotFrame)
        self.toolbarFrame.grid(row=1,column=0)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbarFrame)
        #grid the plot frame
        self.plotFrame.grid(row=0,column=0)
    

    #draw empty plot
    def drawEmpty(self):
        #adding the subplot
        self.plot1 = self.fig.add_subplot(111)
        #plotting the graph
        self.plot1.plot(0)
        #drawing plot into the window
        self.draw()



# ******* Types of plots *********** #

    #standard plot
    def drawPlot(self,data):

         # process data
        x_values=data[0]
        y_values=data[1]
    
        # adding the subplot
        self.plot1 = self.fig.add_subplot(111)
        # plotting the graph
        self.plot1.plot(x_values,y_values)
        #drawing plot into the window
        self.draw()

    # histogram
    def drawHistogram(self,data,bins):
        #data
        values = data[0]
        #bins
        bins=bins
        # adding the subplot
        self.plot1 = self.fig.add_subplot(111)
        # plotting the graph
        self.plot1.hist(values,bins)
        #drawing plot into the window
        self.draw()


    # scatter plot
    def drawScatter(self,data):
         # process data
        x_values=data[0]
        y_values=data[1]
    
        # adding the subplot
        self.plot1 = self.fig.add_subplot(111)
        # plotting the graph
        self.plot1.scatter(x_values,y_values)
        #drawing plot into the window
        self.draw()

    # pie chart  
    def drawPieChart(self,data):
        values=data[0]
        labels=data[1]
        # adding the subplot
        self.plot1 = self.fig.add_subplot(111)
        # plotting the graph
        self.plot1.pie(values,labels=labels)
        self.draw()
        pass

    def drawPolarPlot(self,data):
         # process data
        x_values=data[0]
        y_values=data[1]
    
        # adding the subplot
        self.plot1 = self.fig.add_subplot(111)
        # plotting the graph
        self.plot1.polar(x_values,y_values)
        #drawing plot into the window
        self.draw()
    def drawBarChart(self,data):
         # process data
        x_values=data[0]
        y_values=data[1]
    
        # adding the subplot
        self.plot1 = self.fig.add_subplot(111)
        # plotting the graph
        self.plot1.bar(x_values,y_values)
        #drawing plot into the window
        self.draw()