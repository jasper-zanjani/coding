win = self.props.active_window
if not win:
    win = TextEditorWindow(application=self)
win.present()
