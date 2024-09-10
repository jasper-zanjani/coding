#[derive(Debug)]
struct Counter {
    count: usize,
}

impl Counter {
    fn new() -> Counter {
        Counter { count: 0}
    }
}

impl Iterator for Counter {
    type Item = usize;

    fn next(&mut self) -> Option<usize> {
        self.count += 1;
        Some(self.count)
    }
}

fn main() {
    let mut ctr = Counter::new();
    println!("{:?}", ctr);

    ctr.next();
    println!("{:?}", ctr)

    ctr.next();
    println!("{:?}", ctr)
}
