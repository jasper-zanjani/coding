self.create_action("about", self._on_about_activated)
self.create_action('quit', lambda *_: self.app.quit(), ['<primary>q'])
#self.create_action("shortcuts", self._on_shortcuts_activated,  ['<primary>question'])

self.create_action("open", lambda *_: self.on_open_clicked(None), ["<Primary>o"])
self.create_action("save", lambda *_: self.on_save_clicked(None) if self.save_btn and self.save_btn.get_sensitive() else None, ["<Primary>s"])
self.create_action("copy", lambda *_: self.on_copy_button_clicked(), ["<Primary>c"])
self.create_action("paste", lambda *_: self.on_copy_from_clicked(None), ["<Primary>v"])

