use std::fs::File;
use std::io::prelude::*;
use std::str::FromStr;


fn read_input() -> (i32, i32, i32) {
    let mut file = File::open("input").expect("Unable to open the file");
    let mut contents = String::new();
    file.read_to_string(&mut contents).expect("Unable to read the file");
    let tokens: Vec<&str> = contents.split("\n").collect();
    
    let hp_tokens: Vec<&str> = tokens[0].split(" ").collect();
    let hp_str: &str = &hp_tokens[2].to_string()[..hp_tokens[2].chars().count() - 1];
    let hp = i32::from_str(hp_str).unwrap();
    
    let dmg_tokens: Vec<&str> = tokens[1].split(" ").collect();
    let dmg_str: &str = &dmg_tokens[1].to_string()[..dmg_tokens[1].chars().count() - 1];
    let dmg = i32::from_str(dmg_str).unwrap();
    
    let armor_tokens: Vec<&str> = tokens[2].split(" ").collect();
    let armor_str: &str = &armor_tokens[1].to_string()[..armor_tokens[1].chars().count()];
    let armor = i32::from_str(armor_str).unwrap();
    
    (hp, dmg, armor)
}

fn damage(atk: i32, def: i32) -> i32 {
    if def >= atk {
        return 1;
    }
    atk - def
}

fn player_wins(enemy: (i32, i32, i32), player: (i32, i32, i32)) -> bool {
    let mut enemy_hp = enemy.0;
    let enemy_dmg = enemy.1;
    let enemy_def = enemy.2;
    
    let mut player_hp = player.0;
    let player_dmg = player.1;
    let player_def = player.2;
    
    loop {
        enemy_hp = enemy_hp - damage(player_dmg, enemy_def);
        if enemy_hp <= 0 {
            return true
        }
        
        player_hp = player_hp - damage(enemy_dmg, player_def);
        if player_hp <= 0 {
            return false
        }
    }
}

fn main() {
    let enemy = read_input();
    
    let weapons: [(i32, i32, i32); 5] = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)];
    let armor: [(i32, i32, i32); 6] = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5), (0, 0, 0)];
    let rings: [(i32, i32, i32); 8] = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3), (0, 0, 0), (0, 0, 0)];
    let hp = 100;
    
    let mut max_cost = -1;
    for w in weapons.iter() {
        for a in armor.iter() {
            for (i, r1) in rings.iter().enumerate() {
                for (j, r2) in rings.iter().enumerate() {
                    if i != j {
                        let cost = w.0 + a.0 + r1.0 + r2.0;
                        let dmg = w.1 + a.1 + r1.1 + r2.1;
                        let def = w.2 + a.2 + r1.2 + r2.2;
                        if !player_wins(enemy, (hp, dmg, def)) {
                            if cost > max_cost {
                                max_cost = cost;
                            }
                        }
                    }
                }
            }
        }
    }
    println!("{}", max_cost);
}
