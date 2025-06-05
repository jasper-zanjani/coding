List widgets like [ListView][Gtk.ListView] and [GridView][Gtk.GridView] require a **model** and a **factory**.

-   Model: **SelectionModel** subclass (1)
    {: .annotate }

    1.  

        --8<-- "includes/gtk/GtkSelectionModel/info.md"

-   Factory: **ListItemFactory** subclass (1)
    {: .annotate }

    1.  

        --8<-- "includes/gtk/GtkListItemFactory/info.md"


The simplest implementation of a model is a [StringList][Gtk.StringList] from a list of strings, which can then be formed into a [SingleSelection][Gtk.SingleSelection].

As for factory, ListView can be implemented in the UI definition with **BuilderListItemFactory** (1) or in code with **SignalListItemFactory** (2).
{: .annotate }

1.  

    <div class="grid cards" markdown>

    ```py hl_lines="17-20"
    --8<-- "includes/gtk/GtkListView/BuilderListItemFactory/00/main.py"
    ```

    ```blueprint hl_lines="25-38"
    --8<-- "includes/gtk/GtkListView/BuilderListItemFactory/00/main.blp"
    ```

    </div>

2.  

    <div class="grid cards" markdown>

    ```py hl_lines="20-31 35"
    --8<-- "includes/gtk/GtkListView/SignalListItemFactory/00/main.py"
    ```


    ```blueprint hl_lines="25"
    --8<-- "includes/gtk/GtkListView/SignalListItemFactory/00/main.blp"
    ```

    </div>



A more elaborate model can be implemented by extending [GObject][GObject] and creating a [ListStore][Gio.ListStore]. (1)
{: .annotate }

1.  

    <div class="grid cards" markdown>

    -   **SignalListItemFactory**

        === ":simple-python: Python"

            ```py
            # To be implemented
            ```

        === "Blueprint"

            ```blueprint
            // To be implemented
            ```

    -   **BuilderListItemFactory**

        === ":simple-python: Python"

            ```py
            --8<-- "includes/gtk/GtkListView/BuilderListItemFactory/01/main.py"
            ```

        === "Blueprint"

            ```blueprint
            --8<-- "includes/gtk/GtkListView/BuilderListItemFactory/01/main.blp"
            ```

    </div>

GridView works very similarly to ListView.
In fact, Taiko's tutorial implements GridView with a SignalListItemFactory. (1)
{: .annotate }

1.  

    <div class="grid cards" markdown>

    -   **GridView with SignalListItemFactory**

        ```py
        --8<-- "includes/gtk/taiko/18/main-gridview.py"
        ```


    -   **GridView with BuilderListItemFactory**

        === ":simple-python: Python"

            ```py hl_lines="19-20" title="main.py"
            --8<-- "includes/gtk/GtkListView/02/main.py"
            ```

        === "Blueprint"

            ```blueprint hl_lines="25" title="main.blp"
            --8<-- "includes/gtk/GtkListView/02/main.blp"
            ```


    </div>

