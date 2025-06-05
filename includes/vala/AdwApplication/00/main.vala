public class App : Adw.Application {
  public override void activate () {
    var win = new Gtk.ApplicationWindow (this);
    win.present();
  }
}

int main() {
  var app = new App ();
  return app.run();
}
