use gtk::{glib, Application, ApplicationWindow, Button};
use gtk::prelude::*;

const APP_ID: &str = "org.gtk_rs.HelloWorld2";

fn main() -> glib::ExitCode {
    let app = Application::builder().application_id(APP_ID).build();
    app.connect_activate(build_ui);
    app.run()
}

fn build_ui(app: &Application) {
    let button_inc = Button::builder()
        .label("+")
        .margin_top(12)
        .margin_bottom(12)
        .margin_start(12)
        .margin_end(12)
        .build();
    let mut number = 0;
    button_inc.connect_clicked( |_| number += 1 );
    let window = ApplicationWindow::builder()
        .application(app)
        .title("My GTK App")
        .child(&button_inc)
        .build();
    window.present();
}
