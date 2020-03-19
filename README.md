# Dataset for the traveling salesman problem of the brazilian states capitals distance combinations


## Results
`states.csv` and `states_straigth_line.json`,`states_gmaps.json` contains the output of `src` scripts

* `states.csv` contains the latitude and longitude for each brazilian state capital
* `states_line.json` contains the name of the states and the distance in km of all possible pairs
assuming a line conecting the cities
* `states_gmaps.json` contains the name of the states and the distance in km of all possible pairs
with the information from google regarding its distance, some combination results in NaN
(all combinations to or from Acre and Amapá), due to non existing routes to the location.
* `states_merged.json` substitutes `states_gmaps.json` Nan from `states_line.json` distances

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

to get `states_merged.json` use
```bash
python3 merge.py
```

follow [this tutorial](https://developers.google.com/maps/documentation/distance-matrix/start) to get the API key