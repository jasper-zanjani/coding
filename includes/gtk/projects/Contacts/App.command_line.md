This method overrides the virtual function provided by the Gio.Application class.
It first calls [`activate`](https://api.pygobject.gnome.org/Gio-2.0/class-Application.html#gi.repository.Gio.Application.activate), causing MainWindow to appear.
It then determines which options were passed from the command-line by testing for the existence of strings in the VariantDict returned by [`get_options_dict`](https://api.pygobject.gnome.org/Gio-2.0/class-ApplicationCommandLine.html#gi.repository.Gio.ApplicationCommandLine.get_options_dict)
