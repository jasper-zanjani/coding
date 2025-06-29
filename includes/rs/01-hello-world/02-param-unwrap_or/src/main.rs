use std::env::args;

fn main() {
    let default = String::from("World");
    println!("Hello, {}!", args().nth(1).unwrap_or(default));
}
