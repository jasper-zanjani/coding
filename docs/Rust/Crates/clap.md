Any clap application is defined by two main structs.

[**Command**][clap::Command] defines the overall structure of subcommands, options, and arguments that comprise command-line usage. Command structs are assembled through a sequence of method calls using the Builder pattern. (1)
{ .annotate }

1. 
An [additional workflow](https://docs.rs/clap/latest/clap/_derive/index.html) is available which disposes with the Builder pattern entirely and uses a central struct decorated with attributes.
This example is probably outdated and needs to be replaced entirely.
```rs
use clap::Parser; // (1)

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
    1. **Parser** requires the **derive** and **std** features:
    ```toml title="Cargo.toml"
    clap = { version = "3.0.12", features = ["std", "derive"], default-features = false}
    ```
    2. Without providing arguments to version or author, the relevant values will be pulled from the crate itself, similar to the [crate\_authors](https://docs.rs/clap/latest/clap/macro.crate_version.html) and [crate\_version](https://docs.rs/clap/latest/clap/macro.crate_version.html) macros for the procedural API.


[**ArgMatches**][clap::ArgMatches] is formed using the [get\_matches method](https://docs.rs/clap/latest/clap/struct.Command.html#method.get_matches) which is usually the last method on the Command struct. This struct returns command-line arguments when various [getter methods](#getters) are called.



<div class="grid cards" markdown>

-   #### [Command][clap::Command]

    ---

    Using the Builder pattern, a series of **arg** and **subcommand** methods elaborate the central Command struct.

    Some macros exist to facilitate ease of use.

    === "Using structs"

        ```rs
        use clap::{Command, Arg, crate_version, crate_authors};

        fn main() {
            let args = Command::new("Say hello")
                .version(crate_version!())
                .author(crate_authors!())
                .arg(
                    Arg::new("name") // (2)
                        .default_value("World")
                )
                .arg(
                    Arg::new("greeting")
                        .default_value("Hello")
                        .short('g')
                        .long("greeting")
                )
                .get_matches();

            println!("{}, {}!", args.value_of("greeting").unwrap(), args.value_of("name").unwrap());
        }
        ```

    === "Using macros"

        ```rs
        use clap::command, arg;

        fn main() {
            let args = commands!()
                .arg(arg!(<name>))
                .arg(arg!(-g --greeting <greeting>))
                .get_matches();
            
            println!("{} {}", args.)
        }
        ```

        - [**command!**](https://docs.rs/clap/latest/clap/macro.command.html) allows a command to be defined more succinctly by drawing metadata from the crate's manifest, equivalent to using the various [**crate\_..** macros](https://docs.rs/clap/latest/clap/index.html#macros).

        - [**arg!**](https://docs.rs/clap/latest/clap/macro.arg.html) similarly allows the argument to be defined succinctly, but there is no support for default values (yet).



-   #### [Arg][clap::Arg]

    ---

    Notice that the **Arg** structs also exhibit the Builder pattern and are also defined using a sequence of method calls.

    - [**short**](https://docs.rs/clap/latest/clap/struct.Arg.html#method.short) sets POSIX-style short option using a char (additional hidden flags can be defined with [**short\_alias**](https://docs.rs/clap/latest/clap/struct.Arg.html#method.short_alias))
    - [**long**](https://docs.rs/clap/latest/clap/struct.Arg.html#method.long) defines the long version of the option, omitting the two hyphens
    - [**default_value**](https://docs.rs/clap/latest/clap/struct.Arg.html#method.default_value)
    - [**subcommand**](https://docs.rs/clap/latest/clap/struct.Command.html#method.subcommand) accepts additional Command structs, allowing a tree-like hierarchy of subcommands (in the style of utilities like git, ip, etc) to be formed.
    - [**action**](https://docs.rs/clap/latest/clap/struct.Arg.html#method.action) can define various interesting and useful behavior for the option and accepts an [ArgAction](https://docs.rs/clap/latest/clap/enum.ArgAction.html) value: 

        - ArgAction::[SetTrue](https://docs.rs/clap/latest/clap/enum.ArgAction.html#variant.SetTrue) 
        provides functionality similar to that of the typical flag.

        - ArgAction::[Count](https://docs.rs/clap/latest/clap/enum.ArgAction.html#variant.Count) 
        returns a u8 of the number of times the option was provided


-   #### Getters

    ---

    Arguments provided to a clap application from the command-line are queried using a family of getters on ArgMatches (the most common of which is [**get\_one**](https://docs.rs/clap/latest/clap/struct.ArgMatches.html#method.get_one)).

    === "get\_one"

        ```rs
        --8<-- "includes/rs/hello-world/hello-world-clap/src/main.rs"
        ```

    === "get\_flag"

        ```rs
        --8<-- "includes/rs/clap/bool/src/main.rs"
        ```

    === "get\_count"

        ```rs
        --8<-- "includes/rs/clap/count/src/main.rs"
        ```

    Handling multiple arguments is somewhat more complicated, and there are several approaches.

    - passing **ArgAction::Append** to the argument's action method will allow multiple arguments to be passed. If a short or long option is defined then multiple uses of the command-line option will be necessary.
    - defining a delimiter

    Notice the use of the [turbofish](https://doc.rust-lang.org/reference/glossary.html?highlight=turbofish#turbofish) syntax `::<>` (most familiar from its use in [str][std::str]::[parse](https://doc.rust-lang.org/std/primitive.str.html#method.parse)) to assist the inference algorithm what type is to be retrieved.

    === "Append"

        ```rs hl_lines="7"
        --8<-- "includes/rs/hello-world/hello-world-append/src/main.rs"
        ```

    === "Delimited"

        ```rs hl_lines="7"
        --8<-- "includes/rs/hello-world/hello-world-delimiter/src/main.rs"
        ```


-   #### Subcommands

    ---
    
    
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

</div>

#### Data validation

The [**value\_parser** macro](https://docs.rs/clap/latest/clap/macro.value_parser.html) is provided for data validation on arguments.
Without value\_parser, the argument must retrieved as a string and parsed.

<div class="grid cards" markdown>

```rs hl_lines="9 10" title="Without value_parser"
--8<-- "includes/rs/learning-conversions/conversions-clap-parse/src/main.rs"
```


```rs hl_lines="7" title="With value_parser"
--8<-- "includes/rs/learning-conversions/conversions-clap-value_parser/src/main.rs"
```

</div>

#### Clap tutorials

=== "1"

    ```rs
    --8<-- "includes/rs/clap-tutorials/clap-tutorial-0/src/main.rs"
    ```

=== "2"

    ```rs
    --8<-- "includes/rs/clap-tutorials/clap-tutorial-1/src/main.rs"
    ```

=== "3"

    ```rs
    --8<-- "includes/rs/clap-tutorials/clap-tutorial-2/src/main.rs"
    ```

=== "4"

    ```rs
    --8<-- "includes/rs/clap-tutorials/clap-tutorial-3/src/main.rs"
    ```

=== "5"

    ```rs
    --8<-- "includes/rs/clap-tutorials/clap-tutorial-4/src/main.rs"
    ```


??? info "Derive"

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


--8<-- "includes/rs/links.md"