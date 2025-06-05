private void on_setup_item (Object object) {
  unowned var item = (Gtk.ListItem) object;

  // Create the row widget
  var row = new ContactListRow ();
  item.child = row;

  // Update the selection mode on state changes
  row.selection_mode = (this.state == UiState.SELECTING);
  var state_notify_handler = this.notify["state"].connect ((obj, pspec) => {
    row.selection_mode = (this.state == UiState.SELECTING);
  });
  item.set_data<ulong> ("state-notify-handler", state_notify_handler);

  // Bind the GtkItemList "selected" property, we use it for the checkmark
  var sel_binding = item.bind_property ("selected", row, "selected",
                                        BindingFlags.SYNC_CREATE);
  item.set_data<Binding> ("sel-binding", sel_binding);

  // Listen to the toggle-marked signal
  row.toggle_marked.connect ((select) => {
    this.state = UiState.SELECTING;
    if (!select)
      return;

    if (this.selection_model.is_selected (item.position)) {
      this.selection_model.unselect_item (item.position);
    } else {
      this.selection_model.select_item (item.position, false);
    }
  });
}
