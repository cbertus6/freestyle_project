# Yelp Recommendation App

This app issues requests to the [Yelp Business Search](https://www.yelp.com/) in order to provide restaurant recommendations based on location, food preference, and price. 

# Prerequisites
* Anaconda 3.7
* Python 3.7
* Pip
* Sengrid
* Plotly

## Installation

Clone or download [this repository](https://github.com/melissawelty/freestyle_project) link onto your computer. Then navigate there from the command line:

```sh
cd freestyle_project
```

Use Anaconda to create and activate a new virtual environment called "freestyle-env".

```
conda create -n freestyle-env python =3.7 # (first time only)
conda activate freestyle-env
```

From inside the virtual environment, install package dependices:

```
pip install -r requirements.txt
```
## Setup

Before using or developing this application, you will need to [obtain a Yelp API key](https://www.yelp.com/developers/documentation/v3/authentication) (ex: "abc123").

After obtaining an API key, create a new file in this repository called ".env," and update the contents of the ".env" file to specify your real API key:

```
YELP_API_KEY = "abc123"
```

## Usage
Run the recommendation script:
```
python app/food_rec.py
```
Follow the search prompts to customize search results. 

## Additional Information
A separate window will populate containing a map with the resulting restaurants to enhance the user experience. 