fn main() {
    let arg = std::env::args().nth(1).unwrap();
    let path = std::path::Path::new(&arg);
    if !path.exists() {
        println!("No such directory found!")
    }
    else { std::fs::remove_dir_all(&path).unwrap() } ;
}
