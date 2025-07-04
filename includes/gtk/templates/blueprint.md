In [Blueprint](https://gnome.pages.gitlab.gnome.org/blueprint-compiler/reference/templates.html), a **template** (1) is declared using the `template` keyword and followed by the custom class name **prepended with `$`**.
{: .annotate }

1.  

    --8<-- "includes/gtk/templates.md"


```blueprint
template $FooWidget : Box {} // (1)
```

1.  

    ```xml title="Compiled output"
    <interface>
      <template class="FooWidget" parent="GtkBox">
        <!-- snip -->
      </template>
    </interface>
    ```


This template fragment is bundled with the project using GResource.
