use clap::{Command, Arg, crate_version, crate_authors};

fn main() {
    let args = Command::new("Say hello")
        .version(crate_version!())
        .author(crate_authors!())
        .arg(
            Arg::new("name")
                .default_value("World")
        )
        .arg(
            Arg::new("greeting")
                .default_value("Hello")
                .short('g')
                .long("greeting")
        )
        .get_matches();

    println!("{}, {}!", args.get_one::<String>("greeting").unwrap(), args.get_one::<String>("name").unwrap());
}
