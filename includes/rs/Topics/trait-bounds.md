Using **trait bounds**, any type that implements a trait can be specified as a function parameter instead of a concrete type. 
Calling a function with a type that does not implement the trait will cause a compile time error.

This syntax uses the **impl** keyword followed by the trait name where a concrete type would otherwise occur in a function signature.
Similar syntax exists for return types, although the compiler will enforce only a single concrete return type.

Using trait bounds is very similar to using generics.
The following signatures as equivalent in that they will accept any type that can be converted into str.

```rs title="Equivalent"
fn function strlen(s: impl AsRef<str>) -> usize;

fn strlen<S>(s: S) -> usize
where
    S: AsRef<str>;
```

During compilation the compiler performs **monomorphization**, which means that nongeneric implementations of functions and methods are generated for each concrete used with a generic.

Multiple trait bounds can be provided with **`+`**.
**Where clauses** are also available to more legibly define trait bounds for each generic.


```rs title="Equivalent"
fn function<T: Display + Clone, U: Clone + Debug>(t: T, u: U) -> i32;

fn function<T, U>(t: T, u: U) -> i32
where 
    T: Display + Clone,
    U: Clone + Debug
```