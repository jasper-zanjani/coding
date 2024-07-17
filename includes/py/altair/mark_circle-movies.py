from vega_datasets import data
import streamlit as st
import altair as alt
import pandas as pd


chart = alt.Chart(data.movies.url).mark_circle().encode(
    alt.X('IMDB_Rating:Q').bin(),
    alt.Y('Rotten_Tomatoes_Rating:Q').bin(),
    size='count()'
)

st.write(chart)