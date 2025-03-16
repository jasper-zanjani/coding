**match** is a control flow operator that allows comparison of values against a series of patterns.
A match expression is composed of several **match arms**, each of which can return a value or an expression with a value that is returned.

```rs
enum Coin { Penny, Nickel, Dime, Quarter }

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25
    }
}
```

Closely related is **if let** which is syntactic sugar for a pattern that matches one pattern while ignoring the rest.
Notably, the syntax takes the pattern before the expression similar to a match arm.


<div class="grid cards" markdown>

-   #### if let

    ---

    ``` rs
    let some_u8_value = Some(0u8);

    if let Some(3) = some_u8_value {
        println!("three");
    }
    ```

-   #### match

    ---

    ``` rs
    let some_u8_value = Some(0u8);
    
    match some_u8_value {
        Some(3) => println!("three"),,
        _ => (),
    }
    ```

</div>