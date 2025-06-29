use std::io::stdin;
use rand::Rng;


fn main() {
    println!("Guess the number!");
    let secret_number = rand::rng().random_range(1..=100);
    println!("Secret number: {secret_number}");
    let mut guess = String::new();
    stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {}", guess);
}
