# Tables

Extension: `tables`

## Column Alignment

=== "Result"

    | Feature | Status | Priority | Notes |
    |:--------|:------:|----------:|-------|
    | Dark mode | Supported | High | Auto-switches with OS preference |
    | Search | Supported | High | Full-text with suggestions |
    | Mermaid | Supported | Medium | Flowcharts, sequence, and more |
    | MathJax | Supported | Low | Inline and block equations |

=== "Markdown"

    ```markdown
    | Feature | Status | Priority | Notes |
    |:--------|:------:|----------:|-------|
    | Dark mode | Supported | High | Auto-switches ... |
    | Search | Supported | High | Full-text ... |
    | Mermaid | Supported | Medium | Flowcharts ... |
    | MathJax | Supported | Low | Inline and block ... |
    ```

## Alignment Syntax

```markdown
|:--------|   <!-- left-aligned (default) -->
|:--------:|  <!-- center-aligned -->
|---------:|  <!-- right-aligned -->
```
