use rusqlite::{Connection, Result};

#[derive(Debug)]
enum Color { Red, Yellow, Blue, Green, White, Black }


fn main() -> Result<()> {
    let conn = Connection::open("database.db")?;

    let mut stmt = conn.prepare("SELECT name FROM enums")?;
    let rows = stmt.query_map([], |row| row.get(0))?;

    let mut names : Vec<String> = Vec::new();
    for name_result in rows {
        names.push(name_result?);
    }

    let mut colors : Vec<Color> = Vec::new();

    for name in rows {
        match &name as &str {
            "red" => colors.push(Color::Red),
            "yellow" => colors.push(Color::Yellow),
            "blue" => colors.push(Color::Blue),
            _ => (),
        }
    }

    for color in colors {
        println!("{:?}", color);
    }

    //let mut stmt = conn.prepare("SELECT * FROM enums")?;

    //let records = stmt.query_map([], |record| record.get(0))?;

    //for record in records {
        //println!("{:?}", record?);
    //}

    Ok(())
}


