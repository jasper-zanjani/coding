def create_action(self, name, callback, shortcuts=None):
    action = Gio.SimpleAction.new(name, None)
    action.connect("activate", callback)
    self.add_action(action)
    if shortcuts:
        self.set_accels_for_action(f"app.{name}", shortcuts)
