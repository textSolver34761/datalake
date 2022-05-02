import requests
import csv 
import json
from flask import Flask, json
import pandas as pd

#csv file name to be read in 

#in_csv = 'twitter_comment.csv'

#get the number of lines of the csv file to be read

#number_lines = sum(1 for row in (open(in_csv)))
#print(number_lines)
#size of rows of data to write to the csv, 
#you can change the row size according to your need
rowsize = 1000
#start looping through data writing it to a new file for each set

for i in range(1,1600001,rowsize):
    out_csv = 'input' + str(i) + '.csv'
    #print(out_csv)
    #df = pd.read_csv(in_csv, header=None, nrows = rowsize,#number of rows to read at each loop
    #skiprows = i)#skip rows that have been read

#csv to write data to a new file with indexed name. input_1.csv etc.
#out_csv = 'input' + str(i) + '.csv'
#print(out_csv)
#df.to_csv(out_csv, index=False, header=False, mode='a',#append data to csv file
#chunksize=rowsize)#size of data to append for each loop

jsonArray = []
#read csv file

with open(r'./twitter_comment.csv', 'r', encoding="ISO-8859-1") as csvf: 
    #load csv file data using csv library's dictionary reader
    csvReader = csv.DictReader(csvf)
    #convert each csv row into python dict
    for row in csvReader: 
        #add this python dict to json array
        jsonArray.append(row)
#convert python jsonArray to JSON String and write to file
with open(r'data.json', 'w', encoding='utf-8') as jsonf: 
    jsonString = json.dumps(jsonArray, indent=4)
    jsonf.write(jsonString)

api = Flask(__name__)

@api.route('/twitter', methods=['GET'])
def twitts():
  return json.dumps(jsonString)

print("waiting for api")
if __name__ == '__main__':
    api.run(host='127.0.0.1', port=8880)
