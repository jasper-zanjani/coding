[Streamlit](https://streamlit.io/) is a Python library that allows the creation of interactive, data-driven web applications.

```py
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Render markdown as a string
st.markdown(md)

# Render DataFrame from a CSV file
data = pd.read_csv(csv)
st.write(data)

# Render DataFrame of random values
random = pd.DataFrame(np.random.randn(200,1), columns=['n'])

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)

# Visualization
c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c) # (1)
```

1. ![](altair.png)

```sh
# Run web app locally (port 8501 by default)
streamlit run $SCRIPT
```


</div>

## Tasks

#### Modeling

<div class="grid cards" markdown>

-   #### Datasets

---

Some datasets are available for installation and use, such as [**vega\_datasets**](https://github.com/vega/vega-datasets).

```py
import pandas as pd
from vega_datasets import data

df = pd.read_json(data.movies.url)
```

-   #### Random data

---

Random data is often generated using [**numpy.random.randn**](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html) function.

```py
import pandas as pd
import numpy as np

# Single column of 200 values
df1 = pd.DataFrame(
    np.random.randn(200,1), columns=['n']
)

# 3 columns and 200 rows
df2 = pd.DataFrame(
    np.random.randn(200,3), columns=['a','b','c']
)

# Date range
rng = pd.date_range('1/1/2024', periods=72, freq='D')
df3 = pd.Series(
    np.random.randn(len(rng)), index=rng
)
```

</div>

### Visualization

<div class="grid cards" markdown>


-   #### Altair histogram

---

```py
from vega_datasets import data
import streamlit as st
import altair as alt


st.header("Practicing with Vega datasets")

st.write("From **vega_datasets.data.movies.url**")
df = pd.read_json(data.movies.url)
st.write(df)

chart = alt.Chart(data.movies.url).mark_circle().encode(
    alt.X('IMDB_Rating:Q').bin(),
    alt.Y('Rotten_Tomatoes_Rating:Q').bin(),
    size='count()'
)
st.write(chart)
```

</div>
