use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug)]
struct Point { x: isize, y: isize }

fn main() {
    let point = Point { x: 1, y: 2 };
    let serialized = serde_json::to_string(&point).unwrap();

    println!("serialized = {} ", serialized);

    let deserialized: Point = serde_json::from_str(&serialized).unwrap();
    println!("deseralized = {:?}", deserialized);
}
