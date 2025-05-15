# Overview

--8<-- "includes/pygobject/links.md"

!!! info "Quick Reference"

    --8<-- "includes/pygobject/callout.md"

There are various sources of GTK source code made available for study

-   Workbench demos: The repo has been cloned to **~/.local/src/demos** but these demos mostly appear to use [`Adw.StatusPage`][Adw.StatusPage] as the document root.

## Data binding

Although naive data binding can apparently be done by setting event handlers between two widgets (ref. [Scale](#scale) below), Blueprint allows a deeper two-way data binding to be created very simply, by using the `bind` keyword and specifying the target property.

```blueprint hl_lines="11"
--8<-- "includes/pygobject/98-bind/main.blp"
```

## Scale

[Scale][Gtk.Scale] and [SpinButton][Gtk.SpinButton] take an [Adjustment][Gtk.Adjustment] object when defined in Blueprint.
However, get and set methods are exposed at the parent widget.

In contrast, Vala uses constructors that can specify values for min, max, and increment inline.
However, event handlers are wired to the `adjustment` property.

=== "Python"

    <div class="grid cards" markdown>

    ```py title="main.py"
    --8<-- "includes/vala/tutorial/03/main.py"
    ```

    ```blueprint hl_lines="11-15 20-24" title="main.blp"
    --8<-- "includes/vala/tutorial/03/main.blp"
    ```


    </div>

=== "Vala"

    ```vala hl_lines="16 17"
    --8<-- "includes/vala/tutorial/03/main.vala"
    ```

## CSS

Slight variations to how to add a [CssProvider][Gtk.CssProvider].
[StyleContext][Gtk.StyleContext] is deprecated since 4.10 so I have no clue how this approach should change into the future.

<div class="grid cards" markdown>

```py title="From Taiko's tutorial"
# Loading CSS file
css_provider = Gtk.CssProvider()
css_provider.load_from_path('style.css') # 

Gtk.StyleContext.add_provider_for_display(
        Gdk.Display.get_default(), 
        css_provider, 
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
```

```py title="Produced by Gemini"
# Providing CSS definitions in a multiline string
css = # ...
css_provider = Gtk.CssProvider()
css_provider.load_from_data(css.encode())

# Apply the CSS to the style context of the target element
style_context = box.get_style_context()
style_context.add_provider(
        css_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_USER)
```

</div>

## Containers and children

There are two kinds of [container](https://docs.gtk.org/gtk3/class.Container.html) in GTK, both of which are subclasses of the abstract GtkContainer base class:

-   Subclasses of GtkBin have a single child
-   Others can have more than one child

## [Templates](https://developer.gnome.org/documentation/tutorials/widget-templates.html)

What is the purpose of Gtk.Template?

<div class="grid cards" markdown>

```py hl_lines="4 8"
--8<-- "includes/pygobject/text-editor/00/window.py"
```

```py hl_lines="4 8"
--8<-- "includes/pygobject/text-editor/01/window.py"
```

</div>

