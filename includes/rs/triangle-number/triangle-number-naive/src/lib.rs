pub fn triangle(n: isize) -> isize {
    let mut sum = 0;
    for i in 1..=n { sum += i; }
    sum
}