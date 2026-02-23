# Code Blocks

Extensions: `pymdownx.highlight`, `pymdownx.superfences`, `pymdownx.inlinehilite`

Features: `content.code.copy`, `content.code.annotate`

## Syntax Highlighting

=== "Result"

    ```python
    def fibonacci(n: int) -> list[int]:
        """Generate the first n Fibonacci numbers."""
        if n <= 0:
            return []
        sequence = [0, 1]
        for _ in range(2, n):
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[:n]
    ```

=== "Markdown"

    ````markdown
    ```python
    def fibonacci(n: int) -> list[int]:
        """Generate the first n Fibonacci numbers."""
        if n <= 0:
            return []
        sequence = [0, 1]
        for _ in range(2, n):
            sequence.append(sequence[-1] + sequence[-2])
        return sequence[:n]
    ```
    ````

## Line Numbers and Highlighted Lines

=== "Result"

    ```python linenums="1" hl_lines="3 4 5"
    import os
    from pathlib import Path

    # These lines are highlighted
    CONFIG_DIR = Path(os.environ.get("CONFIG_DIR", "~/.config"))
    CONFIG_FILE = CONFIG_DIR / "settings.yaml"

    def load_config():
        return CONFIG_FILE.read_text()
    ```

=== "Markdown"

    ````markdown
    ```python linenums="1" hl_lines="3 4 5"
    import os
    from pathlib import Path

    # These lines are highlighted
    CONFIG_DIR = Path(os.environ.get("CONFIG_DIR", "~/.config"))
    CONFIG_FILE = CONFIG_DIR / "settings.yaml"

    def load_config():
        return CONFIG_FILE.read_text()
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

    - Python: `#!python range(10)` generates numbers 0 through 9
    - JavaScript: `#!javascript console.log("hello")` writes to the console
    - Bash: `#!bash echo $PATH` prints the PATH variable

=== "Markdown"

    ```markdown
    - Python: `#!python range(10)` generates numbers 0 through 9
    - JavaScript: `#!javascript console.log("hello")` writes to the console
    - Bash: `#!bash echo $PATH` prints the PATH variable
    ```
