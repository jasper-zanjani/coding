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
