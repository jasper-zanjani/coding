fn main() {
    let arg = std::env::args().nth(1).unwrap();
    std::fs::create_dir(&arg).unwrap();
}
