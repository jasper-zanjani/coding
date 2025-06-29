fn main() {
    for arg in std::env::args().skip(1) {
        println!("{}", std::fs::read_to_string(arg).unwrap());
    }
}
