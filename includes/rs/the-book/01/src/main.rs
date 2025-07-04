use std::io::stdin;


fn main() {
    println!("Guess the number!");
    let mut guess = String::new();
    stdin()
        .read_line(&mut guess)
        .and_then(proces_string)
        .expect("Failed to read line");
}

fn process_string(input: String) -> Result<(), E> {
    println!("You guessed: {}", input);
}
