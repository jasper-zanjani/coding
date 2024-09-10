use clap::{command, arg, value_parser};

fn main() {
    let args = command!()
        .arg(
            arg!(<int> "Enter a number to be parsed as u8")
                .value_parser(value_parser!(usize))
        )
        .get_matches();
    if let Some(int) = args.get_one::<usize>("int") {
        println!("{}", int);
    }
}
