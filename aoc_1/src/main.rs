fn main() {
    let lines: Vec<&str> = include_str!("../input.txt").split("\n\n").collect();
    let mut summations: Vec<i32> = vec![0; lines.len()];
    let mut index = 0;
    for e in lines.iter() {
        for l in e.lines() {
            let v: i32 = l.parse().unwrap();
            let item = &mut summations[index];
            *item += v;
        }
        index += 1;
    }
    summations.sort();
    summations.reverse();
    println!("Max: {}", summations.first().unwrap());
    println!("Max(3) Sum: {}", summations.iter().take(3).sum::<i32>());
}