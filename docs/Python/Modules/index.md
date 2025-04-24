# Modules

When learning unfamiliar packages and importing them in a demonstration script, care must be taken that the 
demonstration script does not have the same name as the package being studied. 
If so, attempting to import the package while in an interpreter within that directory will cause the interpreter to try 
importing the incomplete script and not the package.

When running a Python interpreter within this directory, the files "calc" and "main" can be imported as modules by
specifying their names with no file extension.

```
. 
├── calc.py 
└── main.py
```
```py
import calc # No errors
import main # No errors
```
Specifying the full filename including extension does produce an error
```py
import calc.py # Error
import main.py # Error
```

#### [argparse](https://docs.python.org/3/library/argparse.html)

--8<-- "includes/py/modules/argparse.md"

#### asyncio

--8<-- "includes/py/modules/asyncio.md"

#### socket

--8<-- "includes/py/modules/socket.md"

#### scrapy

--8<-- "includes/py/modules/scrapy.md"

<div class="grid cards" markdown>

-   #### [azure.cosmos](https://github.com/Azure/azure-sdk-for-python)

    ```py
    import azure.cosmos
    from azure.cosmos.partition_key import PartitionKey

    database = cosmos_client.create_database('RetailDemo')
    container = database.create_container(id='WebsiteData', partition_key=PartitionKey(path='/CartID'))
    print('Container WebsiteData created')
    ```


-   #### collections

    ---

    - **abc** provides `Mapping` and `MutableMapping` ABCs to formalize the interfaces of dict and similar types
    - **ChainMap** Lookups are performed on each mapping in order
    - **Counter** Holds an integer count for each key; each new key adds to the count
    - **deque**: Thread-safe double-ended queue that supports most `list` methods
    - **namedtuple**
    ```py
    Card = namedtuple('Card',['rank','suit'])`
    City = namedtuple('City', 'Name Country Population Coordinates'.split(' ')]
    ```
    - OrderedDict: Maintains keys in insertion order
    - UserDict: Designed to be subclassed


-   #### csv

    ---

    ```py
    with open('file.csv', newline=''):
      data = [row for row in csv.reader(f)]
    ```
    [csv.DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader)
    ```py
    with open('greeks.csv') as f:
      reader = csv.DictReader(f)
      for row in reader:
        print(row['name'],row['city'],row['dob'])
    ```

-   #### datetime

    ---

    --8<-- "includes/py/modules/datetime.md"

-   #### discord.py

    ---

    ```sh
    pip install discord.py
    client = discord.Client()
    ```
    `Client` objects expose a decorator that is used for event handlers, functions named after various events:
    - `on_ready`
    - `on_member_join`
    - `on_error`
    - `on_message`
    ```py
    @client.event
    async def on_ready():
      print(f'{client.user} has connected to Discord!')
    ```
    Another decorator is exposed for in-chat commands ([`commands.Bot`](#discordextcommandsbot) has to be instantiated first.)
    ```py
    @bot.command(name='roll_dice', help='Simulates rolling dice.')
    async def roll(ctx, number_of_dice: int, number_of_sides: int):
      dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
      ]
      await ctx.send(', '.join(dice))
    ```
    ```py
    client.run(token)
    ```

    ```py
    bot = comands.Bot(command_prefix='!')
    ```

-   #### dotenv

    ---

    ```sh
    pip install -U python-dotenv
    ```
    Load a .env file placed in the current working directory.
    ```py
    load_dotenv()
    value =  os.getenv('key')
    ```


-   #### functools
    
    ---

    For higher-order functions (functions that act on or return other functions)\
    Apply `function` of two arguments cumulatively to the items of `iterable` in order to reduce it to a single value

    ```py
    functools.reduce(function, iterable [, initializer])
    ```

    Calculate ((((1+2) +3) +4) +5)

    ```py
    functools.reduce(lambda x, y: x+y, [1,2,3,4,5])
    ```
    `functools.reduce(lambda a,b: a*b, range(1,6))` => 120 : factorial

-   #### glob

    ---

    ```py
    # Produce a list of strings
    glob.glob('*.py')
    ```

-   #### heapq

    ---

    Support **heaps**, data objects where each node is either greater than or equal to its parent (**max-heap**) or less than or equal to its parent (**min-heap**)


    ```py
    # Create a heap from {iterable}
    heapq.heapify(iterable)

    # Remove and return the smallest element of {heap}
    heapq.heappop(heap)

    # Replace the smallest element of {heap} with {element}
    heapq.heapreplace(heap,element)
    ```

-   #### http

    ---


    ```sh
    # Start an HTTP server serving the current directory
    python http.server
    ```

-   #### itertools

    ---

    **`cycle()`** works like `next()`, but it restarts from the beginning of the iterable that is passed as argument after the last element has been reached.

    ```py
    with open('raven') as f:
        raven = [ l for l in f ]

    itertools.cycle(raven)
    ```


-   #### json

    ---

    ```py
    import json

    # Deserialize
    with open('starships.json') as f:
        data = json.load(f)

    # Serialize
    with open('starships.json',"w") as f:
        json.dump(data,f)
    ```

-   #### logging

    ---

    ```python
    import logging

    def main():
      logging.basicConfig(filename='/tmp/learn-logging.log', level=logging.ERROR, format='%(asctime)s %(levelname)s: %(message)s')
      logging.info("Once upon a midnight dreary,")
      logging.warning('While I pondered weak and weary,')
      logging.error('Over many a quaint and curious volume of forgotten lore,')

    if __name__ == '__main__':
      main()
    ```

-   #### os

    ---

    ```py
    # Execute shell command given by string.  
    # The value returned is not the output but the exit code.
    os.system('ls -la')

    # Store output in a variable
    os.popen('ls -la').read()

    # Navigate filesystem
    os.getcwd()
    os.chdir(path)

    # Test for existence of a file
    os.path.isfile(file)
    ```

-   #### pathlib

    ---

    ```py
    # Create a new pathlib object; represents a file or directory
    pathlib.Path(path)

    # Test for existence of a file
    pathlib.Path.is_file(file)

    # Test for existence of a directory
    pathlib.Path.is_dir(dir)

    # Find all .py files. Returns a generator
    pathlib.Path.glob('*.py')

    # Open a file. 
    # This makes a file object that is automatically closed, similar to `open` builtin:
    pathlib.Path.open()

    # Display file extension
    pathlib.Path.suffix()

    # Display file size
    pathlib.Path.stat().st_size
    ```

-   #### random

    ---

    ```py
    --8<-- "includes/py/modules/random.py"

    # Random 20-byte hex value
    hex(random.randrange(2**(8*20)))
    random.randrange(2**(8*20)).to_bytes(20, 'big').hex()
    ```


-   #### setuptools

    ---

    Setuptools is used when uploading packages to PyPi. 
    To create self-contained executable files, use [pyinstaller](#pyinstaller).

    ```
    PROJECT
    ├── PROJECT     # Additional code files will be placed in here
    │   └── init.py
    └── setup.py    # Containing a call to `setuptools.setup()`

    1 directory, 2 files
    ```
    setup.py
    ```python
    from setuptools import setup

    setup(
    name='funniest',
    version='0.1',
    description='The funniest joke in the world',
    url='http://github.com/storborg/funniest',
    author='Flying Circus',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=['funniest'],
    zip_safe=False
    )
    ```
    If the package has dependencies, they can be added by appending a `install_requires` keyword argument passing an array of the module names
    ```python
    setup(
    install_requires=[ 'markdown', ],
    )
    ```

    ```py
    # Reserve the name, upload package metadata, and create the pypi.python.org webpage
    python setup.py register

    # Create a source distribution, producing a tarball inside the top-level directory
    python setup.py sdist

    # Upload the source distribution
    python setup.py sdist upload

    # Do all the above in a single step
    python setup.py register sdist upload
    ```

-   #### sqlite3

    ---

    --8<-- "includes/py/modules/sqlite3.md"


-   #### subprocess

    ---

    --8<-- "includes/py/modules/subprocess.md"

-   #### sys

    ---

    --8<-- "includes/py/modules/sys.md"


-   #### threading

    ---

    --8<-- "includes/py/modules/threading.md"

-   #### tomllib

    ---

    --8<-- "includes/py/modules/tomllib.md"

-   #### typing

    ---

    --8<-- "includes/py/modules/typing.md"

-   #### urllib

    ---

    --8<-- "includes/py/modules/urllib.md"

-   #### weakref

    ---

    --8<-- "includes/py/modules/weakref.md"

-   #### winrm

    ---

    --8<-- "includes/py/modules/winrm.md"

-   #### yaml

    ---

    --8<-- "includes/py/modules/yaml.md"

-   #### xml

    ---

    --8<-- "includes/py/modules/xml.md"

</div>

