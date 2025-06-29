The **rusqlite** crate works largely off the **Connection** object, which usually would open a database on disk with **open** but could also open an in-memory database with **open_in_memory** with no arguments.

Various methods on the connection object also enable the execution of SQL statements.

- [`execute`](https://docs.rs/rusqlite/latest/rusqlite/struct.Connection.html#method.execute) takes a `&str`.

- [`prepare`](https://docs.rs/rusqlite/latest/rusqlite/struct.Connection.html#method.prepare) which is used to prepare a statement for execution, to later capture its output or to reuse it with different values.

[`Statement`](https://docs.rs/rusqlite/latest/rusqlite/struct.Statement.html) struct is good for repeated executions with [**execute**](https://docs.rs/rusqlite/latest/rusqlite/struct.Statement.html#method.execute) or for capturing output (using [**query\_map**](https://docs.rs/rusqlite/latest/rusqlite/struct.Statement.html#method.query_map) for example

[**MappedRows**](https://docs.rs/rusqlite/latest/rusqlite/struct.MappedRows.html) is the iterator returned by Statement.query\_map

```rs
use rusqlite::{Connection, Result};

fn main() -> Result<()> {
    let path = "./path/to/db.db";
    let conn = Connection::open(path)?;

    conn.execute(/* ... */, [])?;

    Ok(());
}
```


```rs
--8<-- "includes/rs/rusqlite/chrono/src/main.rs"
```

```rs
--8<-- "includes/rs/rusqlite/enums/src/main.rs"
```
