[SignalListItemFactory][Gtk.SignalListItemFactory] emits several signals.
Handlers for them take two arguments: the factory itself and the list item, which contains the data to be bound to the widget.

<div class="grid cards" markdown>

-   **setup**

    `setup` is emitted to create a widget for each row.
    The widget is created in code within the callback and then assigned to the list item with `set_child`


    -   In the example implementation, this is a humble [Label][Gtk.Label]. (1)
        This is also how Taiko implements the factory when he creates the GridView. (2)
        {: .annotate }

        1.  

            ```py hl_lines="20-22" title="SignalListItemFactory example"
            --8<-- "includes/pygobject/GtkListView/SignalListItemFactory/00/main.py"
            ```

        2.  

            ```py hl_lines="32-35" title="Taiko step 18 (GridView)"
            --8<-- "includes/pygobject/taiko/18/main-gridview.py"
            ```

    -   In the Starships implementation, this is a [Bin][Adw.Bin] containing a Label. (1)
        {: .annotate }

        1.  

            ```py hl_lines="17-21" title="Starships"
            --8<-- "includes/pygobject/starships/02/main.py"
            ```

-   **bind**

    `bind` is responsible for implementing data binding and is called every time the underlying model's data is updated.
    Its callback must associate the list item with the appropriate data from the model using `get_item`.



    -   In all example implementations, the Label is simply assigned the list item's text with `set_text`. (1) (2) (3)
        {: .annotate }

        1.  

            ```py hl_lines="20-22" title="SignalListItemFactory example"
            --8<-- "includes/pygobject/GtkListView/SignalListItemFactory/00/main.py"
            ```

        2.  

            ```py hl_lines="32-35" title="Taiko step 18 (GridView)"
            --8<-- "includes/pygobject/taiko/18/main-gridview.py"
            ```

        3.  

            ```py hl_lines="23-27" title="Starships"
            --8<-- "includes/pygobject/starships/02/main.py"
            ```

</div>


