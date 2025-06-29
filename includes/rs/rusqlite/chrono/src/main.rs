use rusqlite::{Connection, Result};
use chrono::naive::NaiveDate;


fn main() -> Result<()> {
    let conn = Connection::open("database.db")?;
    let mut stmt = conn.prepare("SELECT * FROM dates")?;
    let date_iter = stmt.query_map([], |record| {
        Ok(
            NaiveDate::from_ymd_opt(
               record.get(0).unwrap(), 
               record.get(1).unwrap(),
               record.get(2).unwrap(),
           ).unwrap()
        )
    })?;

    for date in date_iter { println!("{:?}", date.unwrap()); }
    Ok(())
}
