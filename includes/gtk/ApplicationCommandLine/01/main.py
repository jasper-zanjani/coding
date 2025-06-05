import sys
import gi
gi.require_version("Gio", "2.0")
gi.require_version("GLib", "2.0")
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib, Gio

class ApplicationCommandLineExample (Gtk.Application):
    def __init__(self, *args, **kwargs): # (1)
        super().__init__(*args, **kwargs)
        name_option = GLib.OptionEntry()
        name_option.long_name = "name"
        name_option.short_name = ord('n') # 110
        name_option.arg = GLib.OptionArg.STRING
        name_option.description="Greet the specified name"
        name_option.flags=GLib.OptionFlags.NONE # 0
        options = [name_option]
        self.add_main_option_entries(options)

    def do_command_line(self, command_line) -> int: # (2)
        options = command_line.get_options_dict()
        name = options.lookup_value("name", expected_type=GLib.VariantType(type_string="s"))
        if name is None:
            print("Hello, World!")
        else:
            print(f"Hello, {name.get_string()}")
        return 0


    def do_activate(self): # (3)
        pass

if __name__ == "__main__":
    app = ApplicationCommandLineExample(flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE) # (4)
    app.run(sys.argv)
