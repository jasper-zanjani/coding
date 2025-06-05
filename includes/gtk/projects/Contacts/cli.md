[Gio.ApplicationCommandLine][Gio.ApplicationCommandLine] represents a command-line invocation of an application.
It is emitted in the `command_line` signal and virtual function of the Application class.

App also exposes an OptionEntry list which supports command-line options.
These are passed to `add_main_option_entries()` in the App constructor.
