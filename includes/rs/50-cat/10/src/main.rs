use std::io::prelude::*;
use std::io::{BufReader, Lines, Result};

fn read_lines(file_path: &str) -> Result<Lines<BufReader<std::fs::File>>> {
    let file = std::fs::File::open(file_path)?;
    Ok(BufReader::new(file).lines())
}

fn main() {
    for file in std::env::args().skip(1) {
        if let Ok(lines) = read_lines(&file) {
            for line in lines {
                if let Ok(contents) = &line {
                    println!("{}", &contents);
                }
            }
        }
    }
}