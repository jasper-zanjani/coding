# Adwaita

--8<-- "includes/gtk/links.md"

#### ApplicationWindow

[ApplicationWindow][Gtk.ApplicationWindow] will display a HeaderBar by default (not known if this is actually a HeaderBar or some other placeholder widget).
[Adw.ApplicationWindow][Adw.ApplicationWindow] needs [Adw.ToolbarView][Adw.ToolbarView] and [Adw.HeaderBar][Adw.HeaderBar]

<div class="grid cards" markdown>

```blueprint title="Gtk"
--8<-- "includes/gtk/01-boilerplate/main.blp"
```

```blueprint title="Adw" hl_lines="9-12"
--8<-- "includes/gtk/01-boilerplate-adw/main.blp"
```

</div>
