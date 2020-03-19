import json
from math import isnan


def load_json(fname):
	ans={}
	with open(fname) as f:
		obj=json.load(f)
	for city1,city2,dist in obj["edges"]:
		ans[(city1,city2)]=dist
	return ans,obj["nodes"]

line,nodes1=load_json("states_line.json")
gmaps,nodes2=load_json("states_gmaps.json")

assert nodes1==nodes2

nodes=nodes1

for (city1,city2),dist in gmaps.items():
	if not isnan(dist):continue
	print(city1,city2)
	gmaps[(city1,city2)]=line[(city1,city2)]

edges=[(city1,city2,dist) for (city1,city2),dist in gmaps.items() ]


with open("states_merged.json","w") as f:
	json.dump({"nodes":nodes,"edges":edges},f,ensure_ascii=False,indent=4)
