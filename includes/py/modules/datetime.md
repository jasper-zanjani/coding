The most commonly used methods on datetime objects are:

- `strftime` output a datetime according to [format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) beginning with `%`

- `strptime` parse a string as a datetime

```py
datetime.date(2016,7,24)
datetime.date.today()
```
Difference between `datetime` objects is a `timedelta`
Parse strings into datetime objects
```py
datetime.strptime(datestring,formatstring)
``` 
```py
# Various metacharacters are defined for `strptime`
datetime.datetime.strptime('06/30/1992','%m/%d/%Y')
```
