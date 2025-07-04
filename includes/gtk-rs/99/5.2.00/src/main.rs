mod custom_button;

use custom_button::CustomButton;
use gtk::prelude::*;
use gtk::{
    glib,
    Application,
    ApplicationWindow,
};

fn main() -> glib::ExitCode {
    let app = Application::builder().build();
    app.connect_activate(build_ui);
    app.run()
}

fn build_ui(app: &Application) {
    let button = CustomButton::with_label("Press me!");
    button.set_margin_top(12);
    button.set_margin_bottom(12);
    button.set_margin_start(12);
    button.set_margin_end(12);

    button.connect_clicked(move |button| {
        button.set_label("Hello, World!");
    });

    let window = ApplicationWindow::builder()
        .application(app)
        .title("My GTK App")
        .child(&button)
        .build();
    window.present();
}
