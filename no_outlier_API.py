# Making API for outlier data to be accessed online
# Import packages
from fastapi import FastAPI, HTTPException
import pandas as pd

# Create new object
app = FastAPI()

# Create new function to read data
def getData():
    return pd.read_csv('no_outlier.csv')

# API to read data
# Show entire data entry after outlier handling
# Endpoint -> home
# Have to use response model
# /home to show data
@app.get("/home",response_model=list)
def getHome():
    data = getData()
    return data.to_dict(orient='records') 

# API to delete data
# Delete data entry after handling outlier
@app.delete("/{index}}")
def deleteByIndex(index:int):
   data = getData()
   if index not in data.index:
       raise HTTPException(status_code=404, detail = "Row not found")
   else:
       data = data.drop(index)
       data.to_csv('no_outlier.csv', index=False)
   return {
        "message" : f"Deleted row {index} successfully"
    }
