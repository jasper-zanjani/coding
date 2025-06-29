use clap::{command, arg};

fn main() {
    let args = command!()
        .arg(arg!(<name>).default_value("World").required(false))
        .arg(arg!(-g --greeting <greeting>).default_value("Hello").required(false))
        .get_matches();
    
    println!("{}, {}!", args.get_one::<String>("greeting").unwrap(), args.get_one::<String>("name").unwrap());
}
