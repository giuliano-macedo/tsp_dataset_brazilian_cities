import pandas as pd
from tqdm import tqdm
from itertools import product
import requests
import os
import json


def gmaps(city1,city2):
	r=requests.get(
	    "https://maps.googleapis.com/maps/api/distancematrix/json",
	    params={
	        "units":"metric",
	        "origins":city1,
	        "destinations":city2,
	        "key":os.getenv('KEY')
	    }
	)
	if not r.ok:
		raise RuntimeError("!r.ok")
	obj=r.json()
	
	if obj["status"] != "OK":
		raise RuntimeError("!obj.status",obj["status"],obj)

	origin_addresses=obj["origin_addresses"][0]
	destination_addresses=obj["destination_addresses"][0]

	print(origin_addresses)
	print(destination_addresses)

	element=obj["rows"][0]["elements"][0]
	


	if element["status"]=="OK":
		return element["distance"]["value"]
	elif element["status"]=="ZERO_RESULTS":
		return float("nan")
	else :
		raise RuntimeError("!element.status",element["status"],obj)



df=pd.read_csv("simplemaps/worldcities.csv")

_query=(df[(df.country == "Brazil") & (df.capital=="admin")])

estados=pd.DataFrame(data=zip(_query.admin_name,_query.lat,_query.lng),columns=("estado","lat","lng"))

estados.to_csv("states.csv",index=False)

nodes=list(estados.estado)
edges=[]

state_city=[(state,city) for city,state in zip(_query.admin_name,_query.city)]

for (state1,city1),(state2,city2) in tqdm(product(state_city,state_city),total=len(nodes)**2):
	if city1==city2:
		continue
	dist=gmaps(
		f"{state1},{city1}",
		f"{state2},{city2}"
	)
	edges.append((city1,city2,dist))

	with open("states_gmaps.json","w") as f:
		json.dump({"nodes":nodes,"edges":edges},f,ensure_ascii=False,indent=4)

