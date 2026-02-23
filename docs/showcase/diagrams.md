# Diagrams

Extension: `pymdownx.superfences` with custom mermaid fence

## Flowchart

=== "Result"

    ```mermaid
    graph TD
        A[Start] --> B{Configuration valid?}
        B -->|Yes| C[Load theme]
        B -->|No| D[Show error]
        C --> E[Build pages]
        E --> F[Apply Bifrost styling]
        F --> G[Generate output]
        D --> H[Exit]
        G --> I[Deploy]
    ```

=== "Markdown"

    ````markdown
    ```mermaid
    graph TD
        A[Start] --> B{Configuration valid?}
        B -->|Yes| C[Load theme]
        B -->|No| D[Show error]
        C --> E[Build pages]
        E --> F[Apply Bifrost styling]
        F --> G[Generate output]
        D --> H[Exit]
        G --> I[Deploy]
    ```
    ````

## Sequence Diagram

=== "Result"

    ```mermaid
    sequenceDiagram
        participant U as User
        participant B as Browser
        participant S as MkDocs Server
        participant T as Theme Engine

        U->>B: Navigate to page
        B->>S: Request page
        S->>T: Render Markdown
        T->>T: Apply Bifrost CSS
        T-->>S: HTML + styles
        S-->>B: Complete page
        B-->>U: Display content
    ```

=== "Markdown"

    ````markdown
    ```mermaid
    sequenceDiagram
        participant U as User
        participant B as Browser
        participant S as MkDocs Server
        participant T as Theme Engine

        U->>B: Navigate to page
        B->>S: Request page
        S->>T: Render Markdown
        T->>T: Apply Bifrost CSS
        T-->>S: HTML + styles
        S-->>B: Complete page
        B-->>U: Display content
    ```
    ````

## Supported Diagram Types

Mermaid supports many diagram types out of the box. See the [Mermaid documentation](https://mermaid.js.org/) for the full list, including:

- Flowcharts
- Sequence diagrams
- Class diagrams
- State diagrams
- Entity relationship diagrams
- Gantt charts
- Pie charts
- Git graphs
