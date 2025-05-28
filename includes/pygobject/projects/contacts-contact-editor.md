**ContactEditor**

Properties:




Methods:

---

**PersonaEditor**

Properties:

Methods:

-   `ensure_chunks()`
-   `add_show_more_button()` creates the "Show More" button in the editor view.

```blueprint "Show More button"
Adw.PreferencesGroup {
  Adw.ButtonRow {
    title: _("_Show More");
    start-icon-name: "view-more-symbolic";
    use-underline: true;
  }
}
```

---

