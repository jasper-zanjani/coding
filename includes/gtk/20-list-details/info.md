To create a list-details UI pattern, there are two widgets available.
Both are typically used with [Breakpoint][Adw.Breakpoint] to implement reactive functionality at smaller sizes.
Note that Breakpoint does not have to be a child of either view.

-   Unlike in [NavigationSplitView][Adw.NavigationSplitView], in OverlaySplitView only a `sidebar` property exists: the rest of the content is provided as child.


-   

    --8<-- "includes/gtk/AdwOverlaySplitView/info.md"

-   

    --8<-- "includes/gtk/AdwNavigationSplitView/info.md"

=== ":simple-python: PyGObject"

    ```py title="starships/03"
    --8<-- "includes/gtk/starships/03/main.py"
    ```

