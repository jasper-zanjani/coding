use clap::{arg, command, ArgAction};

type MyResult<T> = Result<T, Box<dyn Error>>;

#[derive(Debug)]
struct Config {
    files: Vec<String>,
    lines: bool,
    words: bool,
    bytes: bool,
    chars: bool,
}

fn get_args() -> MyResult<Config> {
    
    let args = command!()
        .arg(arg!(<files>).default_value("-"))
        .arg(arg!(-w --words <words>).action(ArgAction::SetTrue))
        .arg(arg!(-c --bytes <bytes>).action(ArgAction::SetTrue))
        .arg(arg!(-m --chars <chars>).action(ArgAction::SetTrue))
        .arg(arg!(-l --lines <lines>).action(ArgAction::SetTrue))
        .get_matches();
    
    Ok( Config {

    })
}

fn main() {
    config = get_args()
}