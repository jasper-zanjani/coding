You have a good foundation in how to read GTK code, refactor simple examples, and to be somewhat more creative. 
You have to begin getting a broader understanding of how and where widgets are used.
Work through the Workbench examples, recreating them in Python.
Find useful examples of GTK layouts that can be replicated or adapted.

-   [ ] Starships list-details pattern using [Adw.OverlaySplitView][Adw.OverlaySplitView] or Adw.NavigationSplitView (like in [GNOME Contacts](https://gitlab.gnome.org/GNOME/gnome-contacts/))

    -   Database demo uses `SignalListItemFactory` and `Gio.ListStore`
    -   List View uses `BuilderListItemFactory`
    -   Incorporate Avatar

-   [ ] Study Tic-tac-toe game produced by Gemini

-   [ ] Study Cairo on its own. Maybe you can incorporate it with GTK later on.

-   [ ] Experiment with the web-based GTK backend [Broadway](https://docs.gtk.org/gtk4/broadway.html)

-   Study the many GTK4 applications on [valpackett/awesome-gtk](https://github.com/valpackett/awesome-gtk?tab=readme-ov-file#journaling), Python and Vala

    -   Download repos and see if they contain Blueprint files
    -   Do they mention Snapshot or other interesting widgets?
    -   Do they work with Cairo, GSK or other libraries?
    -   Commonalities between projects.
    -   Characterize projects by difficulty: maybe you can work your way up in Vala


-   [x] Study [templates](https://developer.gnome.org/documentation/tutorials/widget-templates.html) since that features prominently in the other tool that you are supposed to be working with, Builder.
    This will probably involve:

    1.  Wrapping the widgets in a template element with a specific `class` attribute value
    2.  Decorating that class in Python code with `@Gtk.Template(resource_path=...)`

-   [x] Follow the [official GNOME tutorial](https://developer.gnome.org/documentation/tutorials/beginners/getting_started.html) which should fill in the gaps for the text-editor tutorial video you watched a few days ago.
    Maybe follow the Vala version as well to get a handle on the syntax?

-   [x] Now that you have completed a couple of tutorials, you have to become more familiarized with Blueprint files since they are so obviously superior to XML UI definitions.
    This will allow you to use the demos in Workbench, especially once you work out how to put those demos into a separate application.

-   [x] Go back through the tutorials and rework them to use Builder objects with Blueprint files.
    Discard the pug files since they are not useful.


