use std::collections::HashMap;

fn main() {
    let input = include_str!("../input.txt");
    let lines: Vec<&str> = input.split("\n").collect::<Vec<&str>>();
    println!("Line Count: {:?}", lines.len());

    run(lines)
}

fn run(lines: Vec<&str>) {
    let value_sheet = HashMap::from([
        (("A", "X"), ((4), (3))),
        (("A", "Y"), ((8), (4))),
        (("A", "Z"), ((3), (8))),
        (("B", "X"), ((1), (1))),
        (("B", "Y"), ((5), (5))),
        (("B", "Z"), ((9), (9))),
        (("C", "X"), ((7), (2))),
        (("C", "Y"), ((2), (6))),
        (("C", "Z"), ((6), (7))),
    ]);

    let mut p1_sum = 0;
    let mut p2_sum = 0;
    for line in lines.iter() {
        if *line == "" { continue; }
        let par_tup = value_sheet.get(&line.split_once(" ").unwrap()).unwrap();
        p1_sum += par_tup.0;
        p2_sum += par_tup.1;
    }

    println!("P1 SUM: {}", p1_sum);
    println!("P2 SUM: {}", p2_sum);
}