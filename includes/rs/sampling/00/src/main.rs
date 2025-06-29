use rand::prelude::*;

fn main() {
    let mut rng = rand::rng();
    let mut data = vec![ "Plato", "Aristotle", "Socrates", "Euclid", "Pythagoras", "Hipparcos", "Eratosthenes", ];
    println!("{}", *data.choose_mut(&mut rng).unwrap());
}
