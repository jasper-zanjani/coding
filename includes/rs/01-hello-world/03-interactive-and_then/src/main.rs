use std::io::stdin;

fn main() {
    println!("Enter name: ");
    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();
    process_string(input);
}

fn process_string(input: String) -> Result {
    let name = input.trim();
    println!("Hello, {}!", name);
}
