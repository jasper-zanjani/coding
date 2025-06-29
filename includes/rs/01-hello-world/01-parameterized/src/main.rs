use std::env::args;

fn main() {
    println!("Hello, {}!", args().nth(1).unwrap());
}
