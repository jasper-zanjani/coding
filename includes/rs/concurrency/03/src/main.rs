use std::thread::spawn;

fn main() {
    let v = vec![1, 2, 3];

    let handle = spawn(|| {
        println!("Here's a vector: {v:?}");
    });

    handle.join().unwrap();
}
