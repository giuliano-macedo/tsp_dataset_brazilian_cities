# Dataset for the traveling salesman problem of the brazilian states capitals distance combinations


## Results
`results` folder contains the files `states.csv` and `states_line.json`,`states_gmaps.json`,
`states_merged.json` that are the output of `src` scripts

* `states_coords.csv` contains the latitude and longitude for each Brazilian state capital
* `states_line.json` contains the name of the states and the distance in km of all possible pairs
assuming a line connecting the cities
* `states_gmaps.json` contains the name of the states and the distance in km of all possible pairs
with the information from Google regarding its distance, some combination results in NaN
(all combinations to or from Acre and Amapá), due to non existing routes to the location.
* `states_merged.json` substitutes `states_gmaps.json` Nan from `states_line.json` distances
* the remaining .csv's are the json adjacency matrix counterpart

## Requirements
* python >=3.7
* pip

## Executing
install pip dependencies with
```bash
pip install -r requirements.txt
```

then chdir to `src`
```bash
cd src
```

to get `states_line.json` use 
```bash
python3 line.py
```

to get `states_gmaps.json` use
```bash
KEY=YOUR_KEY python3 gmaps.py
```

follow [this tutorial](https://developers.google.com/maps/documentation/distance-matrix/start) to get the API key

to get `states_merged.json` use
```bash
python3 merge.py
```

to convert any json to an adjacency matrix in csv use `json2csv.py`
```bash
python3 json2csv.py [file]
```
