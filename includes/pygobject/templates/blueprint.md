In [blueprint](https://gnome.pages.gitlab.gnome.org/blueprint-compiler/reference/templates.html), a **template** (1) is declared using the `template` keyword and followed by the custom class name **prepended with `$`**.
{: .annotate }

1.  

    --8<-- "includes/pygobject/templates.md"

<div class="grid cards" markdown>

```blueprint
template $FooWidget : Box {}
```

```xml
<interface>
  <template class="FooWidget" parent="GtkBox">
    <!-- snip -->
  </template>
</interface>
```

</div>

This template fragment is bundled with the project using GResource.
