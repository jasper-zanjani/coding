use std::env::args;

fn main() {
    let arg = args().nth(1).unwrap();
    let parsed_arg: usize = arg.parse().expect("Not a number");
    println!("Parsed integer: {}", parsed_arg);
}
