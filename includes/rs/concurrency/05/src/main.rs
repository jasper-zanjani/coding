use std::sync::mpsc;
use std::thread::spawn;

fn main() {
    let (tx, rx) = mpsc::channel();

    spawn(move || {
        let val = String::from("Hello, World!");
        tx.send(val).unwrap();
    });

    let received = rx.recv().unwrap();
    println!("Got: {received}");
}
