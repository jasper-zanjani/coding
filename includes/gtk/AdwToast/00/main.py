import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class MyApp(Adw.Application):
    def do_activate(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.ui")

        win = self.props.active_window
        if not win:
            win = self.builder.get_object("main_window")
        win.set_application(self)
        win.present()

        self.button = self.builder.get_object("button")
        self.button.connect("clicked", self.on_clicked_button)

    def on_clicked_button(self, button):
        def toast_cb(toast):
            self.button.sensitive = True
        toast = Adw.Toast.new("Toasty!")
        toast.connect("dismissed", toast_cb)
        toast_overlay = self.builder.get_object("toast_overlay")
        toast_overlay.add_toast(toast)
        self.button.sensitive = False



if __name__ == "__main__":
    app = MyApp()
    app.run()
