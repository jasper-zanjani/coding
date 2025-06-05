GTK supports limited parsing of command-line options through **ApplicationCommandLine** (1), which represents a command-line invocation of an application.
{: .annotate }

1.  **Resources**

    -   [:simple-python: ApplicationCommandLine][ApplicationCommandLine-pygobject]
    -   [:simple-vala: ApplicationCommandLine][ApplicationCommandLine-vala]

Implementation is not trivial.
The following appears to be the simplest possible implementation.

=== ":simple-python: Python"

    ```py
    --8<-- "includes/gtk/ApplicationCommandLine/01/main.py"
    ```

    --8<-- "includes/gtk/ApplicationCommandLine/01/main.py-annotations.md"

=== ":simple-vala: Vala"

    ```vala
    --8<-- "includes/gtk/ApplicationCommandLine/01/main.vala"
    ```

    --8<-- "includes/gtk/ApplicationCommandLine/01/main.vala-annotations.md"

    Compiling this example requires definition of the `GETTEXT_PACKAGE` preprocessor macro, which must match the string passed to `Intl.textdomain`.

    ```sh title="Compilation"
    --8<-- "includes/cmd/valac/valac-x-GETTEXT_PACKAGE.sh"
    ```
