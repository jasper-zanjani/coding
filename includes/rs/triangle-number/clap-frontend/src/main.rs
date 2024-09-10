use clap::{command, arg, value_parser};
use triangle::triangle;

fn main() {
    let args = command!()
        .arg(arg!(<NUMBER>).value_parser(value_parser!(isize)))
        .get_matches();

    let number = *args.get_one("NUMBER").unwrap();
    let result = triangle(number);
    println!("Triangle number of {}: {}", number, result);
}