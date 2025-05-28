!!! info "Workflow"

    1.  

        The **includes** folder is organized into languages and major libraries representing a campaign (i.e. GTK or Rust).
        Each campaign directory is organized into subdirectories representing tutorials, projects, or major language features.
        Each project, when it can be iterated, is subdivided into numbered folders.
        This allows each project iteration to be contained separately.

    2.  

        In the **docs** folder, create a Study directory under the associated campaign which will contain a markdown document for each project.
        This document will illustrate changes made between iterations as well as commentary on what was learned and what was challenging, like a journal.
        These Study documents can be numbered in reverse sequence (i.e. starting from 99 and counting down) in order to make sure that the most recent project is on top no matter the alphabetic order of titles.
        Once enough of the campaign has been learned to distill well-structured Tasks, those are placed in a separate folder.
        
    3.  Create an Anki cloze note corresponding to each Task.


!!! info "Coding challenges"

    -   [Coderwars](https://www.codewars.com)
    -   [CodeCrafters](https://app.codecrafters.io/)

#### CLI DB utility idea

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
