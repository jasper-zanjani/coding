fn main() {
    let results = vec![Ok(1), Err("bla"), Ok(2)];
    println!("results: {:?}", results); // (1)

    let values: Vec<_> = results.iter()
        .map(|r| r.unwrap_or(0))
        .collect();

    println!("values: {:?}", values); // (2)

}
