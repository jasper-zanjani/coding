use clap::{command, arg};
use std::io::{BufRead};

fn main() {
    let matches = command!().arg(arg!(<file>)).get_matches();
    if let Some(arg) = matches.get_one::<String>("file") {
        let path = std::path::Path::new(&arg);

        if let Ok(file) = std::fs::File::open(&path) {
            let reader = std::io::BufReader::new(&file);

            for line in reader.lines() {
                if let Ok(content) = line {
                    println!("{}", &content);
                }
            }
        }
    }
    println!("Hello, world!");
}
