`Scale` (1) takes an `Adjustment` (2) object when defined in Blueprint.
However, get and set methods are exposed at the parent widget. (3)
{: .annotate }

1.  

    --8<-- "includes/gtk/callouts/gtkscale.md"

2.  

    --8<-- "includes/gtk/callouts/gtkadjustment.md"

3.  

    --8<-- "includes/gtk/widgets/gtkscale/info.md"


```blueprint title="blp/scale.blp"
--8<-- "includes/gtk/blp/scale.blp"
```

Scale requires at minimum a `width-request` so that it is rendered correctly.
Most of its properties and methods are inherited from `Range` (1)
Other properties:
{: .annotate }

1.  

    --8<-- "includes/gtk/callouts/gtkrange.md"

<!-- -->

-   `width-request` required at minimum so that it does not render as infinitesimally small
-   `digits` determines the precision of the value and is only meaningful when used with `draw-value`
-   `draw-value` when set to true will display a legend above the scale's cursor indicating the value
-   `adjustment` takes an Adjustment object, which defines the range of the scale as well as its default value, which is sticky.
-   `orientation` (optional) horizontal by default

--8<-- "includes/gtk/widgets/gtkscale/marks.md"

In contrast, Vala uses constructors that can specify values for min, max, and increment inline.
However, event handlers are wired to the `adjustment` property. (1)
{: .annotate }

1.  === ":simple-python: PyGObject"

        <div class="grid cards" markdown>

        ```py title="main.py"
        --8<-- "includes/vala/tutorial/03/main.py"
        ```

        ```blueprint hl_lines="11-15 20-24" title="main.blp"
        --8<-- "includes/vala/tutorial/03/main.blp"
        ```


        </div>

    === ":simple-vala: Vala"

        ```vala hl_lines="16 17"
        --8<-- "includes/vala/tutorial/03/main.vala"
        ```

