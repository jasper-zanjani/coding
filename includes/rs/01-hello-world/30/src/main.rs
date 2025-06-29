use std::thread::{spawn, current};

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let mut threads = vec![];
    let thread_count: usize = args[1].parse().unwrap();
    for _ in 0..thread_count { threads.push(spawn(say_hello)); }
    for t in threads {
        t.join().unwrap();
    }
    say_hello();
}

fn say_hello() {
    let id = current().id();
    println!("Hello from thread {id:?}!");
}
