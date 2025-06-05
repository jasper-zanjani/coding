1.  [OptionEntry][OptionEntry-py] defines a command-line option.
    Unlike in Vala, in Python the constructor for OptionEntry takes no arguments and must be built up by setting its properties up procedurally.

    [`add_main_option_entries()`](https://api.pygobject.gnome.org/Gio-2.0/class-Application.html#gi.repository.Gio.Application.add_main_option_entries) takes a list of OptionEntry.

2.  The [`do_command_line`](https://api.pygobject.gnome.org/Gio-2.0/class-Application.html#gi.repository.Gio.Application.do_command_line) signal handler is overridden, as in Vala.
    Note that this method must return an int!

    VariantType in PyGObject does not have the `STRING` enum, but is initialized by a type string that defines the type.
    It appears that explicitly calling the `get_string()` method may not be necessary, since a Python string is returned when using it in a string-like way.

3.  The [`do_activate`](https://api.pygobject.gnome.org/Gio-2.0/class-Application.html#gi.repository.Gio.Application.do_activate) method must be implemented.

4.  It is probably the case that [ApplicationFlags][ApplicationFlags-py] can be implemented in several places, as `application_id` can.
