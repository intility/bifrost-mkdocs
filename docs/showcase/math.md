# Math Equations

Extension: `pymdownx.arithmatex` + MathJax

## Inline Math

=== "Result"

    The Pythagorean theorem states that \(\alpha^2 + \beta^2 = \gamma^2\).

    Einstein's famous equation \(E = mc^2\) relates energy and mass.

=== "Markdown"

    ```markdown
    The Pythagorean theorem states that \(\alpha^2 + \beta^2 = \gamma^2\).

    Einstein's famous equation \(E = mc^2\) relates energy and mass.
    ```

## Block Equations

=== "Result"

    Euler's identity:

    \[
    e^{i\pi} + 1 = 0
    \]

    Gaussian integral:

    \[
    \int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
    \]

    Basel problem:

    \[
    \sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}
    \]

=== "Markdown"

    ```markdown
    Euler's identity:

    \[
    e^{i\pi} + 1 = 0
    \]

    Gaussian integral:

    \[
    \int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
    \]

    Basel problem:

    \[
    \sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}
    \]
    ```

## Syntax

```markdown
Inline: \(expression\)
Block:  \[ expression \]
```

MathJax is configured in `docs/javascripts/mathjax.js` and loaded via `extra_javascript` in `mkdocs.yaml`.
