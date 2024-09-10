use std::collections::HashMap;

fn fib(n: u64, map: &mut HashMap<u64, u64>) -> u64 {
    match n {
        0 | 1 => 1,
        n => {
            if map.contains_key(&n) {
                *map.get(&n).unwrap()
            } else {
                let val = fib(n-1, map) + fib(n-2, map);
                map.insert(n, val);
                val
            }
        }
    }
}

fn main() {
    let n: u64 = std::env::args().nth(1).unwrap().parse().unwrap();
    let mut map = HashMap::new();
    for i in 1..n {
        println!("{}: {}", i, fib(i, &mut map));
    }
}