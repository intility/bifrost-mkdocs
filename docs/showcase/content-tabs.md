# Content Tabs

Extension: `pymdownx.tabbed`

Feature: `content.tabs.link` (syncs tab selection across the page)

## Basic Tabs

=== "Tab One"

    Content for the first tab. Tabs are useful for showing platform-specific
    instructions or alternative approaches.

=== "Tab Two"

    Content for the second tab. All tabs within a group stay in sync across the
    page when `content.tabs.link` is enabled.

=== "Tab Three"

    Content for the third tab. You can nest any Markdown content inside tabs,
    including code blocks, admonitions, and lists.

**Syntax:**

```markdown
=== "Tab One"

    Content for the first tab.

=== "Tab Two"

    Content for the second tab.

=== "Tab Three"

    Content for the third tab.
```

## Code Tabs

A common use case is showing the same example in multiple languages:

=== "Python"

    ```python
    def greet(name: str) -> str:
        return f"Hello, {name}!"
    ```

=== "JavaScript"

    ```javascript
    function greet(name) {
        return `Hello, ${name}!`;
    }
    ```

=== "Go"

    ```go
    func greet(name string) string {
        return fmt.Sprintf("Hello, %s!", name)
    }
    ```

=== "Bash"

    ```bash
    greet() {
        echo "Hello, $1!"
    }
    ```

**Syntax:**

````markdown
=== "Python"

    ```python
    def greet(name: str) -> str:
        return f"Hello, {name}!"
    ```

=== "JavaScript"

    ```javascript
    function greet(name) {
        return `Hello, ${name}!`;
    }
    ```
````
