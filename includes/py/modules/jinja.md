??? info "Installation and import"

    The package name in PyPi is capitalized

    <div class="grid cards" markdown>

    ```sh
    pip install Jinja2
    ```

    ```py
    import jinja2
    ```

    </div>


Jinja template syntax, which is inspired by Django, uses several [delimiters](https://tedboy.github.io/jinja2/templ1.html#synopsis).

- `{{ ... }}` for [expressions](https://tedboy.github.io/jinja2/templ13.html#expressions)

- `{% ... %}` for [statements](https://tedboy.github.io/jinja2/templ11.html#list-of-control-structures)

- ``

Template files are assumed to be stored in a dedicated directory.
This directory is associated with the **Environment** object which is the central object in the Jinja API.

```py
from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates"))
template = environment.get_template("template.j2")
```



```xml
--8<-- "includes/j2/circle.svg.j2"
```

