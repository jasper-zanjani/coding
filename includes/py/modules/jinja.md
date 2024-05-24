The Python package is capitalized, whereas it is in lowercase when being imported within Python itself.

<div class="grid cards" markdown>

```sh
pip install Jinja2
```

```py
import jinja2
```

</div>

Templates are assumed to be stored in a dedicated directory.
This directory is associated with the **Environment** object which is the central object in the Jinja API.

```py
from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("template.j2")
```