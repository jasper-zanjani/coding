public class MyApp : Gtk.Application {
    public MyApp () {}

    public override void activate () {
        var builder = new Gtk.Builder ();
        builder.add_from_file ("main.ui");
        var win = builder.get_object("main_window") as Gtk.ApplicationWindow;
        win.set_application(this);
        win.present();
    }
}

int main (string[] args) {
    var app = new MyApp();
    app.run();
    return 0;
}
