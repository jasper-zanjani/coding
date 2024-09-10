pub mod encryptor {
    pub trait Encryptable {
        fn encrypt(&self) -> String;
    }

    pub struct Rot13(pub String);

    impl Encryptable for Rot13 {
        fn encrypt(&self) -> String {
            self.0
                .chars()
                .map(|ch| match ch {
                    'a'..='m' | 'A'..='M' => (ch as u8 + 13) as char,
                    'n'..='z' | 'N'..='Z' => (ch as u8 - 13) as char,
                    _ => ch,
                })
                .collect()
        }
    }
}

use encryptor::Encryptable;

fn main() {
    println!("Input the string you want to encrypt:");
    let mut user_input = String::new();

    std::io::stdin()
        .read_line(&mut user_input)
        .expect("Cannot read input!");
    println!(
        "Your encrypted string: {}",
        encryptor::Rot13(user_input).encrypt()
    );
}