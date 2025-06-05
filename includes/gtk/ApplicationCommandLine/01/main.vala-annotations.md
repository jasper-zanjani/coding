1.  Options are defined using [OptionEntry][OptionEntry-vala], a struct which defines a single option.
    These are collected in a list and then passed to [`add_main_option_entries()`](https://valadoc.org/gio-2.0/GLib.Application.add_main_option_entries.html).

    !!! info "Zeroed-struct terminated array"

        Although it does not appear in GTK documentation, the OptionEntry list must be null-terminated. 
        That is, a final empty struct `{}` must be placed at the end of the list, unless the array has a specified size.
        This is a common C convention.

    Interestingly, the `--help` option appears to be built-in and is enabled or disabled with [`set_help_enabled()`](https://valadoc.org/glib-2.0/GLib.OptionContext.set_help_enabled.html).
    It automatically processes and displays the description provided with the option entries.

2.  In order to process the options, the `command_line()` method is overridden, passing the ApplicationCommandLine object (also named "command\_line".

    A variety of methods are available for extracting the values passed in from command-line: `get_arguments()` ( -> `str[]`) and `get_options_dict()` (-> `VariantDict`).

    Note that arguments are processed as VariantTypes such as `VariantType.STRING` which have to be parsed into native types with methods like `get_string()`.

3.  ApplicationCommandLine will raise a compile-time error if a textdomain is not defined.
    This must be accompanied by definition of the `GETTEXT_PACKAGE` preprocessor macro:

    ```sh
    --8<-- "includes/cmd/valac/valac-x-GETTEXT_PACKAGE.sh"
    ```

    Finally, the application's entrypoint must pass command-line arguments for processing.
