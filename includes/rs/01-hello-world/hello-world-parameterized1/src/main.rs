fn main() {
    match &std::env::args().nth(1).unwrap() as &str {
        "greet" => println!("Greetings, {}!", std::env::args().nth(2).unwrap()),
        _ => println!("Hello, {}!", std::env::args().nth(1).unwrap())
    }
}