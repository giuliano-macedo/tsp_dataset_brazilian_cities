import pandas as pd
import json
from math import sin, cos, sqrt, atan2, radians
from itertools import combinations
def dist(lat1,lng1,lat2,lng2):

	lat1=radians(lat1)
	lng1=radians(lng1)
	lat2=radians(lat2)
	lng2=radians(lng2)

	dlon = lng2 - lng1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	return dist.R * c
dist.R=6373.0# approximate radius of earth in km

df=pd.read_csv("simplemaps/worldcities.csv")

_query=(df[(df.country == "Brazil") & (df.capital=="admin")])

estados=pd.DataFrame(data=zip(_query.admin_name,_query.lat,_query.lng),columns=("estado","lat","lng"))

estados.to_csv("states.csv",index=False)

nodes=list(estados.estado)

edges=[]

for (estado1,lat1,lng1),(estado2,lat2,lng2) in combinations(estados.values,2):

	edges.append((estado1,estado2,dist(lat1,lng1,lat2,lng2)))

with open("states.json","w") as f:
	json.dump({"nodes":nodes,"edges":edges},f,ensure_ascii=False,indent=4)