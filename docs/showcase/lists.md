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
    - [x] Configure Zensical with the Bifrost theme
    - [x] Add Bifrost styling
    - [ ] Write all documentation
    - [ ] Deploy to production

=== "Markdown"

    ```markdown
    - [x] Create the project structure
    - [x] Configure Zensical with the Bifrost theme
    - [x] Add Bifrost styling
    - [ ] Write all documentation
    - [ ] Deploy to production
    ```

## Definition List

=== "Result"

    **Zensical**
    :   A static site generator for project documentation, the successor to MkDocs and Material for MkDocs.

    **Bifrost Zensical**
    :   A packaged Zensical theme applying Intility's Bifrost design system.

    **Bifrost**
    :   Intility's design system, providing consistent colors, typography, and component styling.

=== "Markdown"

    ```markdown
    **Zensical**
    :   A static site generator for project documentation, the
        successor to MkDocs and Material for MkDocs.

    **Bifrost Zensical**
    :   A packaged Zensical theme applying Intility's Bifrost
        design system.

    **Bifrost**
    :   Intility's design system, providing consistent colors,
        typography, and component styling.
    ```
