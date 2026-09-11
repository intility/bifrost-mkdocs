# Tables

Extensions: `tables`, `intility_bifrost_zensical.table_ext`

The `table_ext` extension gives every table the Bifrost `bf-table` look. Tables you give a class yourself are left alone.

## Column Alignment

=== "Result"

    | Feature | Status | Priority | Notes |
    |:--------|:------:|----------:|-------|
    | Dark mode | Supported | High | Auto-switches with OS preference |
    | Search | Supported | High | Full-text with suggestions |
    | Mermaid | Supported | Medium | Flowcharts, sequence, and more |
    | Code copy | Supported | Low | One-click copy on code blocks |

=== "Markdown"

    ```markdown
    | Feature | Status | Priority | Notes |
    |:--------|:------:|----------:|-------|
    | Dark mode | Supported | High | Auto-switches ... |
    | Search | Supported | High | Full-text ... |
    | Mermaid | Supported | Medium | Flowcharts ... |
    | Code copy | Supported | Low | One-click copy ... |
    ```

## Alignment Syntax

```markdown
|:--------|   <!-- left-aligned (default) -->
|:--------:|  <!-- center-aligned -->
|---------:|  <!-- right-aligned -->
```
