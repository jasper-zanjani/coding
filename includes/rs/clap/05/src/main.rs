use clap::{command, Arg, arg, ArgAction};

fn main() {
    let args = command!()
        .arg(Arg::new("count").short('c').action(ArgAction::Count))
        .arg(arg!(-b --bee ... ))
        .get_matches();

    println!( "c: {:?}", args.get_count("count"));
    println!("b: {:?}", args.get_count("bee"));
}
