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
    #draw plot
    def drawPlot(self):

         # list of squares
        y = [i**2 for i in range(101)]
    
        # adding the subplot
        self.plot1 = self.fig.add_subplot(111)
        # plotting the graph
        self.plot1.plot(y)
        #drawing plot into the window
        self.draw()

    #draw empty plot
    def drawEmpty(self):
        #adding the subplot
        self.plot1 = self.fig.add_subplot(111)
        #plotting the graph
        self.plot1.plot(0)
        #drawing plot into the window
        self.draw()

    


