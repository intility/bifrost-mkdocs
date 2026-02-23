# Lists

Extensions: `pymdownx.tasklist`, `def_list`

## Unordered List

=== "Result"

    - First item
    - Second item
        - Nested item A
        - Nested item B
            - Deeply nested
    - Third item

=== "Markdown"

    ```markdown
    - First item
    - Second item
        - Nested item A
        - Nested item B
            - Deeply nested
    - Third item
    ```

## Ordered List

=== "Result"

    1. First step
    2. Second step
        1. Sub-step A
        2. Sub-step B
    3. Third step

=== "Markdown"

    ```markdown
    1. First step
    2. Second step
        1. Sub-step A
        2. Sub-step B
    3. Third step
    ```

## Task List

=== "Result"

    - [x] Create the project structure
    - [x] Configure MkDocs with Material theme
    - [x] Add Bifrost styling
    - [ ] Write all documentation
    - [ ] Deploy to production

=== "Markdown"

    ```markdown
    - [x] Create the project structure
    - [x] Configure MkDocs with Material theme
    - [x] Add Bifrost styling
    - [ ] Write all documentation
    - [ ] Deploy to production
    ```

## Definition List

=== "Result"

    **MkDocs**
    :   A static site generator for project documentation, written in Python.

    **Material for MkDocs**
    :   A theme for MkDocs that provides a modern, responsive design with many built-in features.

    **Bifrost**
    :   Intility's design system, providing consistent colors, typography, and component styling.

=== "Markdown"

    ```markdown
    **MkDocs**
    :   A static site generator for project documentation, written in Python.

    **Material for MkDocs**
    :   A theme for MkDocs that provides a modern, responsive design
        with many built-in features.

    **Bifrost**
    :   Intility's design system, providing consistent colors,
        typography, and component styling.
    ```
