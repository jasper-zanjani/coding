use std::env::args;
use std::io::Result;

fn main() -> Result<()> {
    println!("Hello, {}!", args().nth(1)?);
    Ok(())
}
