import json
import requests
import streamlit as st

@st.cache_data
def get_series_list_api(series_type):
    """
    Fetches the list of series from the API based on the series type.

    This function sends a GET request to the specified API endpoint to retrieve 
    series information. The response is cached to avoid redundant API calls.

    Parameter series_type: The type of series to retrieve.
    Precondition: series_type is a string representing the series type (e.g., 'international', 'domestic').

    Returns: 
    A dictionary containing the series information if the API call is successful.
    """
    url = f"https://cricbuzz-cricket.p.rapidapi.com/series/v1/{series_type}"

    headers = {
        "x-rapidapi-key": "b49fd7490bmsh375c84ac44f1844p12a2c7jsn60ead074afca",
        "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            print("Error: Unable to parse JSON response.")
            print("Response content:", response.content)
    else:
        print(f"Error: Received status code {response.status_code}")
        print("Response content:", response.content)

    return response_json

@st.cache_data
def get_ranking_api(formatType, isWomen, category):
    """
    Fetches the ICC ranking data from the API based on the given parameters.

    This function sends a GET request to the specified API endpoint to retrieve 
    ICC ranking information. The response is cached to avoid redundant API calls.

    Parameters:
    - formatType: The format of the game (e.g., 'test', 'odi', 't20').
    - isWomen: A flag indicating if the rankings are for women (set to 1 for women).
    - category: The category of the ranking (e.g., 'batsmen', 'bowlers', 'allrounders', 'teams').

    Precondition: 
    - formatType is a string.
    - isWomen is a string ('0' or '1').
    - category is a string.

    Returns: 
    A dictionary containing the ICC ranking information if the API call is successful.
    """
    url = f"https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/{category}"

    if isWomen == '0':
        querystring = {"formatType":f"{formatType}"}
    else:
        querystring = {"formatType":f"{formatType}", "isWomen":f"{isWomen}"}

    headers = {
        "x-rapidapi-key": "b49fd7490bmsh375c84ac44f1844p12a2c7jsn60ead074afca",
        "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            print("Error: Unable to parse JSON response.")
            print("Response content:", response.content)
    else:
        print(f"Error: Received status code {response.status_code}")
        print("Response content:", response.content)

    return response_json

@st.cache_data
def get_records_api(statsType):
    """
    Fetches the ICC records data from the API based on the given stats type.

    This function sends a GET request to the specified API endpoint to retrieve 
    ICC records information. The response is cached to avoid redundant API calls.

    Parameter statsType: The type of statistics to retrieve (e.g., 'mostRuns').
    Precondition: statsType is a string.

    Returns: 
    A dictionary containing the ICC records information if the API call is successful.
    """
    url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/topstats/0"

    querystring = {"statsType":f"{statsType}"}

    headers = {
        "x-rapidapi-key": "b49fd7490bmsh375c84ac44f1844p12a2c7jsn60ead074afca",
        "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            print("Error: Unable to parse JSON response.")
            print("Response content:", response.content)
    else:
        print(f"Error: Received status code {response.status_code}")
        print("Response content:", response.content)

    return response_json
