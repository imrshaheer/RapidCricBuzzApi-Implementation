import streamlit as st
from Utils import APIs
from Utils import helpers
import pandas as pd

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="Rapid CricBuzz Api - Implementation",
    page_icon=":cricket_bat_and_ball:",
    layout="wide",
    initial_sidebar_state="expanded"
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #     'Report a bug': "https://www.extremelycoolapp.com/bug",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)

# Create tabs for different sections
series_list_tab, ranking_tab, records_tab = st.tabs(["Series List", "ICC Rankings", "ICC Records"])

# Series List Tab
with series_list_tab:

    # Sidebar for selecting series parameters
    with st.sidebar:
        st.header("Series List parameters")
        st.session_state.series_type = st.selectbox(
            "Select Series Type:",
            ("international", "league", "domestic", "women"),
            index=0,
            placeholder="Select series type..."
        )

        # Clear previous series variables and store the selected series type
        try:
            helpers.clear_series_variables()
            st.session_state.prev_series_type = st.session_state.series_type
        except:
            pass

    # Fetch and display series data based on selected type
    try:
        if 'series_data' not in st.session_state:
            st.session_state.series_data = APIs.get_series_list_api(st.session_state.series_type)
    except:
        pass

    # Display the series list in a dataframe
    with st.container(border=False):
        st.header("All Series List for 2024-2025")

        try:
            df = helpers.get_series_data(st.session_state.series_data)
            st.session_state.series_data = st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                on_select="rerun",
                selection_mode="multi-row"
            )
        except:
            st.error("[ERROR] in loading ICC series data! Please refresh the page or select some other options", icon="🚨")

# ICC Rankings Tab
with ranking_tab:

    # Sidebar for selecting ranking parameters
    with st.sidebar:
        st.header("ICC Ranking parameters")
        st.session_state.format_type = st.selectbox(
            "Select Format Type:",
            ("test", "odi", "t20"),
            index=0,
            placeholder="Select format type..."
        )

        st.session_state.is_women = st.selectbox(
            "Select Gender Type:",
            ("0", "1"),
            index=0,
            placeholder="Select gender type...",
            help="0: is for men, 1: is for women"
        )

        st.session_state.category = st.selectbox(
            "Select Category Type:",
            ("batsmen", "bowlers", "allrounders", "teams"),
            index=0,
            placeholder="Select category type..."
        )

        # Clear previous ranking variables and store the selected parameters
        try:
            helpers.clear_ranking_variables()
            st.session_state.prev_format_type = st.session_state.format_type
            st.session_state.prev_is_women = st.session_state.is_women
            st.session_state.prev_category = st.session_state.category
        except:
            pass

    # Fetch and display ICC ranking data based on selected parameters
    try:
        if 'icc_ranking_data' not in st.session_state:
            st.session_state.icc_ranking_data = APIs.get_ranking_api(
                st.session_state.format_type,
                st.session_state.is_women,
                st.session_state.category
            )
    except:
        pass

    # Display the ranking data in a dataframe
    with st.container(border=False):
        st.header(f"ICC {st.session_state.format_type} Ranking 2024 - {'men' if st.session_state.prev_is_women == '0' else 'women'} {st.session_state.category}")

        try:
            df = helpers.get_ranking_data(st.session_state.icc_ranking_data)

            st.session_state.icc_ranking_data = st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                on_select="rerun",
                selection_mode="multi-row"
            )
        except:
            st.error("[ERROR] in loading ICC ranking data! Please refresh the page or select some other options", icon="🚨")

# ICC Records Tab
with records_tab:

    # Set default stats type
    st.session_state.stats_type = "mostRuns"

    # Fetch and display ICC records data
    if 'icc_records_data' not in st.session_state:
        st.session_state['icc_records_data'] = APIs.get_records_api(st.session_state.stats_type)

    # Display the records data in a dataframe
    with st.container(border=False):
        st.header("ICC Records List - All Time Most Runs in Test Cricket")

        try:
            st.session_state.cols = helpers.get_headers(st.session_state.icc_records_data)
            st.session_state.records_list = helpers.get_values(st.session_state.icc_records_data)

            st.session_state.index_col = pd.DataFrame(
                (f"{i+1}" for i, val in enumerate(st.session_state.records_list)), columns=["Rank"]
            )
            st.session_state.df = pd.DataFrame(st.session_state.records_list, columns=st.session_state.cols)
            st.session_state.df.insert(loc=0, column='Rank', value=st.session_state.index_col)

            st.session_state.icc_records_data = st.dataframe(
                st.session_state.df,
                use_container_width=True,
                hide_index=True,
                on_select="rerun",
                selection_mode="multi-row"
            )
        except:
            st.error('[ERROR] in loading ICC records data! Please refresh the page or select some other options', icon="🚨")
