use clap::{command, Arg, arg, ArgAction};

fn main() {
    let args = command!()
        .arg(
            Arg::new("bool")
                .short('b')
                .action(ArgAction::SetTrue)
        )
        .get_matches();

    println!(
        "bool: {:?}", 
        args.get_flag("bool")
    );
}