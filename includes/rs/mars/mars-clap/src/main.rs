use clap::{command, arg};
use std::error::Error;

fn calculate_weight_on_mars(weight: f64) -> f64 {
    (weight / 9.81) * 3.711
}

fn main() {
    let args = command!().arg(arg!(<weight>).required(true)).get_matches();

    if let Some(weight) = args.get_one::<f64>("weight") {
        println!("Weight on Mars: {}", calculate_weight_on_mars(*weight));
    }
}
