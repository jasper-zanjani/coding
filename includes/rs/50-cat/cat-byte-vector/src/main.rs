use clap::{command, arg, Command};

fn main() {
    let matches = command!()
        .arg(arg!(<file>))
        .get_matches();
    
    if let Some(arg)  = matches.get_one::<String>("file") {
        let path = std::path::Path::new(arg);
        {
            if let Ok(bytes) = std::fs::read(&path) {
                if let Ok(content) = std::str::from_utf8(&bytes) {
                    println!("{}", &content);
                };
            };
        }
    };
}
