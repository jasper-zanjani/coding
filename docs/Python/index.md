# Python

!!! info "Glossary"

    **Method resolution order (MRO)** is the order of base classes that are searched when using **super()**. 
    It is accessed with **\_\_mro\_\_**, which returns a tuple of base classes in order of precedence, ending in `object` which is the root class of all classes.
    ([src](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/))

    **Non-interactive debugging** is the most basic form of debugging, dependent on `print` or `log` statements placed within the body of code.

    A **type slot** is any of a number of fields within each magic method, including `__new__()`, `__init__()`, and `__prepare__()` (which returns a dictionary-like object that's used as the local namespace for all code from the class body)


## Tasks

!!! info "Miscellany"

    <div class="grid cards" markdown>


    ```py title="Entrypoint"
    if __name__ == '__main__':
        main()
    ```

    ```sh title="Virtual environments"
    pipenv --python 3.6

    python -m venv project

    virtualenv -p /usr/bin/python2 project
    ```

    -   #### Formatting

        ---

        **flake8**, **black**, and especially **yapf** (Google) are CLI tools used to automatically format Python code.

    </div>

#### Terminal text output

<div class="grid cards" markdown>

-   #### colorama

    ---

    Colorama provides a set of enums that resolve to terminal codes when concatenated with strings.

    ```py
    colorama.Fore.GREEN
    colorama.Style.RESET_ALL
    ```

-   #### termcolor

    ---

    --8<-- "includes/py/modules/termcolor.md"


</div>

#### Hashing

A variety of hashing algorithms are available in various libraries.

<div class="grid cards" markdown>

-   The standard library contains [**hashlib**](https://docs.python.org/3/library/hashlib.html), which supports a variety of SHA algorithms including SHA3, as well as MD5, Blake and SHAKE (Secure Hashing Algorithm and KECCAK).

    ```py title="hashlib"
    import hashlib

    data = b'Hello, World!'

    # The quickest way to use them is to use the named constructors, passing the text as binary.
    hashlib.sha256(data).hexdigest()

    # A generic constructor is also available with a less appealing workflow
    h = hashlib.new('sha256')
    h.update(data)
    h.hexdigest()
    ```


-   The [**pysha3**](https://pypi.python.org/pypi/pysha3) module also supports various algorithms, including SHA3, SHAKE, and Keccak.

    ```py
    import sha3

    data = b'Hello, World!'

    sha3.keccak_256(data).hexdigest()
    ```


-   The [**eth-utils**](https://pypi.org/project/eth-utils/) package also provides the [Keccak-256](https://wiki.rugdoc.io/docs/introduction-to-ethereums-keccak-256-algorithm/) algorithm used by Ethereum.


    ```py
    import eth_utils

    data = b'Hello, World!'

    eth_utils.keccak(text=data.hex()).hex()
    ```

</div>


#### File processing

<div class="grid cards" markdown>


```py hl_lines="6" title="YAML"
import yaml

# Serialize
with open('./starships.yaml','w') as f:
    yaml.dump(starships, f)

# Deserialize
with open('./starships.yaml') as f:
    starships = yaml.safe_load(f)
```

```py title="JSON"
import json

# Serialize
with open('/starships.json',"w") as f:
    json.dump(data,f)

# Deserialize
with open('./starships.json') as f:
    data=json.load(f)
```

</div>
