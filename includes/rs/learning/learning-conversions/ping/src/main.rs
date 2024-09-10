use std::net::Ipv4Addr;

fn ping<A>(address: A) -> std::io::Result<bool>
    where A: Into<Ipv4Addr> 
    {
        let ipv4_address = address.into();
        Ok(true)
    }
    
fn main() {
    println!("{:?}", ping(Ipv4Addr::new(192, 168, 0, 1)));

    // Conveniently, u32 and [u8;4] implement Into<Ipv4Addr>
    println!("{:?}", ping([192, 168, 0, 1]));

    let bytes = [192, 168, 0, 1];
    println!("{:?}", ping(u32::from_ne_bytes(&bytes)));

    

}
