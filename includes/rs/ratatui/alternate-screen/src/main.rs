use clap::{command, arg};

use std::{
    io::{stderr, Result},
    thread::sleep,
    time::Duration,
};

use ratatui::crossterm::{
    terminal::{EnterAlternateScreen, LeaveAlternateScreen},
    ExecutableCommand,
};
use ratatui::{prelude::*, widgets::*};

fn main() -> Result<()> {
    let args = command!()
        .arg(arg!(<VALUE>))
        .get_matches();

    if let Ok() = args.get_one::<bool>
    // let should_enter_alternate_screen = std::env::args().nth(1).unwrap().parse::<bool>().unwrap();
    if should_enter_alternate_screen {
        stderr().execute(EnterAlternateScreen)?; // remove this line
    }

    let mut terminal = Terminal::new(CrosstermBackend::new(stderr()))?;

    terminal.draw(|f| {
        f.render_widget(Paragraph::new("Hello World!"), Rect::new(10, 20, 20, 1));
    })?;
    sleep(Duration::from_secs(2));

    if should_enter_alternate_screen {
        stderr().execute(LeaveAlternateScreen)?; // remove this line
    }
    Ok(())
}
