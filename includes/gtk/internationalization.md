--8<-- "includes/gtk/gettext/info.md"

GLib [internationalization](https://docs.gtk.org/glib/i18n.html) is implemented through gettext support macros provided in **glib/gi18n.h**.

The `GETTEXT_PACKAGE` preprocessor macro for a library must be defined.
For a Vala project, this can be done by defining the variable through the compiler.

```sh
--8<-- "includes/cmd/valac/valac-x-GETTEXT_PACKAGE.sh"
```

This step is necessary when calling the `textdomain` function to set a gettext text domain.
