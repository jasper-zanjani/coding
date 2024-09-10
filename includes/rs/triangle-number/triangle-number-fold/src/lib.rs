pub fn triangle(n: isize) -> isize {
    (1..=n).fold(0, |sum, item| sum + item)
}