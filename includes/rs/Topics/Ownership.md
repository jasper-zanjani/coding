One of the key and unique features of Rust is the concept of **ownership**, which achieves memory safety without the use of a garbage collector.

The stack and heap are locations in memory that are available to the application at runtime.

- The **stack** is a LIFO that is used for sizes that are known at compile-time. 
It is comparable to a stack of plates of uniform size from which plates can be removed only from the top. 
Values are said to be "**pushed onto**" or "**popped off**" the stack. 

- The **heap** is less organized and less efficient, and is used for sizes that are known only at runtime. 
The operating system must search for an appropriate memory location based on the application's request at runtime, returning a pointer, and this process makes the heap less efficient than the stack. 
Memory locations are said to be "**allocated on**" the heap. 

Some complex data types like **String** are composed of a pointer, stored in the stack because its size is known at compile-time, that points to a location on the heap that holds the String's contents, which are known only at runtime.

In other languages these statements would cause s2 to become a shallow copy of s1, pointing to the same location in memory where the String contents are stored.
However, ownership rules in Rust cause s1 to be invalidated because s2 becomes the owner of the data contents on the heap, and this is called a **move**.

```rs
let s1 = String::from("Hello, world!");
let s2 = s1;
println("{}", s1); // compiler error
```

This allows Rust to avoid the **double free** error caused by attempting to free the same memory location twice, which can cause corruption and security issues.
When the variable goes out of scope, its **backing memory** is freed.

A deep copy is still possible with the common `clone` method:

```rs
let s2 = s1.clone();
```

This behavior is only for data that is stored on the heap, not the stack.
The size of integers is known at compile-time, so they are stored entirely on the stack, and therefore copies of the values are efficiently made.

```rs
let x = 5;
let y = x;
println!("{}",x); // no error
```

More specifically, certain types have a special annotation called the **`Copy` [trait](#trait)** which enable this behavior.
For types that "are `Copy`" - i.e. have the `Copy` trait - an older variable is still usable after assignment.
`Copy` types include integers, booleans, chars, floats, and tuples containing only other `Copy` types.

Function calls also exhibit move behavior; after a variable is passed as argument to a function, the function owns it and it may not be used again in its original context unless ownership is returned.
If the value is not returned, the argument's contents are consumed and it may not be used again in the calling context.

This is why most function calls in Rust use [**references**](#references), prefixing the variable identifier with `&`, a process called **borrowing**.

Passing a value to a function while transferring ownership is called "passing by value" or a **move**, whereas using a reference is called "passing by reference".


=== "Pass by reference"

    ```rs hl_lines="3 7"
    fn main() {
        let s = String::from("Dgiapusccu");
        hello_world(&s);
        println!("Hello again, {}!", s);
    }

    fn hello_world(s:&String) {
        println!("Hello, {}!", s)

    }
    ```

=== "Pass by value"

    ```rs hl_lines="4"
    fn main() {
        let s = String::from("Dgiapusccu");
        hello_world(s);
        println!("Hello again, {}!", s); // compiler error
    }

    fn hello_world(s:String) {
        println!("Hello, {}!", s)

    }
    ```

=== "Return value"

    ```rs hl_lines="3 9"
    fn main() {
        let s = String::from("Dgiapusccu");
        let s = hello_world(s);
        println!("Hello again, {}!", s);
    }

    fn hello_world(s:String) -> String {
        println!("Hello, {}!", s);
        s
    }
    ```