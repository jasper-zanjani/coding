--8<-- "includes/pygobject/links.md"

Using the [GResource][Gio.Resource] API, files associated with UI (icons, XML, markup, etc) are packaged into a binary resource bundle that can be linked to the executable.
This provides an alternative to manual inclusion of files which brings some benefits, such as memory efficiency and compression.

Resource bundles are created using the **glib-compile-resources** command.
This command is intended to be run from the project's root (i.e. at the parent to **src**) and will create the bundle at this root.

```sh
--8<-- "includes/pygobject/gresources/glib-compile-resources.sh"
```

Here the `file` tag specifies window.ui, which contains a composite template.
This file's path is relative to the argument to `--sourcedir` in the call to glib-compile-resources above.

```xml title="src/gresources.xml"
--8<-- "includes/pygobject/gresources/gresources.xml"
```

The `prefix` attribute of the `gresource` tag defines a shared namespace for all included resources which is included in that of the entire process.
This means that they can be accessed within the application using URIs like "resource:///org/gtk/Example/window.ui".
