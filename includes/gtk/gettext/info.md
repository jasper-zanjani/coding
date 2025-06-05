GNU gettext (1)is a widely used tool for internationalization of open software, especially in C but with support for other languages.
{: .annotate }

1.  

    --8<-- "includes/gtk/gettext/callout.md"

Using gettext, software is [prepared](https://www.gnu.org/software/gettext/manual/html_node/Sources.html) for internationalization in a variety of ways.

-   When using GNU gettext, each application has its own **text domain**, a unique name that identifies the application (perhaps we would say nowadays that it defines its own namespace).
    This domain is defined by a call to the `textdomain` function.

-   PO files ("portable object"), following a [specific format](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html), facilitate the management of translations.

-   `xgettext` aids in the creation of PO files by extracting translatable strings.

