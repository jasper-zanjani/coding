#[derive(Debug)]
struct BinaryData {
    data: Vec<u8>
}

impl From<String> for BinaryData {
    fn from(input: String) -> Self {
        let data: Vec<u8> = input.into_bytes();
        BinaryData { data }
    }
}

fn main() {
    let binarydata_from: BinaryData = BinaryData::from("Hello, World!".to_string());
    println!("{:?}", binarydata_from.data);

    let binarydata_into: BinaryData = "Hello, World!".to_string().into();
    println!("{:?}", binarydata_into.data);
}