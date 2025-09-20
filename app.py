#import sys
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/add")  # this is now an end point
def add(x,y):
    return float(x)+float(y)

@app.get("/subtract") # this is now an end point
def subtract(x,y):
    return float(x)-float(y)

'''x=5
y=10

#print (f"The sum of {x}, {y}:",add(x,y))'''

if __name__== "__main__":
    '''x=sys.argv[1]
    y=sys.argv[2]
    print(add(float(x),float(y)))'''
    uvicorn.run(app, host="0.0.0.0", port=9321)
    
  
