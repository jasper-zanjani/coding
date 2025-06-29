use std::env::args;
use std::thread::{spawn,current};

fn main() {
    let args = args().collect();
    let threads: vec![];
    


    let t1 = spawn(f);
    let t2 = spawn(f);

    println!("Hello from the parent thread.");

    t1.join().unwrap();
    t2.join().unwrap();

}

fn f() {
    println!("Hello from spawned thread!");

    let id = current().id();
    println!("This is my thread id: {id:?}");
}
