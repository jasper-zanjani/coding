// https://docs.rs/clap/4.5.9/clap/_tutorial/chapter_2/index.html
use clap::{command, Arg};

fn main() {
    let matches = command!() // requires `cargo` feature
        .arg(Arg::new("name")
            .value_parser(clap::builder::NonEmptyStringValueParser::new())
        )
        .get_matches();

    println!("Arg: {}", matches.get_one::<String>("name").unwrap());
}