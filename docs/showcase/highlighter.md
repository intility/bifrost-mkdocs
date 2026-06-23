# Highlighter

Extensions: `pymdownx.highlight`, `pymdownx.superfences`, `pymdownx.inlinehilite`

Features: `content.code.copy`, `content.code.annotate`

## Syntax Highlighting

Colors mirror the [Bifrost Highlighter](https://bifrost.intility.com/react/highlighter):
keywords, control flow, functions, strings, and numbers each map to a fixed
Bifrost token color.

=== "Result"

    ```typescript
    interface User {
      id: number;
      name: string;
    }

    async function fetchUser(id: number): Promise<User> {
      const response = await fetch(`/api/users/${id}`);
      if (!response.ok) {
        throw new Error(`User ${id} not found`);
      }
      return response.json();
    }
    ```

=== "Markdown"

    ````markdown
    ```typescript
    interface User {
      id: number;
      name: string;
    }

    async function fetchUser(id: number): Promise<User> {
      const response = await fetch(`/api/users/${id}`);
      if (!response.ok) {
        throw new Error(`User ${id} not found`);
      }
      return response.json();
    }
    ```
    ````

## Titled Code Block

A `title="…"` fence renders a header bar (language label or filename) with the
copy button, matching the Bifrost Highlighter's `header` prop.

=== "Result"

    ```go title="main.go"
    package main

    import "fmt"

    func main() {
        fmt.Println(greet("world"))
    }

    func greet(name string) string {
        return fmt.Sprintf("Hello, %s!", name)
    }
    ```

=== "Markdown"

    ````markdown
    ```go title="main.go"
    package main
    ...
    ```
    ````

## Line Numbers and Highlighted Lines

=== "Result"

    ```rust linenums="1" hl_lines="3 4"
    fn main() {
        let numbers = vec![1, 2, 3, 4, 5];
        // These two lines are highlighted
        let sum: i32 = numbers.iter().sum();
        println!("Sum of {numbers:?} is {sum}");
    }
    ```

=== "Markdown"

    ````markdown
    ```rust linenums="1" hl_lines="3 4"
    fn main() {
        let numbers = vec![1, 2, 3, 4, 5];
        // These two lines are highlighted
        let sum: i32 = numbers.iter().sum();
        println!("Sum of {numbers:?} is {sum}");
    }
    ```
    ````

## Code Annotations

=== "Result"

    ```yaml
    site_name: My Documentation # (1)!
    theme:
      name: material # (2)!
      palette:
        primary: teal # (3)!
    ```

    1. The name displayed in the browser tab and header.
    2. Material for MkDocs provides the theme engine.
    3. Bifrost supports `teal`, `purple`, `pink`, and `yellow`.

=== "Markdown"

    ````markdown
    ```yaml
    site_name: My Documentation # (1)!
    theme:
      name: material # (2)!
      palette:
        primary: teal # (3)!
    ```

    1. The name displayed in the browser tab and header.
    2. Material for MkDocs provides the theme engine.
    3. Bifrost supports `teal`, `purple`, `pink`, and `yellow`.
    ````

## Inline Code Highlighting

=== "Result"

    - SQL: `#!sql SELECT * FROM users WHERE id = 1` reads a single row
    - CSS: `#!css color: var(--bfc-base-c)` reads a Bifrost token
    - Bash: `#!bash echo $PATH` prints the PATH variable

=== "Markdown"

    ```markdown
    - SQL: `#!sql SELECT * FROM users WHERE id = 1` reads a single row
    - CSS: `#!css color: var(--bfc-base-c)` reads a Bifrost token
    - Bash: `#!bash echo $PATH` prints the PATH variable
    ```
