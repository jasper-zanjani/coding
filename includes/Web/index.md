# Web

## Observable Framework

[**Observable Framework**](https://observablehq.com/framework/what-is-framework) or Framework is an open-source static-site generator for data apps deployed as a Node.js application avaiable via npm.
Framework combines a static site generator that compiles Markdown, JS, and other sources with a command-line interface as well as a local development server (1).
{ .annotate }

1. 
```sh title="Run local development server"
--8<-- "includes/Commands/y/yarn-dev.sh"
```


A Framework project consists of a home page and additional assets that could include data loaders, static data files, and other assets.
Pages are written in [extended Markdown](https://observablehq.com/framework/markdown#markdown) with support for HTML, JavaScript, SQL, YAML front matter and other languages.
The [structure](https://observablehq.com/framework/project-structure#project-structure) (1) of Framework projects centers on the main **src** directory which is the "source root". 
Projects can be created with interactive prompts. (2)
{ .annotate }

1. 
```
.
├─ src                    # source root
│  ├─ .observablehq
│  │  ├─ cache            # data loader cache
│  │  └─ deploy.json      # deployment metadata
│  ├─ components
│  │  └─ dotmap.js        # shared JavaScript module
│  ├─ data
│  │  └─ quakes.csv.ts    # data loader
│  ├─ index.md            # home page
│  └─ quakes.md           # page
├─ .gitignore
├─ README.md
├─ observablehq.config.js # project configuration
├─ package.json           # node package dependencies
└─ yarn.lock              # node package lockfile
```
2. 
```sh
# Create a new project with npm
npm init @observablehq

# Create a new project with yarn
yarn create @observablehq
```

Observable uses [file-based routing](https://observablehq.com/framework/project-structure#routing), meaning each page in the site has a corresponding Markdown file of the same name.

Javascript fenced code blocks are used to display content such as charts and inputs.

