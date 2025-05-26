[Breakpoint][Adw.Breakpoint] describes a breakpoint for Window or Dialog, intended for use in adaptive UI.
There are two main settings:

-   `condition` takes a string that must be parsed (note that it does not a semicolon)
-   `setters` determines what property values are changed when the condition is met

```blueprint
Adw.Breakpoint {
  condition ("max-width: 560sp")

  setters {
    split_view.collapsed: true;
  }
}
```

