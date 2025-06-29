use clap::{command, arg, value_parser, ArgAction};
use std::path::PathBuf;
use std::fs::read_to_string;

fn main() {
    let args = command!()
        .arg(arg!(<file>).action(ArgAction::Append).value_parser(value_parser!(PathBuf)))
        .get_matches();
    
    for filename in args.get_many::<PathBuf>("file").unwrap() {
        println!("{}", read_to_string(filename).unwrap());
    }

}
