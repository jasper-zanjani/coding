use gtk::prelude::*;
use gtk::{glib, Application, ApplicationWindow, Builder};

const APP_ID: &str = "org.gtk_rs.HelloWorld";

fn main() -> glib::ExitCode {
    let app = Application::builder()
        .application_id(APP_ID)
        .build();
    app.connect_activate(build_ui);
    app.run()
}

fn build_ui(app: &Application) {
    let builder = Builder::from_file("main.ui");
    let window: ApplicationWindow = builder
        .object("main_window")
        .unwrap();
    window.set_application(Some(app));
    window.present();
}
