use std::collections::HashMap;

fn fib(n: u64) -> u64 {
    match n {
        0 | 1 => 1,
        n => fib(n - 1) + fib(n - 2)
    }
}

fn main() {
    let n: u64 = std::env::args().nth(1).unwrap().parse().unwrap();
    for i in 1..n {
        println!("{}: {}", i, fib(i));
    }
}