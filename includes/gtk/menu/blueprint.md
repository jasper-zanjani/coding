[Menus in blueprint](https://gnome.pages.gitlab.gnome.org/blueprint-compiler/reference/menus.html) are defined using `menu`.
Blueprint offers a shorthand syntax for creating menus.
Instead of defining the `label`, `action`, and `icon` fields separately, you can provide their values in that order.
Note the lack of a semicolon for the shorthand definition of each item.

<div class="grid cards" markdown>

```blueprint title="Default menu created by new Builder project"
--8<-- "includes/gtk/builder/menu.blp"
```

```blueprint title="Using shorthand"
--8<-- "includes/gtk/builder/menu-shorthand.blp"
```

</div>

The menu can then be referenced by its id as the value of the `menu-model` property of an appropriate widget, like [MenuButton][Gtk.MenuButton].
