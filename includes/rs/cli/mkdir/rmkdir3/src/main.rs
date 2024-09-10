fn main() -> std::io::Result<()> {
    let arg = std::env::args().nth(1).unwrap();
    let path = std::path::Path::new(&arg);
    std::fs::create_dir(&path)
}
