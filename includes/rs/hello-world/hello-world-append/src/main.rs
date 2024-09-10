use clap::{command, arg, ArgAction};

fn main() {
    let args = command!() .arg( arg!(<name>).action(ArgAction::Append).default_value("World")).get_matches();

    let names: Vec<String> =  args
        .get_many::<String>("name")
        .unwrap()
        .map(|s| String::from(s))
        .collect();
    
    println!("Hello, {}!", names.join(", "));
}
// To-do: oxford comma
