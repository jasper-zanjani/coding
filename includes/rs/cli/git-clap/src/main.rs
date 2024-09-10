use clap::{command, Command, arg, Arg};

fn main() {
    let git = Command::new("git")
        .subcommand(command!("clone").arg(Arg::new("clone_arg")))
        .subcommand(command!("commit").arg(Arg::new("commit_arg")))
        .subcommand(command!("push").arg(Arg::new("push_arg")))
        .get_matches();

    match git.subcommand_name() {
        Some("clone")  => {println!("subcommand: clone")}, // clone was used
        Some("push")   => {println!("subcommand: push")}, // push was used
        Some("commit") => {println!("subcommand: commit")}, // commit was used
        _              => {}, // Either no subcommand or one not tested for...
    }

    if let Some(clone_matches) = git.subcommand_matches("clone") {
        println!("clone argument: {}",clone_matches.get_one::<String>("clone_arg").unwrap());
    }

    if let Some(commit_matches) = git.subcommand_matches("commit") {
        println!("commit argument: {}", commit_matches.get_one::<String>("commit_arg").unwrap());
    }

    if let Some(push_matches) = git.subcommand_matches("push") {
        println!("push argument: {}", push_matches.get_one::<String>("push_arg").unwrap());
    }

}