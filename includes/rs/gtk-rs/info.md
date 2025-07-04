gtk-rs (1)
{: .annotate }

1.  

    --8<-- "includes/rs/gtk-rs/callout.md"

```rs
# Install GTK 4 and the build essentials
dnf install -y gtk4-devel gcc
```

The cargo project must also add dependencies.

```sh
cargo add gtk4 --rename gtk --features v4_12

# The version specified in the feature must match the version of GTK4 installed on the system.
# On Fedora 38, GTK 4.10.5 is installed.
cargo add gtk4 --rename gtk --features v4_10
```

## Tasks

#### Hello, World!

```rs
--8<-- "includes/rs/gtk-rs/hello-world/src/main.rs"
```

The Button widget implements [interfaces](https://gtk-rs.org/gtk4-rs/git/book/widgets.html) in C which have equivalents in Rust:

<div class="grid cards" markdown>

-   
    - [GtkAccessible](https://docs.gtk.org/gtk4/iface.Accessible.html)
    - [GtkActionable](https://docs.gtk.org/gtk4/iface.Actionable.html)
    - [GtkBuildable](https://docs.gtk.org/gtk4/iface.Buildable.html)
    - [GtkConstraintTarget](https://docs.gtk.org/gtk4/iface.ConstraintTarget.html)

-   
    - [AccessibleExt](https://gtk-rs.org/gtk4-rs/stable/latest/docs/gtk4/prelude/trait.AccessibleExt.html)
    - [ActionableExt](https://gtk-rs.org/gtk4-rs/stable/latest/docs/gtk4/prelude/trait.ActionableExt.html)
    - [BuildableExt](https://gtk-rs.org/gtk4-rs/stable/latest/docs/gtk4/prelude/trait.BuildableExt.html)
    - [ConstraitTargetExt](https://gtk-rs.org/gtk4-rs/stable/latest/docs/gtk4/prelude/trait.ConstraintTargetExt.html)

</div>

GTK is an object-oriented framework written in a language which does not support object-orientation out of the box.
This is why GTK relies on the GObject library to provide the object system.
GObject concepts like inheritance and interfaces are [mapped](https://gtk-rs.org/gtk4-rs/git/book/g_object_concepts.html) to Rust traits.
