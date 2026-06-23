# Attributes

Extension: `attr_list`

`attr_list` attaches HTML attributes (classes, IDs, and key/value pairs) to Markdown elements using a `{ ... }` block placed right after the element.

## Link Attributes

Add attributes like `target` and `title` to a link:

=== "Result"

    [Open in a new tab](https://www.mkdocs.org/){ target=_blank rel=noopener title="MkDocs documentation" }

=== "Markdown"

    ```markdown
    [Open in a new tab](https://www.mkdocs.org/){ target=_blank rel=noopener title="MkDocs documentation" }
    ```

## Icon Sizing and Alignment

Icons accept the `.lg` / `.xl` size helpers and the `.middle` alignment helper:

=== "Result"

    :material-rocket-launch:{ .lg .middle } Large icon, vertically centered with the text.

=== "Markdown"

    ```markdown
    :material-rocket-launch:{ .lg .middle } Large icon, vertically centered with the text.
    ```

## Custom Heading IDs

Override the auto-generated anchor for a heading so you can link to it with a stable URL:

```markdown
## Configuration { #config }

Jump to it with [the config section](#config).
```

## Syntax

```markdown
[text](url){ key=value .class #id }   <!-- on a link -->
:icon-name:{ .lg .middle }            <!-- on an icon -->
## Heading { #custom-id }             <!-- on a heading -->
```

Separate multiple attributes with spaces: `.class` sets a CSS class, `#id` sets an ID, and `key=value` sets any other HTML attribute.
