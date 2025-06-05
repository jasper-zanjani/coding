public void show_contact (Individual? individual) {
  if (individual == null) {
    this.contact = null;
    remove_contact_sheet ();
    this.stack.set_visible_child_name ("none-selected-page");
    return;
  }

  if (this.contact == null || this.contact.individual != individual) {
    this.contact = new Contact.for_individual (individual);
  }
  show_contact_sheet (this.contact);
}
