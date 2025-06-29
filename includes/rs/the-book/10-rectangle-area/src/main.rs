struct Rectangle {
    width: usize,
    height: usize,
}

fn main() {
    let rect = Rectangle {
        width: 30,
        height: 50,
    };

    let area = area(&rect);
    println!("Area: {area}");
}

fn area(rectangle: &Rectangle) -> usize {
    rectangle.width * rectangle.height
}
