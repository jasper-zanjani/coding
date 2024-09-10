use rand::prelude::SliceRandom;

fn main() {
    let mut rng = rand::thread_rng();

    match &std::env::args().nth(1).unwrap() as &str {
        "integers" => {
            let data = [1, 2, 4, 8, 16, 32];
            println!("{}", data.choose(&mut rng).unwrap());
        }
        "strings" => {
            let data: Vec<&str> = vec![
                "Plato",
                "Aristotle",
                "Socrates",
                "Euclid",
                "Pythagoras",
                "Hipparcos",
                "Eratosthenes",
            ];
            println!("{}", *data.choose(&mut rng).unwrap());
        }
        _ => eprintln!("Invalid command!"),
    }
}