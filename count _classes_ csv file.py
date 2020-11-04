# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:27:35 2020
path= csv file path as given below

@author: Admin
"""



import pandas as pd

def csv_count(path):
    
    with open(path,'rt')as f:
        
        data = pd.read_csv(f)
        print(data['class'].value_counts())
   
if __name__== "__main__":
    
    path= "C://Users//Admin//Desktop//csv_file//train_labels.csv"
    
    csv_count(path)
  
       
            
            
         
       
          