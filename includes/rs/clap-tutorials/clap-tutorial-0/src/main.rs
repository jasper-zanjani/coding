// https://docs.rs/clap/4.5.9/clap/_tutorial/chapter_0/index.html
use clap::{arg, command, value_parser, ArgAction, Command};
use std::path::PathBuf;

fn main() {
    let matches = command!()
        .arg(arg!([name] "Optional name to operate on"))
        .arg(arg!(-c --config <FILE> "Sets a custom config file").required(false)
            .value_parser(value_parser!(PathBuf)))
        .arg(arg!(-d --debug ... "Turn debugging information on"))
        .subcommand(Command::new("test")
            .about("does testing things")
            .arg(arg!(-l --list "lists test values").action(ArgAction::SetTrue)))
        .get_matches();

    if let Some(name) = matches.get_one::<String>("name") {
        println!("Value for name: {name}");
    }

    if let Some(config_path) = matches.get_one::<PathBuf>("config") {
        println!("Value for config: {}", config_path.display());
    }

    match matches.get_one::<u8>("debug").expect("Counts are defaulted") {
        0 => println!("Debug mode is off"),
        1 => println!("Debug mode kind of on"),
        2 => println!("Debug mode is really on"),
        _ => println!("Unacceptable"),
    }

    if let Some(matches) = matches.subcommand_matches("test") {
        if matches.get_flag("list") {
            println!("Printing testing lists...");
        } else {
            println!("Not printing testing lists...");
        }
    }
}
