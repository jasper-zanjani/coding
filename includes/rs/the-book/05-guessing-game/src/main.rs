use std::cmp::Ordering;
use std::io::stdin;
use rand::Rng;


fn main() {
    println!("Guess the number!");
    let secret_number = rand::rng().random_range(1..=100);
    loop {
        let mut guess = String::new();
        println!("Enter guess:");
        stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        let guess: usize = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("Correct!");
                break;
            }
        }
    }
}
