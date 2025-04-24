# Data science

## Jupyter

--8<-- "includes/py/jupyter/info.md"


## Pandas

Construct a **data frame** using **pandas.DataFrame**.

```py
import pandas as pd

# Define column headers
df_one = pd.DataFrame(columns=['Column 1', 'Column 2'])

# Define a data frame from a dictionary object
df = pd.DataFrame(data)

# Import a CSV
url='https://raw.githubusercontent.com/QuantEcon/lecture-python-programming/master/source/_static/lecture_specific/pandas/data/test_pwt.csv'
df_csv = pd.read_csv(url)

# Select data by position
df_csv[2:5]

# Select columns by passing a list of column names
df_csv[['country','tcgdp']]

# Select both rows and columns
df.iloc[2:5, 0:4]
```

Pandas uses **matplotlib** as the default backend for graphs

## matplotlib

--8<-- "includes/py/matplotlib/info.md"


<div class="grid cards" markdown>

-   **yfinance**

    ---

    --8<-- "includes/py/yfinance/info.md"

-   **streamlit**

    --8<-- "includes/py/streamlit/info.md"
