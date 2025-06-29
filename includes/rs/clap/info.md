Using clap comes down to managing two main structs.

-   [`Command`][Command] defines the overall structure of subcommands, options, and arguments that comprise command-line usage. 
    Command structs are assembled through a sequence of method calls using the Builder pattern.
-   The [`get_matches`](https://docs.rs/clap/latest/clap/struct.Command.html#method.get_matches) method on Command returns  an [`ArgMatches`][ArgMatches] struct.
    CLI arguments are accessed via methods on this struct.

However, the simplest way to get started is to use the various macros available.

- [`command`][command] allows a command to be defined more succinctly by drawing metadata from the crate's manifest, equivalent to using the various [`crate_` macros](https://docs.rs/clap/latest/clap/index.html#macros).

- [`arg`](https://docs.rs/clap/latest/clap/macro.arg.html) similarly allows the argument to be defined succinctly, but there is no support for default values (yet).

#### Hello, World!

The following example demonstrates use of the command and arg macros to define a very simple Hello, World! with a single argument.
Note the [turbofish](https://doc.rust-lang.org/reference/glossary.html?highlight=turbo#turbofish) syntax on `get_one` defining the return type.

```rs title="clap/00" hl_lines="5"
--8<-- "includes/rs/clap/00/src/main.rs"
```

A more elaborated example illustrates the same macros to define an option. (1)
{: .annotate }

1.  The equivalent application defined by avoiding the macros and manually defining the structs:

    ```rs title="03"
    --8<-- "includes/rs/clap/03/src/main.rs"
    ```

    --8<-- "includes/rs/clap/Arg.md"

```rs title="clap/01" hl_lines="5 6"
--8<-- "includes/rs/clap/01/src/main.rs"
```

#### Oxford Comma

Passing `ArgAction::Append` to the argument's action method will allow multiple arguments to be passed (requiring multiple uses of the option and use of the `get_many` method).

```rs hl_lines="9" title="clap/02"
--8<-- "includes/rs/clap/02/src/main.rs"
```

Using `value_delimiter` is an alternative way of implementing multiple values for a single argument.

```rs hl_lines="5" title="clap/06"
--8<-- "includes/rs/clap/06/src/main.rs"
```

#### Data validation

The [`value_parser`][value_parser] macro is provided for data validation on arguments.
Without it, the argument must retrieved as a string and parsed.


```rs hl_lines="9 10" title="cat/02"
--8<-- "includes/rs/50-cat/02/src/main.rs"
```

#### Getters

Arguments provided to a clap application from the command-line are queried using a family of getters on ArgMatches (the most common of which is [`get_one`](https://docs.rs/clap/latest/clap/struct.ArgMatches.html#method.get_one)).

-   [`get_flag`](https://docs.rs/clap/latest/clap/struct.ArgMatches.html#method.get_flag) is used to retrieve the value of an option that is set to true or false using [`ArgAction`][ArgAction]. (1)
    {: .annotate }

    1.  

        ```rs title="04"
        --8<-- "includes/rs/clap/04/src/main.rs"
        ```

-   [`get_count`](https://docs.rs/clap/latest/clap/struct.ArgMatches.html#method.get_count) is used to retrieve the number of types an option was passed (1)
    {: .annotate }

    1.  Note that `...` is syntactic sugar for this action when using the arg macro.

        ```rs title="05" hl_lines="6"
        --8<-- "includes/rs/clap/05/src/main.rs"
        ```

#### Subcommands
    
The following implementation will accept only the specified subcommands and suggest one if it is mispelled by the user.

```rs
let git_clone = Command::new("clone");
let git_push = Command::new("push");
let git_commit = Command::new("commit");

let git = Command::new("git")
    .subcommand(git_clone)
    .subcommand(git_commit)
    .subcommand(git_push)
    .get_matches();
```

Subcommands are accessed (mostly) by [subcommand\_matches](https://docs.rs/clap/latest/clap/struct.ArgMatches.html#method.subcommand_matches) which should be used in a series of **if let** statements. (1)
{ .annotate }

1. An additional method [subcommand\_name](https://docs.rs/clap/latest/clap/struct.ArgMatches.html#method.subcommand_name) returns only an `Option<&str>` and appears to be less useful.
```rs
match git.subcommand_name() {
    Some("clone")  => {},
    Some("push")   => {},
    Some("commit") => {},
    _              => {},
}
```

```rs
if let Some(clone_matches) = git.subcommand_matches("clone") {
    println!(
        "clone argument: {}",
        clone_matches.get_one::<String>("clone_arg").unwrap());
}

if let Some(commit_matches) = git.subcommand_matches("commit") {
    println!(
        "commit argument: {}", 
        commit_matches.get_one::<String>("commit_arg").unwrap());
}

if let Some(push_matches) = git.subcommand_matches("push") {
    println!(
        "push argument: {}", 
        push_matches.get_one::<String>("push_arg").unwrap());
}
```

#### Data validation


## Derive

Requires the **derive** feature flag

```sh
cargo add clap --features derive
```

Using the [**Parser**](https://docs.rs/clap/latest/clap/trait.Parser.html#) derive allows command-line arguments and options to be defined on a struct with an attribute.
Any **Command**, **Arg**, or **PossibleValue** method can be used as an attribute.

<div class="grid cards" markdown>


-   #### Option

    ```rs
    use clap::Parser;

    #[derive(Parser)]
    #[clap(name = "Hello, World!")]
    struct Args {
        #[clap(short, long, default_value_t = String::from("Hello"))]
        greeting: String,

        #[clap(default_value_t = String::from("World"))]
        name: String,
    }

    fn main() {
        let args = Args::parse();
        println!("{}, {}!", args.greeting, args.name);
    }
    ```



-   #### Command

    ```rs
    use clap::{Parser, Subcommand};

    #[derive(Parser)]
    #[clap(name = "Hello, World!")]
    struct Args {
        #[clap(subcommand)]
        greeting: Greeting,

        #[clap(default_value_t = String::from("World"))]
        name: String
    }

    #[derive(Subcommand)]
    enum Greeting {
        Hello,
        Greetings
    }

    fn main() {
        let args = Args::parse();
        println!("{}, {}!", args.greeting, args.name); // (1)
    }
    ```

    1. This requires the **Display** trait to be implemented
    ```rs
    impl std::fmt::Display for Greeting {
        fn fmt(&self, _: &mut std::fmt::Formatter) -> std::fmt::Result {
            match self {
                Greeting::Hello => { print!("Hello"); Ok(()) },
                _               => { print!("Greetings"); Ok(()) }
            }
        }
    }
    ```

</div>

[**ArgEnum**](https://docs.rs/clap/latest/clap/trait.ArgEnum.html) and [**Subcommand**](https://docs.rs/clap/latest/clap/trait.Subcommand.html) can be used in very similar ways.
ArgEnum variants do show up in the help output but inline with the Subcommand.

<div class="grid cards" markdown>

-   #### ArgEnum

    ---

    ```rs hl_lines="5 10"
    use clap::{ArgEnum, Parser};

    #[derive(Parser)]
    struct Cli {
        #[clap(arg_enum)]
        command: Actions,
    }

    #[derive(Copy, Clone, ArgEnum)]
    enum Actions {
        Eat,
        Drink,
    }

    fn main() {
        let cli = Cli::parse();

        match cli.command {
            Actions::Eat    => println!("Eating"),
            Actions::Drink  => println!("Drinking"),
        }
    }
    ```

-   #### Subcommand

    ---

    ```rs hl_lines="5 10"
    use clap::{Subcommand, Parser};

    #[derive(Parser)]
    struct Cli {
        #[clap(subcommand)]
        command: Actions,
    }

    #[derive(Subcommand)]
    enum Actions {
        Eat,
        Drink,
    }

    fn main() {
        let cli = Cli::parse();

        match cli.command {
            Actions::Eat    => println!("Eating"),
            Actions::Drink  => println!("Drinking"),
        }
    }
    ```

</div>

Apparently they may not be used together, enums with a Subcommand derive attribute require variants that contain Args derived values:

<div class="grid cards" markdown>



```rs
use clap::{Args, Parser, Subcommand};

#[derive(Parser)]
struct Cli {
    #[clap(subcommand)]
    command: Actions,
}

#[derive(Subcommand)]
enum Actions {
    #[clap(arg_enum)]
    Eat(Foods),
    #[clap(arg_enum)]
    Drink(Drinks),
}

#[derive(Args)]
struct Foods {
    name: String,
}

#[derive(Args)]
struct Drinks {
    name: String
}

fn main() {
    let cli = Cli::parse();

    match cli.command {
        Actions::Eat(f) => {
            println!("Eating {}", f.name);
        }
        Actions::Drink(d) => {
            println!("Drinking {}", d.name);
        }
    }
}
```

```rs
use std::string::ParseError;

use clap::{ArgEnum, Args, Parser, Subcommand, };

#[derive(Parser)]
struct Cli {
    #[clap(subcommand)]
    command: Actions,
}

#[derive(Subcommand)]
enum Actions {
    #[clap(arg_enum)]
    Eat(Food),
    #[clap(arg_enum)]
    Drink(Drink),
}

#[derive(Args)]
struct Food {
    name: String,
}

#[derive(Args)]
struct Drink {
    drink: Drinks
}

#[derive(ArgEnum, Clone)]
enum Drinks {
    Coke,
    Pepsi,
    Other
}

impl std::str::FromStr for Drinks {
    type Err = ParseError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "coke" => Ok(Self::Coke),
            "pepsi" => Ok(Self::Pepsi),
            _ => Ok(Self::Other),
        }
    }
}

impl From<Drinks> for String {
    fn from(item: Drinks) -> String {
        match item {
            Drinks::Coke => String::from("Coke"),
            Drinks::Pepsi => String::from("Pepsi"),
            _ => String::from("Other")
        }
    }
}

fn main() {
    let cli = Cli::parse();

    match cli.command {
        Actions::Eat(f) => {
            println!("Eating {}", f.name);
        }
        Actions::Drink(d) => {
            println!("Drinking {}", String::from(d.drink));
        }
    }
}
```

</div>

#### Starships using Derive




```rs
#[macro_use] extern crate diesel;
use diesel::prelude::*;
use diesel::result::QueryResult;
use diesel::sqlite::SqliteConnection;

mod models;                         // (1)
use models::Starship;
mod schema;                         // (2)
use schema::starships::dsl::*;

use clap::{Parser, Subcommand};

#[derive(Parser)]
struct Cli {
    #[clap(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    Add(Starship),
    Update,
    Remove,
    List,
}

fn main() {
    let app = Cli::parse();
    match app.command {
        Commands::Add(s)    => add_ship(&s),
        Commands::List      => list_ships(),
        Commands::Remove    => println!("Removing"),
        Commands::Update    => println!("Updating"),
    }
}

fn add_ship(s: &Starship) {
    let conn = get_connection().unwrap();
    println!("Adding {:?}", s);
    s.insert_into(starships)
        .execute(&conn)
        .unwrap();
}

fn list_ships() {
    println!("{:?}", get_ships().unwrap());
}

fn get_connection() -> ConnectionResult<SqliteConnection> {
    dotenv::dotenv().expect("Couldn't load .env file");
    let url = &std::env::var("DATABASE_URL").unwrap();
    SqliteConnection::establish(url)
}

fn get_ships() -> QueryResult<Vec<Starship>> {
    let conn = get_connection().unwrap();
    starships
        .load::<Starship>(&conn)
}
```

1. Note that the order of the fields matters (for both postgres as well as sqlite connections), and the primary key should be the first field defined.
```rs
use crate::schema::starships;
use clap::Args;

#[derive(Args,Debug, Queryable, Insertable, Identifiable, Clone)]
#[primary_key(registry)]
pub struct Starship {
    #[clap(long, short)]
    pub registry: String,
    #[clap(long, short)]
    pub name: String,
    #[clap(long, short)]
    pub crew: i32,
}
```
2. 
```rs
table! {
    starships (registry) {
        registry -> Text,
        name -> Text,
        crew -> Integer,
    }
}
```

## Parser

An [additional workflow](https://docs.rs/clap/latest/clap/_derive/index.html) is available which disposes with the Builder pattern entirely and uses a central struct decorated with attributes.
This example is probably outdated and needs to be replaced entirely.

```rs
use clap::Parser;

#[derive(Parser)]
#[clap(name = "Hello, World!", version, author)] // (2)
struct Cli {
    #[clap(short, long, default_value_t = String::from("Hello"))]
    greeting: String,

    #[clap(default_value_t = String::from("World"))]
    name: String,
}

fn main() {
    let cli = Cli::parse();
    println!("{}, {}!", cli.greeting, cli.name);
}
```

Without providing arguments to version or author, the relevant values will be pulled from the crate itself, similar to the [`crate_authors`](https://docs.rs/clap/latest/clap/macro.crate_version.html) and [`crate_version`](https://docs.rs/clap/latest/clap/macro.crate_version.html) macros for the procedural API.
