use std::io::stdin;


fn main() {
    println!("Guess the number!");
    let mut guess = String::new();
    stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {}", guess);
}
