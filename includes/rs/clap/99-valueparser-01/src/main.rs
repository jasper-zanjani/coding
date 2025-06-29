clap::{Arg, Command, value_parser};

fn main () {

    let mut cmd = Command::new("raw")
        .arg(
            Arg::new("output") .value_parser(value_parser!(usize)) .required(true)
        );

    let m = cmd.try_get_matches_from_mut(["cmd", "23"]).unwrap();
    assert_eq!(*m.get_one::<usize>("output").unwrap(), 23);
}
