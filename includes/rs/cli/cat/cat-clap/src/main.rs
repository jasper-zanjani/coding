use clap::{command, arg, ArgAction, value_parser};
use std::path::PathBuf;

fn main() {
    let args = command!()
        .arg(
            arg!(<file>)
                .action(ArgAction::Append)
                // .value_parser(value_parser!(PathBuf))
        )
        .get_matches();
    
    let filenames = args
        .get_many::<String>("file")
        .unwrap()
        // .map(|s| s.as_str())
        // .map(|i| println!("{:#?}", i));
        .collect::<Vec<String>>();
        
    for filename in filenames {
        let path = std::path::Path::new(&filename);
        {
            if let Ok(contents) = std::fs::read_to_string(&filename) {
                println!("{}", &contents);
            };
        }
    };
}
