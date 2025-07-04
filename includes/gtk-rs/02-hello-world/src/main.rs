use gtk::prelude::*;
use gtk::{glib, Application, ApplicationWindow, Button, Builder};

const APP_ID: &str = "org.gtk_rs.HelloWorld1";

fn main() -> glib::ExitCode {
    let app = Application::builder().application_id(APP_ID).build();
    app.connect_activate(build_ui);
    app.run()
}

fn build_ui(app: &Application){
    let builder = Builder::from_file("main.ui");
    let button: Button = builder.object("button").unwrap();

    button.connect_clicked( move |button| {
        button.set_label("Hello, World!");
    });

    let window: ApplicationWindow = builder.object("main_window").unwrap();
    window.set_application(Some(app));
    window.present();
}
