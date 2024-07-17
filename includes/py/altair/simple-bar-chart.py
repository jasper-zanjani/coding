import altair as alt
import pandas as pd
import streamlit as st
import numpy as np
from random import random

letters = [chr(l + 65) for l in range(26)]
values = [random() for i in letters]

df = pd.DataFrame({
    'a': letters,
    # 'b': np.random.randn(len(letters),1)
    'b': values
})

chart = alt.Chart(df).mark_bar().encode(
    x='a',
    y='b'
)

st.write(chart)