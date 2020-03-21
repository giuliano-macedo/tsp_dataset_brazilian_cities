import json
import pandas as pd
import numpy as np
import argparse
import os

parser=argparse.ArgumentParser()
parser.add_argument("file",type=argparse.FileType("r"))
args=parser.parse_args()

obj=json.load(args.file)

nodes=obj["nodes"]
n=len(nodes)

table=np.empty((n,n))
table[:]=np.nan

for city1,city2,dist in obj["edges"]:
	table[nodes.index(city1),nodes.index(city2)]=dist
for i in range(n):
	table[0][0]=0

df=pd.DataFrame(table,columns=nodes)
fname,_=os.path.splitext(args.file.name)
fname+=".csv"
print("saving as",fname)
df.to_csv(fname,index=False)