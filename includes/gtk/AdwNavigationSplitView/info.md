[NavigationSplitView][Adw.NavigationSplitView] (1) is simpler than OverlaySplitView.
Although it also has `sidebar` asnd `content` properties to accept children, in this case they must both be [NavigationPages][Adw.NavigationPage].
[NavigationSplitView][Adw.NavigationSplitView] does not support the `show-sidebar` property.
{: .annotate}

1.  

    ```blueprint hl_lines="11 19" title="Basic example"
    --8<-- "includes/gtk/AdwNavigationSplitView/00/main.blp"
    ```

The [ToolbarView][Adw.ToolbarView] and [Headerbar][Adw.HeaderBar] must be defined for both `sidebar` and `content` for the entire widget to look right. (1)
If one or the other is missing, that section of the window will not function properly.
In this case both sidebar and content have `show-title` enabled.
{: .annotate }

1.  

    ```blueprint hl_lines="10-14 39-43"
    --8<-- "includes/gtk/AdwNavigationSplitView/01/main.blp"
    ```

In this final iteration, a [Breakpoint][Adw.Breakpoint] is used to collapse the split view at a set size which then displays a previously hidden button. (1)
{: .annotate }

1.  

    ```blueprint hl_lines="10-17"
    --8<-- "includes/gtk/AdwNavigationSplitView/99/main.blp"
    ```
