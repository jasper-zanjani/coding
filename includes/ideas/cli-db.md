```
# Create db named boxes, which then is treated as a subcommand
db --new boxes

# Sane defaults for data types when defining schema
db boxes schema name location number contents

# DB is only lazily created after first good record is created
db boxes add box1 ceiling 24 blablabla

# Print social security record in default db
db my ss

db set my ss 123-45-6789
```
