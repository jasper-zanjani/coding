#[derive(Debug)]
struct Rectangle {
    width: usize,
    height: usize,
}

impl Rectangle {
    fn area(&self) -> usize {
        self.width * self.height
    }
}

fn main() {
    let rect = Rectangle {
        width: 30,
        height: 50,
    };

    let area = rect.area();
    println!("Area of {rect:?}: {area}");
}

