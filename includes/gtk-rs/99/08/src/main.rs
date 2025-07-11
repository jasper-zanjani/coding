use std::cell::Cell;
use std::rc::Rc;
use gtk::{glib, Application, ApplicationWindow, Button, Box};
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
    let button_dec = Button::builder()
        .label("-")
        .margin_top(12)
        .margin_bottom(12)
        .margin_start(12)
        .margin_end(12)
        .build();

    let number = Rc::new(Cell::new(0));
    button_inc.connect_clicked( 
        glib::clone!(
            #[weak]
            number, 
            #[weak] 
            button_dec,
            move |_| { 
                number.set(number.get() + 1); 
                button_dec.set_label(&number.get().to_string());
            }
        )
    );
    button_dec.connect_clicked( 
        glib::clone!(
            #[weak]
            button_inc,
            move |_| { 
                number.set(number.get() - 1);
                button_inc.set_label(&number.get().to_string());
            }
        )
    );

    let gtkbox = Box::builder().build();
    gtkbox.append(&button_inc);
    gtkbox.append(&button_dec);

    let window = ApplicationWindow::builder()
        .application(app)
        .title("My GTK App")
        .child(&gtkbox)
        .build();
    window.present();
}
