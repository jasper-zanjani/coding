use std::cell::{Cell, RefCell};
use std::rc::Rc;
use gtk::{glib, Application, ApplicationWindow, Button, Box, Label};
use gtk::prelude::*;

const APP_ID: &str = "org.gtk_rs.clicker";

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
    let button_dec = Button::builder()
        .label("-")
        .margin_top(12)
        .margin_bottom(12)
        .margin_start(12)
        .margin_end(12)
        .build();
    let label = Label::builder().label("0").build();

    let number = Rc::new(Cell::new(0));

    button_inc.connect_clicked( 
        glib::clone!(
            #[weak] 
            number, 
            #[weak]
            label,
            move |_| { 
                number.set(number.get() + 1); 
                label.set_label(&number.get().to_string());
            }
        )
    );
    button_dec.connect_clicked( 
        glib::clone!(
            #[weak]
            label,
            move |_| { 
                number.set(number.get() - 1);
                label.set_label(&number.get().to_string());
            }
        )
    );

    let gtkbox = Box::builder().build();
    gtkbox.append(&button_dec);
    gtkbox.append(&label);
    gtkbox.append(&button_inc);

    let window = ApplicationWindow::builder()
        .application(app)
        .title("My GTK App")
        .child(&gtkbox)
        .build();
    window.present();
}
