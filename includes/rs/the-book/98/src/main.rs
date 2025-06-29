use std::{
    io::{BufReader, prelude::*},
    net::{TcpListener, TcpStream},
    thread::{JoinHandle, spawn, sleep},
};

pub struct ThreadPool {
    workers: Vec<Worker>,
}

impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id));
        }

        ThreadPool {workers}
    }

    pub fn execute<F>(&self, f: F) where F: FnOnce() + Send + 'static, { }
}

struct Worker {
    id: usize,
    thread: JoinHandle<()>,
}

impl Worker {
    fn new(id: usize) -> Worker {
        let thread = spawn(|| {} );
        Worker {id, thread }
    }
}

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap(); // Maybe incorporate CLI option?
    
    for stream in listener.incoming() {
        let stream = stream.unwrap();
        let pool = ThreadPool::new(4);

        pool.execute(|| {
            handle_connection(stream);
        });
    }
}

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&stream);
    let request_line = buf_reader.lines().next().unwrap().unwrap();

    let (status_line, filename) = match &request_line[..] {
        "GET / HTTP/1.1" =>  ("HTTP/1.1 200 OK", "hello.html"),
        "GET /sleep HTTP/1.1" => {
            sleep(std::time::Duration::from_secs(5));
            ("HTTP/1.1 200 OK", "hello.html")
        }
        _ => ("HTTP/1.1 404 NOT FOUND", "404.html"),
    };

    let contents = std::fs::read_to_string(filename).unwrap();
    let length = contents.len();
    let response = 
        format!("{status_line}\r\nContent-Length: {length}\r\n\r\n{contents}");

    stream.write_all(response.as_bytes()).unwrap();
}
