# Chessboard

--8<-- "includes/gtk/links.md"

??? info "Libraries"


    GDK is concerned with _how and where_ to draw (i.e. window management, display server communication, and input) whereas GSK is concerned with _what_ to draw and _how to render it efficiently_ using hardware acceleration.

    <div class="grid cards" markdown>

    -   **GDK**

        ---

        --8<-- "includes/gtk/GDK/info.md"

    -   **GSK**

        ---

        --8<-- "includes/gtk/GSK/info.md"

    -   **Cairo**

        ---

        --8<-- "includes/gtk/cairo/info.md"

    -   **Graphene**

        ---

        --8<-- "includes/gtk/Graphene/info.md"

    </div>


!!! info "Concepts"

    <div class="grid cards" markdown>

    -   **Gestures**

        ---

        --8<-- "includes/gtk/gestures/info.md"

    -   **Snapshots**

        ---

        --8<-- "includes/gtk/snapshots/info.md"

    </div>

This example was derived (or rather copied wholesale) from the Snapshot demo in [Workbench][Workbench-git]. (1)
{: .annotate }


1.  

    ```py
    --8<-- "includes/gtk/90-chessboard/chessboard.py"
    ```

Almost all UI elements are defined in the `do_snapshot` method.
In this method the chessboard itself is assembled from groups of four squares, whose colors are defined in the class's constructor. (1)
Groups of four [Graphene.Rect][Graphene.Rect]s are assembled manually then added using `push_repeat` and `pop`.
{: .annotate }

1.  

    ```py title="Square colors" hl_lines="4-7"
    --8<-- "includes/gtk/90-chessboard/chessboard.__init__.py"
    ```

```py hl_lines="7-22"
--8<-- "includes/gtk/90-chessboard/chessboard.do_snapshot.py"
```

