#[derive(Debug, Default)]
struct Person {
    name: String,
    age: u8,
}

impl From<&str> for Person {
    fn from(s: &str) -> Self {
        if s.len() == 0 {
            return Person::default()
        }

        let parts = s.split(",").collect::<Vec<&str>>();

        if parts[0].len() == 0 {
            return Person::default()
        }

        match parts[1].parse::<u8>() {
            Ok(age) => Person { name: parts[0].to_string(), age },
            _ => Person::default(),
        }
            
    }
}

fn main() {
    let p1 = Person::from("Mark,20");
    println!("{:?}", p1);

    let p2: Person = "Gerald,70".into();
    println!("{:?}", p2);
}