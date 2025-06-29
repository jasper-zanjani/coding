use rand::prelude::*;
use std::env::args;

fn main() {
    let mut rng = rand::thread_rng();

    match args().last().unwrap().as_str() {
        "integers" => {
            let mut data = [1, 2, 4, 8, 16, 32];
            println!("{}", data.choose_mut(&mut rng).unwrap());
        }
        "strings" => {
            let mut data: Vec<&str> = vec![
                "Plato",
                "Aristotle",
                "Socrates",
                "Euclid",
                "Pythagoras",
                "Hipparcos",
                "Eratosthenes",
            ];
            println!("{}", *data.choose_mut(&mut rng).unwrap());
        }
        _ => eprintln!("Invalid command!"),
    }
}
