use clap::{command, Arg};

fn main() {
    let args = command!()
        .arg(
            Arg::new("name")
                .value_delimiter(',')
                .default_value("World")
        )
        .get_matches();

    let names : Vec<&str>= args
        .get_many::<String>("name")
        .unwrap()
        .map(|s| s.as_str())
        .collect();
    
    println!("Hello, {}", names.join(", "));
}
// To-do: oxford comma