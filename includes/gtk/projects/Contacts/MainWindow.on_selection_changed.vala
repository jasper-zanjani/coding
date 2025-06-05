private void on_selection_changed (Gtk.SelectionModel marked,
                                   uint position,
                                   uint n_changed) {
  unowned var selected = get_selected_individual ();

  // Update related actions
  unowned var unlink_action = lookup_action ("unlink-contact");
  ((SimpleAction) unlink_action).set_enabled (selected != null && selected.personas.size > 1);

  if (this.state == UiState.SELECTING) {
    // We really want to treat selection mode specially
    return;
  } else {
    show_contact (selected);
  }
}
