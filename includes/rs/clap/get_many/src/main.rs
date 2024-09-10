use clap::{command, arg, ArgAction};

fn main() {
    let args = command!()
        .arg(arg!(<value>).action(ArgAction::Append))
        .get_matches();

    let values : Vec<&str> = args.get_many::<String>("value").unwrap().map(|s| s.as_str()).collect();
    println!("{:#?}", values);
}
