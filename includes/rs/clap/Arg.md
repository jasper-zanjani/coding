The [Arg][Arg] structs can be defined using the Builder pattern of chained method calls.

- [`short`](https://docs.rs/clap/latest/clap/struct.Arg.html#method.short) sets POSIX-style short option using a char (additional hidden flags can be defined with [**short\_alias**](https://docs.rs/clap/latest/clap/struct.Arg.html#method.short_alias))
- [`long`](https://docs.rs/clap/latest/clap/struct.Arg.html#method.long) defines the long version of the option, omitting the two hyphens
- [`default_value`](https://docs.rs/clap/latest/clap/struct.Arg.html#method.default_value)
- [`subcommand`](https://docs.rs/clap/latest/clap/struct.Command.html#method.subcommand) accepts additional Command structs, allowing a tree-like hierarchy of subcommands (in the style of utilities like git, ip, etc) to be formed.
- [`action`](https://docs.rs/clap/latest/clap/struct.Arg.html#method.action) can define various interesting and useful behavior for the option and accepts an [`ArgAction`](https://docs.rs/clap/latest/clap/enum.ArgAction.html) value: 

    - [`SetTrue`](https://docs.rs/clap/latest/clap/enum.ArgAction.html#variant.SetTrue) 
    provides functionality similar to that of the typical flag.

    - [`Count`](https://docs.rs/clap/latest/clap/enum.ArgAction.html#variant.Count) 
    returns a u8 of the number of times the option was provided


