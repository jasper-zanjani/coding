use std::sync::mpsc;
use std::thread::{spawn,sleep};
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel();
    let tx1 = tx.clone();
    spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("spawned"),
            String::from("thread"),
        ];
        for val in vals{
            tx1.send(val).unwrap();
            sleep(Duration::from_millis(200));
        }
    });

    spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("spawned"),
            String::from("thread"),
        ];
        for val in vals{
            tx.send(val).unwrap();
            sleep(Duration::from_millis(200));
        }
    });

    for received in rx {
        println!("Got: {received}");
    }
}
