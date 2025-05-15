!!! info "Board games"

    --8<-- "includes/vala/games.md"

Vala is a language inspired by C# that outputs C code which can then be compiled to run with no extra library support beyond the GNOME platform.

=== ":material-fedora: Fedora"

    ```sh title="Installation"
    --8<-- "includes/vala/00-installation/install.sh"
    ```

<div class="grid cards" markdown>

-   Vala uses [Java/C#-style construction](https://naaando.gitbooks.io/the-vala-tutorial/content/en/4-object-oriented-programming/construction.html) where the constructor method is named after the class and has [no return type](https://naaando.gitbooks.io/the-vala-tutorial/content/en/4-object-oriented-programming/oop-basics.html).

```vala
--8<-- "includes/vala/tutorial/01/main.vala"
```

-   This appears to be the simplest possible class definition possible in Vala, even though the class isn't instantiated.
    Without a static main function that returns a value, we get a compile-time error.

```vala
--8<-- "includes/vala/oop/00/main.vala"
```

-   Here we see that object properties are defined before the constructor.
    Note the strange syntax of instantiating an object (highlighted).

    Vala examples produced by AI still produce classes with a [destructor](https://en.wikipedia.org/wiki/Destructor_(computer_programming)).
    Following C++ convention, it takes the name of the class prepended with [tilde `~`](https://docs.vala.dev/tutorials/programming-language/main/03-00-object-oriented-programming/03-03-destruction.html).

```vala hl_lines="10"
--8<-- "includes/vala/oop/01/main.vala"
```

-   After defining a private property, we find that attempting to access private data is not possible outside the class definition, causing a compile-time error.

```vala hl_lines="3 6 14"
--8<-- "includes/vala/oop/02/main.vala"
```

-   Vala support C#-style [properties](https://docs.vala.dev/tutorials/programming-language/main/03-00-object-oriented-programming/03-05-properties.html) to hide implementation details while exposing public getters and setters.

```vala
--8<-- "includes/vala/oop/03/main.vala"
```

-   All properties of GObjets publish a signal called `notify`.
    This can be disabled by **annotating** them with the `CCode` attribute:

```vala hl_lines="2"
public class MyObject : Object {
    [CCode(notify = false)]
    // notify signal is NOT emitted upon changes in the property
    public int without_notification { get; set; }
    // notify signal is emitted upon changes in the property
    public int with_notification { get; set; }
}
```

-   Appending a question mark to a type allows it to be [null.](https://docs.vala.dev/developer-guides/bindings/writing-a-vapi-manually/05-00-fundamentals-of-binding-a-c-function/05-03-nullability.html)

    The `unowned` keyword creates a weak reference that does not increase the reference count of the target object.
    This allows referenced objects to be destroyed.

=== "main"

    ```vala
    --8<-- "includes/vala/unowned-demo/main.vala"
    ```

=== "Parent"

    ```vala hl_lines="2"
    --8<-- "includes/vala/unowned-demo/parent.vala"
    ```

=== "Child"

    ```vala hl_lines="2"
    --8<-- "includes/vala/unowned-demo/child.vala"
    ```

</div>

#### GTK

```vala title="Basic GTK App"
--8<-- "includes/vala/tutorial/02/main.vala"
```

```sh title="Compile GTK4 app"
valac --pkg gtk4 $SOURCE_FILE
```

=== "Vala"

    ```vala title="Synchronizing widgets"
    --8<-- "includes/vala/tutorial/03/main.vala"
    ```

=== "Python"

    <div class="grid cards" markdown>

    ```py
    --8<-- "includes/vala/tutorial/03/main.py"
    ```

    ```blueprint
    --8<-- "includes/vala/tutorial/03/main.blp"
    ```

    </div>
