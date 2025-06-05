private void show_contact (Folks.Individual? selected) {
  this.contact_pane.show_contact (selected);
  if (selected != null)
    this.content_box.show_content = true;

  // clearing right_header
  this.contact_pane_page.title = _("Select a Contact");
  this.right_header.show_title = false;
  if (selected != null) {
    update_favorite_actions (selected.is_favourite);
  }
  this.state = selected != null ? UiState.SHOWING : UiState.NORMAL;
}
