# Admonitions

Extensions: `admonition`, `pymdownx.details`

Material for MkDocs supports two syntaxes for admonitions: the standard `!!!` syntax and GitHub-style alert blocks using `> [!TYPE]`.

## GitHub Alert Syntax

=== "Result"

    > [!NOTE]
    > Useful for highlighting information that users should take into account.

    > [!TIP]
    > Helpful advice for getting the most out of a feature.

    > [!IMPORTANT]
    > Key information users need to know.

    > [!WARNING]
    > Something that could cause problems if ignored.

    > [!CAUTION]
    > Actions that are irreversible or could cause data loss.

=== "Markdown"

    ```markdown
    > [!NOTE]
    > Useful for highlighting information that users should take into account.

    > [!TIP]
    > Helpful advice for getting the most out of a feature.

    > [!IMPORTANT]
    > Key information users need to know.

    > [!WARNING]
    > Something that could cause problems if ignored.

    > [!CAUTION]
    > Actions that are irreversible or could cause data loss.
    ```

## All 12 Admonition Types

=== "Result"

    !!! note "Note"
        Useful for highlighting information that users should take into account.

    !!! abstract "Abstract"
        A brief summary of the content that follows.

    !!! info "Info"
        Supplementary information that adds context.

    !!! tip "Tip"
        Helpful advice for getting the most out of a feature.

    !!! success "Success"
        Indicates that an action completed as expected.

    !!! question "Question"
        Prompts the reader to think about something or highlights common questions.

    !!! warning "Warning"
        Something that could cause problems if ignored.

    !!! failure "Failure"
        Indicates that something did not work or is not supported.

    !!! danger "Danger"
        Actions that are irreversible or could cause data loss.

    !!! bug "Bug"
        Known issues or unexpected behavior.

    !!! example "Example"
        A practical demonstration of a concept.

    !!! quote "Quote"
        A citation or noteworthy statement.

=== "Markdown"

    ```markdown
    !!! note "Note"
        Useful for highlighting information.

    !!! abstract "Abstract"
        A brief summary of the content.

    !!! info "Info"
        Supplementary information.

    !!! tip "Tip"
        Helpful advice.

    !!! success "Success"
        Indicates that an action completed.

    !!! question "Question"
        Highlights common questions.

    !!! warning "Warning"
        Something that could cause problems.

    !!! failure "Failure"
        Something did not work.

    !!! danger "Danger"
        Irreversible or destructive actions.

    !!! bug "Bug"
        Known issues or unexpected behavior.

    !!! example "Example"
        A practical demonstration.

    !!! quote "Quote"
        A citation or noteworthy statement.
    ```

## Collapsible Admonitions

=== "Result"

    ??? note "Collapsed by default (click to expand)"
        This content is hidden until the reader clicks the header.
        You can put any content here, including code blocks and lists.

    ???+ tip "Expanded by default (click to collapse)"
        This admonition starts open but can be collapsed by clicking the header.

=== "Markdown"

    ```markdown
    ??? note "Collapsed by default (click to expand)"
        This content is hidden until the reader clicks.

    ???+ tip "Expanded by default (click to collapse)"
        This admonition starts open but can be collapsed.
    ```

## Syntax Comparison

| GitHub Alerts | Standard Syntax |
|---|---|
| `> [!NOTE]` | `!!! note` |
| `> [!TIP]` | `!!! tip` |
| `> [!IMPORTANT]` | `!!! info` |
| `> [!WARNING]` | `!!! warning` |
| `> [!CAUTION]` | `!!! danger` |

The standard `!!!` syntax gives access to all 12 types and supports collapsible blocks (`???` / `???+`). GitHub alerts are limited to 5 types but work on GitHub and other renderers too.
