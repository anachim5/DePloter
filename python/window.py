from tkinter import *
from tkinter import filedialog
from os import getcwd as pwd
import ploting
import data
#main class that runs a window
class windowManager():
    #fields
    filename=""
    data=""

    #create a windows of the application
    def __init__(self):    
        # declare the window
        self.window = Tk()
        # set window title
        self.window.title("DePlotter")
        # set window width and height
        self.window.geometry("1000x900")
        # set window background color
        self.window.configure(bg='lightgray')
        #right frame
        self.rightMenu=Frame(self.window)
        self.rightMenu.grid(row = 0,column=1,sticky=NE)
        #menu bar
        self.menubar()
        self.window.config(menu=self.menubar)
        #fileopenbutton
        self.openFileButton()
        #class containing a plot
        self.plot=ploting.drawPlot(self.window)
        #draw empty plot
        self.drawEmptyPlot()
        #draw plot button
        self.drawPlotButton()
        #draw a frame containing a list of types of plots
        self.definePlotType()
        self.window.mainloop()
    
    #create a function to read files
    def selectFile(self):
        filetypes = (('data files', '*.txt,*.csv,*.xlsx'),('All files', '*.*'))

        self.filename = filedialog.askopenfilename(title='Open a file',initialdir=pwd,filetypes=filetypes)
        print(self.filename)
        try:
            #create object of data processor
            self.dataProcessor=data.DataProc(self.filename)
            #read data type
            self.data=self.dataProcessor.readDataType(self.filename)
            print(self.data)
        except Exception :
            raise NotImplementedError("Cannot read data")

    #create a button that read files
    def openFileButton(self):
        fileFrame=Frame(self.rightMenu)
        name = Label(fileFrame, text = "Choose a data file with data").grid(row = 0,column=0)  
        open_button = Button(fileFrame,text='Open a File',command=self.selectFile).grid(row=0,column=1) 
        fileFrame.grid(row=0,column=0,sticky=N)   
    #create a widget that is a window menu
    def menubar(self):
        #whole menu bar
        self.menubar = Menu(self.window)  
        #file
        file = Menu(self.menubar, tearoff=0)  
        file.add_command(label="New")  
        file.add_command(label="Open")  
        file.add_command(label="Save")  
        file.add_command(label="Save as...")  
        file.add_command(label="Close")  
        
        file.add_separator()  
        
        file.add_command(label="Exit", command=self.window.quit)  
        
        self.menubar.add_cascade(label="File", menu=file)  

        #edit
        edit = Menu(self.menubar, tearoff=0)  
        edit.add_command(label="Undo")  
        edit.add_separator()  
        edit.add_command(label="Cut")  
        edit.add_command(label="Copy")  
        edit.add_command(label="Paste")  
        edit.add_command(label="Delete")  
        edit.add_command(label="Select All")  
        self.menubar.add_cascade(label="Edit", menu=edit)  
        #help
        help = Menu(self.menubar, tearoff=0)  
        help.add_command(label="About")  
        self.menubar.add_cascade(label="Help", menu=help)  
    #draw button to draw plot
    def drawPlotButton(self):
        plot_button = Button(master = self.rightMenu,command = self.chooseTypeOfPlot,height = 2,width = 10,text = "Plot").grid(column=0,row=2)
    #menu to modify plot type
    def definePlotType(self):

        plotTypeFrame = Frame(master=self.rightMenu)
        
        
        lbl = Label(plotTypeFrame,text = "Choose type of plot").pack()
  
        self.listbox = Listbox(plotTypeFrame)
        
        self.listbox.insert(1,"Plot")  
        
        self.listbox.insert(2, "Histogram")  
        
        self.listbox.insert(3, "Scatter plot")  
        
        self.listbox.insert(4, "Pie chart")  
        
        self.listbox.insert(5,"Polar plot")

        self.listbox.insert(6,"Bar chart")
        
        self.listbox.pack()
                
        #this button will choose the selected item from the list   
        
        btn = Button(plotTypeFrame, text = "Choose", command=self.selected_item).pack()
        plotTypeFrame.grid(row=1,column=0,sticky=N)
    

    # ***** draw types of plots ******

    def chooseTypeOfPlot(self):
        if self.typeOfPlot=="Plot":self.drawPlot()
        if self.typeOfPlot=="Histogram":self.drawHistogram()
        if self.typeOfPlot=="Scatter plot":self.drawScatter()
        if self.typeOfPlot=="Pie chart":self.drawPieChart()
        if self.typeOfPlot=="Polar plot":self.drawPolar()
        if self.typeOfPlot=="Bar chart":self.drawBarChart()

    def selected_item(self):
        for i in self.listbox.curselection():
            self.typeOfPlot=self.listbox.get(i)
            print("Type of plot : "+self.typeOfPlot)
    #draw empty plot
    def drawEmptyPlot(self):
        self.plot.drawEmpty()
    #draw plot
    def drawPlot(self):
        self.plot.drawPlot(self.data)
    #draw histogram
    def drawHistogram(self):
        self.plot.drawHistogram(self.data,10)
    #draw scatter
    def drawScatter(self):
        self.plot.drawScatter(self.data)
    #draw pie chart
    def drawPieChart(self):
        self.plot.drawPieChart(self.data)
    #draw polar plot
    def drawPolar(self):
        self.plot.drawPolarPlot(self.data)
    #draw bar char 
    def drawBarChart(self):
        self.plot.drawBarChart(self.data)