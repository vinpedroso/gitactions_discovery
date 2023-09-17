use std::fs::File;
use std::io::Write;
use std::str::FromStr;

fn main() {
    let mut numbers = Vec::new();
    for arg in std::env::args().skip(1) { 
        numbers.push(u64::from_str(&arg) 
        .expect("error parsing argument"));
    }
    if numbers.len() == 0 {
        writeln!(std::io::stderr(), "Usage: NO NUMBER INSERTED...").unwrap(); 
        std::process::exit(1); 
        }
    let mut d = numbers[0]; 
    for m in &numbers[1..] 
        {d = gcd(d, *m);}
    
    println!("The greatest common divisor of {:?} is {}",numbers, d);
    let file_path = "./target/result.txt";
    let _ = write_answer_to_txt_file(file_path,&d);
} 

fn gcd(mut x: u64, mut y: u64) -> u64 {
    assert!(x != 0 &&  y != 0);
    while y != 0 { 
        if y < x {
            let inv = y; 
            y = x;
            x = inv;
        }
        y = y % x; 
    }
    x 
}

fn write_answer_to_txt_file(file_path: &str, inp: &u64) -> std::io::Result<()> {
    let mut output = File::create(file_path)?;
    write!(output,"{}", &inp)
}