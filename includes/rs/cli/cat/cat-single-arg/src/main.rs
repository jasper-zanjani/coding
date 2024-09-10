fn main() {
    for arg in std::env::args().skip(1) {
        if let Ok(contents) = std::fs::read_to_string(arg) {
            println!("{}", &contents);
        }
    }
}