use gtk::{
    prelude::*,
    glib, 
    Application, 
    ApplicationWindow, 
    Builder,
    Scale,
};

fn main() -> glib::ExitCode {
    let app = Application::builder().build();
    app.connect_activate(activate);
    app.run()
}

fn activate(app: &Application) {
    let builder = Builder::from_file("main.ui");
    let window: ApplicationWindow = builder.object("main_window").unwrap();
    window.set_application(Some(app));
    window.present();

    let scale: Scale = builder.object("scale").unwrap();
    scale.connect_value_changed(scale_value_changed);
}

fn scale_value_changed(scale: &Scale) {
    println!("{}", scale.value());
}
