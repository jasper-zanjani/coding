use gtk::prelude::*;
use gtk::{glib, Application, ApplicationWindow, Button, Builder, Label};
use std::cell::{Cell, RefCell};
use std::rc::Rc;

fn main() -> glib::ExitCode {
    let app = Application::builder()
        .build();
    app.connect_activate(build_ui);
    app.run()
}

fn build_ui (app: &Application) {
    let builder = Builder::from_file("main.ui");
    let window: ApplicationWindow = builder .object("main_window") .unwrap();
    let button_inc: Button = builder.object("button_inc").unwrap();
    let button_dec: Button = builder.object("button_dec").unwrap();
    let label: Label = builder.object("label").unwrap();

    let number = Rc::new(Cell::new(0));

    button_inc.clone().connect_clicked(
        move |_| {
            number.set(number.get() + 1);
            label.set_label(&number.get().to_string());
        }
    );
    button_dec.clone().connect_clicked(
        move |_| {
            number.set(number.get() - 1);
            label.set_label(&number.get().to_string());
        }
    );

    window.set_application(Some(app));
    window.present();
}
