fn main() {
    let arg = std::env::args().nth(1).unwrap();
    let path = std::path::Path::new(&arg);
    match path.exists() {
        true => println!("{} already exists!", &arg),
        _ => std::fs::create_dir(&path).unwrap(),
    };
}
