use nix::unistd::{geteuid,getpid,getppid,gethostname};

fn main()  {

    let hostname = gethostname().unwrap();
    let pid = getpid();
    let ppid = getppid();
    let euid = geteuid();

    println!("Hostname: {:?}", hostname);
    println!("Effective user: {}", euid);
    println!("Process ID: {}" , pid);
    println!("Parent process ID: {}", ppid);
}
