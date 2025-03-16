
=== "Ownership"

    --8<-- "includes/rs/Topics/Ownership.md"

=== "Data"

    --8<-- "includes/rs/Topics/Data.md"

=== "Numbers"

    --8<-- "includes/rs/Topics/Numbers.md"

=== "Compound types"

    --8<-- "includes/rs/Topics/Compound.md"


=== "Documentation"

    --8<-- "includes/rs/Topics/Documentation.md"

=== "OOP"

    Strictly speaking, OOP is not actually implemented in Rust because there is no inheritance.
    However, objects that combine data with logic can be created `struct`s and `impl`s.

    A group of methods that are shared by multiple types can have their signatures defined by a [**trait**](#trait).
    Types then implement the trait, and functions can be defined that accept any type that does so by specifying the trait instead of a single concrete type.

    ```rs
    pub fn notify(item: impl Summary) {
        println!("Breaking news! {}", item.summarize());
    }
    ```

=== "Concurrency"

    --8<-- "includes/rs/Topics/Concurrency.md"


=== "References"

    --8<-- "includes/rs/Topics/References.md"

=== "Copy and Clone"

    Rust provides two [traits](#traits) that relate to the copying of data: [**Copy** and **Clone**](https://doc.rust-lang.org/book/appendix-03-derivable-traits.html?highlight=clone#clone-and-copy-for-duplicating-values).

    - **Copy** allows values stored on the **stack only** to be duplicated. Any type whose parts all implement Copy can also derive Copy. However, this trait is rarely required since primitives stored on the stack already have optimizations available. In the background this relies on the **memcpy** syscall.

    - [std][std]::[**Clone**](https://doc.rust-lang.org/std/clone/index.html) is for explicitly creating a **deep copy** of values, especially those allocated on the heap. Types that implement Copy also trivially implement Clone. 

=== "Collections"

    Accessing tuple elements is done with the **`.`** operator

    ``` rs
    let coord: (i8, i8) = (10, 20);
    println!("{}, {}", coord.0, coord.1);
    ```

=== "Structs"

    **Implementation blocks** allow the definitions of functions within the context of structs (i.e. methods).
    Fields are defined within the struct block.

=== "Traits"

    --8<-- "includes/rs/Topics/Traits.md"

=== "Trait bounds"

    --8<-- "includes/rs/Topics/Trait-Bounds.md"

=== "Trait objects"

    --8<-- "includes/rs/Topics/Trait-Objects.md"

=== "Self"

    --8<-- "includes/rs/Topics/Self.md"

=== "Enums"

    [Option](https://doc.rust-lang.org/std/option/enum.Option.html)

    --8<-- "includes/rs/Topics/Option.md"

    [Result](https://doc.rust-lang.org/std/result/enum.Result.html)

    --8<-- "includes/rs/Topics/Result.md"


=== "Testing"

    --8<-- "includes/rs/Topics/Tests.md"

=== "Attributes"

    --8<-- "includes/rs/Topics/Attributes.md"

=== "match"

    --8<-- "includes/rs/Topics/Match.md"

