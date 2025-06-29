use std::fs::read_to_string;
use clap::{command, arg, ArgAction};

fn main() {
    let args = command!()
        .arg(arg!(<file>).action(ArgAction::Append))
        .get_matches();
    
    for filename in args.get_many::<String>("file").unwrap() {
        println!("{}", read_to_string(filename).unwrap());
    }
}
