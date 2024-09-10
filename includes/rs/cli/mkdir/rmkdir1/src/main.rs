fn main() {
    let arg = std::env::args().nth(1).unwrap();
    let path = std::path::Path::new(&arg);
    if path.exists() {
        println!("{} already exists!", &arg);
    }
    else {
        std::fs::create_dir(&path).unwrap();
    }
}
