use clap::{command, arg, value_parser};
use std::thread::spawn;

fn main() {
    let args = command!()
        .arg(arg!(<name>).default_value("World").required(false))
        .arg(arg!(-t --threads <threads>)
            .value_parser(value_parser!(u8))
            .default_value("1")
            .required(false))
        .get_matches();

    let name = args.get_one::<String>("name").unwrap();
    let thread_num = *args.get_one::<u8>("threads").unwrap();
    let mut threads = vec![];

    for i in 0..thread_num {
        threads.push(spawn(move || {
            println!("Hello, {}!", name);
        }));
    }

    for t in threads {
        t.join().unwrap();
    }
}

