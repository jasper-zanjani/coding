// https://docs.rs/clap/4.5.9/clap/_tutorial/chapter_1/index.html
use clap::{arg, Command};
use clap::{crate_name, crate_version, crate_description};

fn main() {
    let matches = Command::new(crate_name!())
        .version(crate_version!())
        .about(crate_description!())
        .arg(arg!(--two <VALUE>).required(true))
        .arg(arg!(--one <VALUE>).required(true))
        .get_matches();

    println!("two: {:?}", matches.get_one::<String>("two").expect("required"));
    println!("one: {:?}", matches.get_one::<String>("one").expect("required"));
}