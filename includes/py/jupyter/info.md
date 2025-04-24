```sh
# Run local Jupyter Notebooks webserver at port 8888 by default
jupyter notebook $PATH
```

Jupyter (1) will automatically open the browser to the [**dashboard**](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Notebook%20Basics.html), which displays the contents of the specified directory.
{: .annotate }

1.  

    --8<-- "includes/py/jupyter/callout.md"

#### Dashboard

If a notebook is already running a green dot appears beside its name, and notebooks can be renamed, deleted, or shut down from the dashboard.
Running kernels can also be displayed in the **Running tab**.
A new notebook can be created using the dropdown, and a **kernel** must be selected.
Notebooks created on the server are saved as .ipynb files under Jupyter's working directory.

#### UI

Notebooks have a modal user interface inspired by vim.
There are two modes: **Edit mode** indicated by blue border around text box and **Command mode** indicated by gray border around text box. 
Keyboard shortcuts function while in command mode. 

-   Enter edit mode on a selected cell by pressing ++enter++ and exit back to command mode with ++esc++
-   ++j++ and ++k++ navigate to cells above and below
-   ++a++ and ++b++ to open a new cell above and beneath the current one 

Cell type can be changed between "Code", "Markdown", and "Raw" from the dropdown at the top.
Markdown cells will render markdown.
Code cells will run code using the kernel.

Shell commands can be run within a code cell by preceding the command with `!`.

```jupyter
!pip freeze
```

Additional directives can be given to the jupyter runtime using **magics**.

-   **Line magics** are specified by `%`
-   **Cell magics** are specified by `%%`

#### VS Code plugin

The Jupyter extension for VS Code will connect to the same server but it must be provided with the token that is displayed when starting the server.

