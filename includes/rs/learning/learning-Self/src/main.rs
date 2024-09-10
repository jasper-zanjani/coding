struct DataStruct1 {
    pub data: String
}

trait SelfTestable {
    fn get_data(&self, other: &Self) -> ();
    fn change_data(&self, other: &mut Self) -> ();
}

impl SelfTestable for DataStruct1 {
    fn get_data(&self, other: &Self) -> () {
        println!("{}", other.data)
    }

    fn change_data(&self, other: &mut Self) -> () {
        other.data = other.data.clone() + " Data has been changed!";
    }
}

fn main() {

    let mut callee = DataStruct1 { 
        data: String::from("Hello, caller! I am the callee.") 
    };
    let caller = DataStruct1 { 
        data: String::from("Hello, callee! I am the caller.")
    };

    caller.get_data(&callee);
    callee.get_data(&caller);
    

    caller.change_data(&mut callee);
    caller.get_data(&callee);
}
