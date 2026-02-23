# Keyboard Keys

Extension: `pymdownx.keys`

Render keyboard shortcuts and key combinations with styled key caps.

## Examples

=== "Result"

    - Copy: ++ctrl+c++ (or ++cmd+c++ on macOS)
    - Paste: ++ctrl+v++
    - Save: ++ctrl+s++
    - Command palette: ++cmd+shift+p++
    - Find: ++ctrl+f++
    - Undo: ++ctrl+z++

=== "Markdown"

    ```markdown
    - Copy: ++ctrl+c++ (or ++cmd+c++ on macOS)
    - Paste: ++ctrl+v++
    - Save: ++ctrl+s++
    - Command palette: ++cmd+shift+p++
    - Find: ++ctrl+f++
    - Undo: ++ctrl+z++
    ```

## Syntax

Wrap key names in `++` and separate combinations with `+`:

```markdown
++key++            <!-- single key -->
++ctrl+c++         <!-- key combination -->
++cmd+shift+p++    <!-- three-key combination -->
```
