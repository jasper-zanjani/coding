private void show_contact_sheet (Contact contact)
    requires (this.contact != null) {
  remove_contact_sheet ();
  var contacts_sheet = new ContactSheet (contact);
  contacts_sheet.hexpand = true;
  this.sheet = contacts_sheet;
  this.contact_sheet_clamp.set_child (this.sheet);
  this.stack.set_visible_child_name ("contact-sheet-page");

  // Show potential link suggestions only if it's an existing contact
  if (contact.individual != null) {
    var matches = this.store.aggregator.get_potential_matches (contact.individual, MatchResult.HIGH);
    foreach (var i in matches.keys) {
      if (i != null && this.store.suggest_link_to (contact.individual, i)) {
        add_suggestion (contact.individual, i);
        break;
      }
    }
  }
}
