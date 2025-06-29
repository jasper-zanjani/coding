use serde::{Serialize, Deserialize};
use std::path::Path;
use std::fs::{File, read_to_string};
use std::io::{BufRead, BufReader};

#[derive(Serialize, Deserialize, Debug)]
struct Starship {
    name: String,
    class: String,
    registry: String,
    series: String,

}

fn main() {
    let ent = Starship { name: "USS Enterprise".to_string(), class: "Constitution".to_string(), registry: "NCC-1701".to_string(), series: "TOS".to_string() };

    println!("Enterprise: {}", serde_json::to_string(&ent).unwrap());

    let json_path = Path::new("/home/jasper/Documents/git/dogfood/json/starships.json");
    let json_file = File::open(&json_path).unwrap();
    let reader = BufReader::new(&json_file);
    //let text = read_to_string(&json_path).unwrap();
    let text: Vec<_> = reader.lines().collect();
    println!("text: {}", text.join(""));

    //let starships : Vec<Starship> = serde_json::from_reader(reader).expect("Error opening file");
    //println!("starships: {}", serde_json::to_string(&starships).unwrap());
}
