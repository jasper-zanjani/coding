use clap::{command, arg};

fn main() {
    let args = command!()
        .arg(
            arg!(<int> "Enter a number to be parsed as u8")
        )
        .get_matches();
    if let Some(int) = args.get_one::<String>("int") {
        println!("{}", int.parse::<usize>().unwrap());
    }
}
