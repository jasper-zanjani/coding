use clap::{command, arg};

fn main() {
    let args = command!()
        .arg(arg!(<name>))
        .get_matches();
    println!("Hello, {}!", args.get_one::<String>("name").unwrap());
}
