use clap::{command, arg, Command, Arg};

fn main() {
    let commands = command!()
        .subcommand(Command::new("new").arg(
            arg!(<arg>))
        )
        .subcommand(Command::new("rm").arg(
            arg!(<arg>))
        )
        .get_matches();

    if let Some(new_matches) = commands.subcommand_matches("new") {
        let path = std::path::Path::new(
            new_matches.get_one::<String>("arg").unwrap()
        );
        match std::fs::create_dir(&path) {
            Ok(()) => println!("Created directory: {}", &path.display()),
            Err(e) => eprintln!("Error!: {}", e),
        }
    }

    if let Some(new_matches) = commands.subcommand_matches("rm") {
        let path = std::path::Path::new(
            new_matches.get_one::<String>("arg").unwrap()
        );
        match std::fs::remove_dir_all(&path) {
            Ok(()) => println!("Deleted directory: {}", &path.display()),
            Err(e) => eprintln!("Error!: {}", e),
        }
    }
}
