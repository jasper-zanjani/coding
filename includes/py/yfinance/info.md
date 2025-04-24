We can use **yfinance** (1) to [retrieve data from Yahoo Finance](https://algotrading101.com/learn/yfinance-guide/).
It uses Yahoo Finance API calls but also occasionally employs HTML scraping and pandas tables scraping to gather other information unofficially.
{: .annotate }

1.  

    --8<-- "includes/py/yfinance/callout.md"

Central to the yfinance library is the [**Ticker**](https://github.com/ranaroussi/yfinance/wiki/Ticker) module defines the Ticker objects.

**pandas\_datareader** is provided for backwards compatibility.


```py
import yfinance as yf

apple= yf.Ticker("aapl")

# show actions (dividends, splits)
apple.actions

# show dividends
apple.dividends

# show splits
apple.splits
```

```py
import yfinance as yf

btc = yf.Ticker('btc-usd')

btc.info['description']
```
