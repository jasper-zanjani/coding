The C compiler raises warnings about the use of the `volatile` qualifier in GLib macros which are not resolvable by an application developer.

``` title="Example"
In file included from /usr/include/glib-2.0/glib/gthread.h:34,
                 from /usr/include/glib-2.0/glib/gasyncqueue.h:34,
                 from /usr/include/glib-2.0/glib.h:34,
                 from /usr/include/gtk-4.0/gtk/css/gtkcss.h:29,
                 from /usr/include/gtk-4.0/gtk/gtk.h:29,
                 from /home/jasper/Documents/git/coding/includes/vala/ApplicationCommandLine/01/main.vala.c:4:
/home/jasper/Documents/git/coding/includes/vala/ApplicationCommandLine/01/main.vala.c: In function ‘application_command_line_example_get_type’:
/usr/include/glib-2.0/glib/gatomic.h:131:5: warning: argument 2 of ‘__atomic_load’ discards ‘volatile’ qualifier [-Wdiscarded-qualifiers]
  131 |     __atomic_load (gapg_temp_atomic, &gapg_temp_newval, __ATOMIC_SEQ_CST); \
      |     ^~~~~~~~~~~~~
/usr/include/glib-2.0/glib/gthread.h:274:7: note: in expansion of macro ‘g_atomic_pointer_get’
  274 |     (!g_atomic_pointer_get (location) &&                             \
      |       ^~~~~~~~~~~~~~~~~~~~
/home/jasper/Documents/git/coding/includes/vala/ApplicationCommandLine/01/main.vala.c:147:13: note: in expansion of macro ‘g_once_init_enter’
  147 |         if (g_once_init_enter (&application_command_line_example_type_id__once)) {
      |             ^~~~~~~~~~~~~~~~~
```
