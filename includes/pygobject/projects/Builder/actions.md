The template provided by Builder provides a `create_action` method aiming to reduce complexity of adding actions.

```py title="main.py create_action(excerpt)"
--8<-- "includes/pygobject/projects/Builder/Builder.create_action.py"
```

Actions associated with "show-help-overlay" do not appear in code, although a separate UI definition file is available which must also be automatically processed somehow.

```blueprint
--8<-- "includes/pygobject/builder/help-overlay.blp"
```
