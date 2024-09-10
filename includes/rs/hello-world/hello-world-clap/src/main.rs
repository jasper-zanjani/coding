use clap::{command, arg};

fn main() {
    let args = command!()
        .arg(arg!(<name>).default_value("World").required(false))
        .get_matches();

    println!( "Hello, {}!", args.get_one::<String>("name").unwrap());
}
