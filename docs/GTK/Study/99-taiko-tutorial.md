# [Taiko2k's Tutorial](https://github.com/Taiko2k/GTK4PythonTutorial/)

--8<-- "includes/gtk/links.md"

## 1. Empty window

Make an empty window (1)
{: .annotate }

1.  === "Links"

        -   Source: [Taiko2k/GTK4PythonTutorial](https://github.com/Taiko2k/GTK4PythonTutorial/tree/main?tab=readme-ov-file#a-most-basic-program)


```py title="main.py"
--8<-- "includes/gtk/taiko/01/main.py"
```

## 2. Adwaita

Here we [integrate](https://github.com/Taiko2k/GTK4PythonTutorial/tree/main?tab=readme-ov-file#a-better-structured-basic-gtk4--adwaita) with Adwaita.
We also add an empty box, which does not affect appearance (yet).

=== "Builder"

    <div class="grid cards" markdown>

    ```py title="main.py"
    --8<-- "includes/gtk/taiko/02/builder.py"
    ```

    ```blueprint title="main.blp"
    --8<-- "includes/gtk/taiko/02/main.blp"
    ```

    </div>

=== "Procedural"

    ```py title="main.py"
    --8<-- "includes/gtk/taiko/02/main.py"
    ```


## 3. GtkBox

=== "Builder"

    <div class="grid cards" markdown>

    ```py title="main.py"
    --8<-- "includes/gtk/taiko/03/builder.py"
    ```


    ```blueprint title="main.blp"
    --8<-- "includes/gtk/taiko/03/main.blp"
    ```

    </div>

=== "Procedural"

    ```py title="main.py"
    --8<-- "includes/gtk/taiko/03/main.py"
    ```

## 4. Button

[Adding](https://github.com/Taiko2k/GTK4PythonTutorial/tree/main?tab=readme-ov-file#add-a-button) a [Button](https://api.pygobject.gnome.org/Gtk-4.0/class-Button.html) that prints "Hello, World!" to the terminal.

We also change the Box's orientation to vertical.

=== "Builder"

    <div class="grid cards" markdown>

    ```py hl_lines="15-16" title="main.py"
    --8<-- "includes/gtk/taiko/04/builder.py"
    ```


    ```blueprint title="main.blp"
    --8<-- "includes/gtk/taiko/04/main.blp"
    ```

    </div>

=== "Procedural"

    ```py hl_lines="11 14-19" title="main.py"
    --8<-- "includes/gtk/taiko/04/main.py"
    ```


## 5. Set parameters on MainWindow

=== "Builder"

    <div class="grid cards" markdown>

    ```py title="main.py"
    --8<-- "includes/gtk/taiko/05/builder.py"
    ```

    ```blueprint hl_lines="5-6" title="main.blp"
    --8<-- "includes/gtk/taiko/05/main.blp"
    ```

    </div>


=== "Procedural"

    ```py hl_lines="18-19" title="main.py"
    --8<-- "includes/gtk/taiko/05/main.py"
    ```

## 6. Fix layout

Additional boxes allow the window to be resized without affecting UI elements.

=== "Builder"

    <div class="grid cards" markdown>
    
    ```py title="main.py"
    --8<-- "includes/gtk/taiko/06/builder.py"
    ```

    ```blueprint title="main.blp"
    --8<-- "includes/gtk/taiko/06/main.blp"
    ```

    </div>

=== "Procedural"

    ```py hl_lines="11-21"
    --8<-- "includes/gtk/taiko/06/main.py"
    ```

## 7. CheckButton

=== "Builder"

    <div class="grid cards" markdown>

    ```py title="main.py"
    --8<-- "includes/gtk/taiko/07/main.py"
    ```

    ```blueprint hl_lines="23-25" title="main.blp"
    --8<-- "includes/gtk/taiko/07/main.blp"
    ```

    </div>

=== "Procedural"

    ```py hl_lines="18 24" title="main.py"
    --8<-- "includes/gtk/taiko/07/main.py"
    ```

## 8. Grouped CheckButtons

Check buttons, when added to a group, become radio buttons.
The way I've implemented this is probably a mess but a custom property can't be added to the CheckButton in the blueprint fileso I simply added a property in code.

=== "Builder"

    <div class="grid cards" markdown>

    ```py hl_lines="24-35 37-38" title="main.py"
    --8<-- "includes/gtk/taiko/08/builder.py"
    ```

    ```blueprint hl_lines="23-26 28-31 33-36" title="main.blp"
    --8<-- "includes/gtk/taiko/08/main.blp"
    ```

    </div>

=== "Procedural"

    ```py hl_lines="18-30 42-43 46"
    --8<-- "includes/gtk/taiko/08/main.py"
    ```

## 9. Switch

=== "Builder"

    <div class="grid cards" markdown>

    ```py title="main.py"
    --8<-- "includes/gtk/taiko/09/builder.py"
    ```

    ```blueprint title="main.blp"
    --8<-- "includes/gtk/taiko/09/main.blp"
    ```

    </div>

=== "Procedural"

    ```py hl_lines="32-42"
    --8<-- "includes/gtk/taiko/09/main.py"
    ```

## 10. CSS

The path specified is relative to the working directory at the time of invocation.

```py hl_lines="12-14 43"
--8<-- "includes/gtk/taiko/10/main.py"
```

1.  

    ```css
    --8<-- "includes/gtk/taiko/10/style.css"
    ```

## 11. Scale


Note that the `get_value()` method is not documented under `Scale` (1) but rather its superclass `Range` (2).
{: .annotate }

1.  

    --8<-- "includes/gtk/callouts/gtkscale.md"

2.  

    --8<-- "includes/gtk/callouts/gtkrange.md"

```py hl_lines="12-17 68-69"
--8<-- "includes/gtk/taiko/11/main.py"
```

1.  

    ```css
    --8<-- "includes/gtk/taiko/11/style.css"
    ```

## 12. HeaderBar


`HeaderBar` (1) is the widget that allows creation of custom title bars for windows.
{: .annotate }

1.  

    --8<-- "includes/gtk/callouts/gtkheaderbar.md"

=== "Builder"

    <div class="grid cards" markdown>
    
    ```py title="main.py"
    --8<-- "includes/gtk/taiko/12/builder.py"
    ```

    ```blueprint hl_lines="9-14" title="main.blp"
    --8<-- "includes/gtk/taiko/12/main.blp"
    ```

    </div>

=== "Procedural"

    ```py hl_lines="12-16"
    --8<-- "includes/gtk/taiko/12/main.py"
    ```

    1.  

        ```css
        --8<-- "includes/gtk/taiko/12/style.css"
        ```

## 13. FileDialog

```py hl_lines="5 14-30 88-97"
--8<-- "includes/gtk/taiko/13/main.py"
```

1.  

    ```css
    --8<-- "includes/gtk/taiko/13/style.css"
    ```

## 14. MenuButton

```py
--8<-- "includes/gtk/taiko/14/main.py"
```

1.  

    ```css
    --8<-- "includes/gtk/taiko/14/style.css"
    ```

## 15. AboutDialog

```py
--8<-- "includes/gtk/taiko/15/main.py"
```

1.  

    ```css
    --8<-- "includes/gtk/taiko/15/style.css"
    ```

## 16. AboutWindow


Implementing `AdwAboutWindow` (1)
{: .annotate }

1.  

    --8<-- "includes/gtk/callouts/adwaboutwindow.md"

```py hl_lines="123-133"
--8<-- "includes/gtk/taiko/16/main.py"
```

1.  

    ```css
    --8<-- "includes/gtk/taiko/16/style.css"
    ```

## 17. Single instancing

```py hl_lines="184 187-188"
--8<-- "includes/gtk/taiko/17/main.py"
```

1.  

    ```css
    --8<-- "includes/gtk/taiko/17/style.css"
    ```

## [18. GridView](https://github.com/Taiko2k/GTK4PythonTutorial/?tab=readme-ov-file#using-gridview)


--8<-- "includes/gtk/taiko/18/info.md"


## 19. Builder

Using Builder we can finally use interface files.

<div class="grid cards" markdown>


```py hl_lines="13-24"
--8<-- "includes/gtk/taiko/19/main.py"
```

```xml
--8<-- "includes/gtk/taiko/19/tutorial.ui"
```

</div>

## Cairo

```py
--8<-- "includes/gtk/taiko/20/main.py"
```

The [DrawingArea][Gtk.DrawingArea] widget can be placed in blueprint.

<div class="grid cards" markdown>

```py hl_lines="21-22"
--8<-- "includes/gtk/taiko/21/main.py"
```

```blueprint hl_lines="19-21"
--8<-- "includes/gtk/taiko/21/main.blp"
```

</div>
