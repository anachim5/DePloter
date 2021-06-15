import os
import pandas as pd

class DataProc():
    file_name=""
    file_extension=""
    file_path=""
    data=""
   #constructor
    def  __init__(self,fpath):
       self.filePath=fpath

    #read data from selected file
    def readDataType(self,fpath):
        # will return a tuple of root and extension
        self.file_path=fpath
        split_tup = os.path.splitext(self.file_path)
  
        # extract the file name and extension
        self.file_name = split_tup[0]
        self.file_extension = split_tup[1]
        
        
        print("File Extension: ", self.file_extension)
        #choose depending on file type, how to process it
        if ".txt" in self.file_extension:
            self.readDataTXT()
        if ".csv" in self.file_extension:
            self.readDataCSV()
        if ".xlsx" in self.file_extension:
            self.readDataXLSX()
       
        return self.data


    def processData(self):
        self.data=self.data.to_numpy()
        x_values=[x[0] for x in self.data]
        y_values=[y[1] for y in self.data]
        # print(x_values)
        # print(y_values)
        self.data=[x_values,y_values]
        
    #read data from xlsx and return DataFrame
    def readDataXLSX(self):
        self.data = pd.read_excel(self.file_path,index_col=False)
        self.processData()
        
    #read data from CSV and return DataFrame
    def readDataCSV(self):
        self.data = pd.read_csv(self.file_path,index_col=False)
        self.processData()
        
    
    #read data from TXT and return DataFrame
    def readDataTXT(self):
        self.data = pd.read_csv(self.file_path, sep=" ", header=None, names=["X", "Y"],index_col=False)
        self.processData()
        





