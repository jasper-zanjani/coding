# List-details pattern

--8<-- "includes/pygobject/links.md"

To create a list-details UI pattern, there are two widgets available.
Both are typically used with [Breakpoint][Adw.Breakpoint] to implement reactive functionality at smaller sizes.
Note that Breakpoint does not have to be a child of either view.

-   Unlike in [NavigationSplitView][Adw.NavigationSplitView], in OverlaySplitView only a `sidebar` property exists: the rest of the content is provided as child.

<div class="grid cards" markdown>

-   [**OverlaySplitView**][Adw.OverlaySplitView]

    ---

    --8<-- "includes/pygobject/AdwOverlaySplitView/info.md"

-   [**NavigationSplitView**][Adw.NavigationSplitView]

    ---

    --8<-- "includes/pygobject/AdwNavigationSplitView/info.md"

</div>

## Starships

```py
--8<-- "includes/pygobject/starships/03/main.py"
```

