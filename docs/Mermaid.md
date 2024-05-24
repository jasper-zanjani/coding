# Mermaid

#### [flowcharts](https://mermaid.js.org/syntax/flowchart.html)
:   

    ```mermaid
    flowchart LR
        A[Hard edge] -->|Link text| B(Round edge)
        B --> C{Decision}
        C -->|One| D[Result one]
        C -->|Two| E[Result two]
    ```

    ```
    flowchart LR
        A[Hard edge] -->|Link text| B(Round edge)
        B --> C{Decision}
        C -->|One| D[Result one]
        C -->|Two| E[Result two]
    ```



#### [gitGraph](http://mermaid.js.org/syntax/gitgraph.html)
:   

    ```mermaid
    %%{init: { 'logLevel': 'debug', 'theme': 'base', 'gitGraph': {'rotateCommitLabel': false}} }%%
    gitGraph
        commit id: "feat(api): ..."
        commit id: "a"
        commit id: "b"
        commit id: "fix(client): .extra long label.."
        branch c2
        commit id: "feat(modules): ..."
        commit id: "test(client): ..."
        checkout main
        commit id: "fix(api): ..."
        commit id: "ci: ..."
        branch b1
        commit
        branch b2
        commit
    ```

    ``` title="gitGraph"
    %%{init: { 'logLevel': 'debug', 'theme': 'base', 'gitGraph': {'rotateCommitLabel': false}} }%%
    gitGraph
        commit id: "feat(api): ..."
        commit id: "a"
        commit id: "b"
        commit id: "fix(client): .extra long label.."
        branch c2
        commit id: "feat(modules): ..."
        commit id: "test(client): ..."
        checkout main
        commit id: "fix(api): ..."
        commit id: "ci: ..."
        branch b1
        commit
        branch b2
        commit
    ```
