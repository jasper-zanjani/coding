A **trait object** is a reference to a trait type and is formed by specifying a pointer such as a reference or Box smart pointer, then the [dyn](https://doc.rust-lang.org/std/keyword.dyn.html) keyword, then specifying the relevant trait.


```rs
let mut buf: Vec<u8> = vec![];
let writer: &mut dyn Write = &mut buf;

Box<dyn Trait>
```

The [dyn](https://doc.rust-lang.org/std/keyword.dyn.html) keyword is used to highlight that calls to methods on the associated Trait are [**dynamically dispatched**](#dynamic-dispatch). (1)
This requires the trait to be [**object safe**](#object-safety). (2)
{ .annotate }

1. As opposed to static dispatch, [trait objects](#trait-objects) perform [**dynamic dispatch**](https://en.wikipedia.org/wiki/Dynamic_dispatch) when the compiler is unable to determine what method is being called at compile time.
2. Only [object safe traits](https://doc.rust-lang.org/reference/items/traits.html#object-safety) can form the base of a trait object.
Rust documentation distinguishes between **dispatchable** and **non-dispatchable** functions.
Non-dispatchable functions are [Sized](https://doc.rust-lang.org/std/marker/trait.Sized.html), i.e. associated with a type with a constant size known at compile time.
Trait objects are not Sized and so cannot use non-dispatchable functions.

Like any other reference, a trait object points to a value, has a lifetime, and can be either `mut` or shared.
But what makes a trait object special is that the compiler does not know the concrete type of the referent at compile time.

Where a trait object is used, Rust's type system will eusre that any value used in that context will implement the trait object's trait.

Trait objects are similar to objects in other programming languages because they combine data with behavior.
However, trait objects' purpose is to allow abstraction across common behavior.

Here, a trait is specified and a field of the Screen struct is defined as a vecto~r of trait objects.

```rs
pub trait Draw {
    fn draw(&self);
}

pub struct Screen {
    pub components: Vec<Box<dyn Draw>>,
}

impl Screen {
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

In memory, a trait object is a [**fat pointer**](#fat-pointer) consisting of a pointer to the value as well a pointer to the table representing that value's type (the **vtable**).
The vtable is generated once at compile time and shared by all objects of that type.