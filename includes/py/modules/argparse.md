The argparse module is for designing command-line interfaces.

The `ArgumentParser` object exposes an attribute that contains the value passed in from the command-line. This attribute takes its identifier from the `dest` keyword argument when invoking the `add_argument()` method.


```py
import argparse

def get_args():
    parser = argparse.ArgumentParser(description=helptext) # (1)
    parser.add_argument("foo", dest='bar')
    return parser.parse_args()

def main():
    args = get_args().bar
```

1. The optional value assigned to description will be displayed when running the script with -h/--help
```
usage: argparse_practice.py [-h] [-f bar]

optional arguments:
  -h, --help         show this help message and exit
  -f bar, --foo bar
```

##### Defining arguments and options

<div class="grid cards" markdown>

```py title="Help string"
parser.add_argument("foo", help="bar")
```

```py title="Typing"
parser.add_argument("foo", type=int)
```


```py title="Flags"
parser.add_argument('-o', '--on', 
                    help='A boolean flag', 
                    action='store_true')
```

```py title="Choices"
parser.add_argument("foo", choices=["bar","baz"])
parser.add_argument("foo", choices=range(1,10))
parser.add_argument("foo", choices='Hello, world!') # equivalent to ['H','e', ...]
```

```py title="Mutually exclusive options" hl_lines="2"
parser = argparse.ArgumentParser(description=helptext) # (1)
g=parser.add_mutually_exclusive_group()
g.add_argument("-v","--verbose", action="store_true")
g.add_argument("-q","--quiet","-s","--silent", 
                    action="store_true",
                    help='quiet/silent mode')
```

```py title="Composite examples"
parser.add_argument( '-r','--radius', 
    type=int, required=True, help='radius')

# Allow multiple calls to the option
parser.add_argument( '-t', '--ticker', 
    choices=['eth', 'btc', 'sol'], action='append')
```

-   

    At least two kwargs are available to modify how an argument is described in the help message as well as its identifier in the final parsed object.


    ```py title="dest"
    # Specify identifier and its appearance in help message
    parser.add_argument("foo", dest='bar')
    ```

    ```py title="metavar"
    # Specify only appearance in help message
    parser.add_argument("foo", metavar="bar")
    ```

</div>
