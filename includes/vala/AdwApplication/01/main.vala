public class App : Adw.Application {
  construct {
    stdout.printf("Hello, World!\n");
  }

  public override void activate () {
    var win = new Gtk.ApplicationWindow (this);
    win.present();
  }
}

int main() {
  var app = new App ();
  return app.run();
}
