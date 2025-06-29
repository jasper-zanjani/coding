# Overview

--8<-- "includes/gtk/links.md"

There are various sources of GTK source code made available for study

-   [Workbench demos][Workbench-git]: The repo has been cloned to **~/.local/src/demos** but these demos mostly appear to use [`Adw.StatusPage`][Adw.StatusPage] as the document root.

## Containers and children

There are two kinds of [container](https://docs.gtk.org/gtk3/class.Container.html) in GTK, both of which are subclasses of the abstract GtkContainer base class:

-   Subclasses of GtkBin have a single child
-   Others can have more than one child

