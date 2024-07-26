import pandas as pd
import streamlit as st

""" Series list functions """

def get_series_data(series_data):
    """
    Converts series data from a given input format into a pandas DataFrame.

    This function processes a nested dictionary structure to extract series information 
    and compile it into a DataFrame with columns 'Series ID', 'Series Name', and 'Dates'.

    Parameter series_data: Dictionary containing series information.
    Precondition: series_data is a dictionary with a specific structure, including 'seriesMapProto'.

    Returns: 
    A pandas DataFrame containing series data.
    """
    data_list = []

    for data in series_data['seriesMapProto']:
        dates = data['date']
        for series_name in data['series']:
            data_list.append({'Series ID': f"{series_name['id']}", 'Series Name': series_name['name'], 'Dates': dates})
        else:
            continue

    df = pd.DataFrame(data_list, columns=['Series ID', 'Series Name', 'Dates'])

    return df

# Function to clear the session state if selectbox value changes
def clear_series_variables():
    """
    Clears the session state for series data if the series type selectbox value changes.

    This function checks if the previous series type stored in the session state is different from 
    the current series type and deletes the stored series data if they are not the same.
    """
    if 'prev_series_type' in st.session_state and st.session_state.prev_series_type != st.session_state.series_type:
        del st.session_state.series_data


""" ICC Ranking list functions """

def get_ranking_data(icc_ranking_data):
    """
    Converts ICC ranking data from a given input format into a pandas DataFrame.

    This function processes a dictionary to extract player ranking information 
    and compile it into a DataFrame with columns 'Player ID', 'Rank No', 'Player Name', 
    'Country', 'Points', 'Avg', and 'last Updated On'.

    Parameter icc_ranking_data: Dictionary containing ICC ranking information.
    Precondition: icc_ranking_data is a dictionary with a specific structure, including 'rank'.

    Returns: 
    A pandas DataFrame containing ICC ranking data.
    """
    data_list = []

    for data in icc_ranking_data['rank']:
        data_list.append({'Player ID': data['id'],
                          'Rank No': data['rank'], 
                          'Player Name': data['name'],
                          "Country": data["country"],
                          "Points": data["points"],
                          "Avg": data["avg"],
                          "last Updated On": data["lastUpdatedOn"],
                          })
        
        df = pd.DataFrame(data_list, columns=['Player ID',
                                              'Rank No', 
                                              'Player Name',
                                              'Country',
                                              'Points',
                                              'Avg',
                                              'last Updated On',
                                              ])
    return df

# Function to clear the session state if selectbox value changes
def clear_ranking_variables():
    """
    Clears the session state for ICC ranking data if selectbox values change.

    This function checks if the previous format type, gender, or category stored in the session state 
    is different from the current values and deletes the stored ICC ranking data if they are not the same.
    """
    if 'prev_format_type' in st.session_state and st.session_state.prev_format_type != st.session_state.format_type:
        del st.session_state.icc_ranking_data
    if 'prev_is_women' in st.session_state and st.session_state.prev_is_women != st.session_state.is_women:
        del st.session_state.icc_ranking_data
    if 'prev_category' in st.session_state and st.session_state.prev_category != st.session_state.category:
        del st.session_state.icc_ranking_data


""" ICC Records list functions """

def get_headers(response):
    """
    Extracts headers from the ICC records response.

    This function processes the response to extract headers and compile them into a list.

    Parameter response: Dictionary containing ICC records information.
    Precondition: response is a dictionary with a specific structure, including 'headers'.

    Returns: 
    A list containing headers.
    """
    header_list = []

    headers = response['headers']
    for x in headers:
        header_list.append(x)

    return header_list

def get_values(response):
    """
    Extracts values from the ICC records response.

    This function processes the response to extract record values and compile them into a list of lists.

    Parameter response: Dictionary containing ICC records information.
    Precondition: response is a dictionary with a specific structure, including 'values'.

    Returns: 
    A list of lists containing record values.
    """
    records_list = []

    values = response['values']

    for x in values:
        records_list.append(x['values'][1:])

    return records_list

# Function to clear the session state if selectbox value changes
def clear_records_variables():
    """
    Clears the session state for ICC records data if the stats type selectbox value changes.

    This function checks if the previous stats type stored in the session state is different from 
    the current stats type and deletes the stored ICC records data if they are not the same.
    """
    if 'prev_stats_type' in st.session_state and st.session_state.prev_stats_type != st.session_state.stats_type:
        del st.session_state.icc_records_data
