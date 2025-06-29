use std::path::{Path,PathBuf};

fn main () {

    let mut cmd = clap::Command::new("raw")
        .arg(
            clap::Arg::new("output")
                .value_parser(clap::value_parser!(PathBuf))
                .required(true)
        );

    let m = cmd.try_get_matches_from_mut(["cmd", "file.txt"]).unwrap();
    let port: &PathBuf = m.get_one("output")
        .expect("required");
    assert_eq!(port, Path::new("file.txt"));
}
