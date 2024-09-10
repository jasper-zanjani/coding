use clap::{command, Arg, arg, ArgAction};

fn main() {
    let args = command!()
        .arg(
            Arg::new("count")
                .short('c')
                .action(ArgAction::Count)
        )
        .get_matches();

    println!(
        "count: {:?}", 
        args.get_count("count")
    );
}