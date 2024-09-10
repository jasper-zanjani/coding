// p. 26
use clap::{App, crate_description, crate_authors, crate_name, crate_version};

fn main() {
    let _matches = App::new(crate_name!())
        .author(crate_authors!())
        .about(crate_description!())
        .version(crate_version!())
        .get_matches();

    println!("{:?}", std::env::args());
}