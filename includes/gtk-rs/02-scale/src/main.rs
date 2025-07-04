use gtk::{
    prelude::*,
    glib, 
    Application, 
    ApplicationWindow, 
    Builder,
    Label,
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

    let label: Label = builder.object("label").unwrap();
    let scale: Scale = builder.object("scale").unwrap();
    scale.connect_value_changed(
        glib::clone!(
            #[weak] scale, 
            move |_| {
                label.set_label(&scale.value().to_string());
            }
        )
    );
}
