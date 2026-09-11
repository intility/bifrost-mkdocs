from __future__ import annotations

import markdown

from intility_bifrost_zensical.table_ext import BIFROST_TABLE_CLASS

TABLE_MD = """\
| Feature | Status |
| ------- | ------ |
| Search  | Yes    |
"""


def _render(text: str, extensions: list[str]) -> str:
    return markdown.markdown(text, extensions=extensions)


def test_classless_table_gets_bifrost_class():
    """A generated table with no class is stamped with the Bifrost classes."""
    html = _render(TABLE_MD, ["tables", "intility_bifrost_zensical.table_ext"])

    assert f'<table class="{BIFROST_TABLE_CLASS}">' in html


def test_classless_table_is_wrapped_for_scrolling():
    """The table is wrapped in Material's responsive scroll structure.

    Material's JS only wraps `table:not([class])`, so once we add a class we
    must emit the wrapper ourselves to keep wide tables scrollable.
    """
    html = _render(TABLE_MD, ["tables", "intility_bifrost_zensical.table_ext"])

    assert '<div class="md-typeset__scrollwrap">' in html
    assert '<div class="md-typeset__table">' in html
    # Wrapper sits outside the table, table inside.
    assert html.index("md-typeset__scrollwrap") < html.index("bf-table")


def test_existing_class_preserved():
    """An author-classed table is left untouched (md_in_html + attr_list)."""
    html = _render(
        '<table class="custom" markdown>\n<tr><td>cell</td></tr>\n</table>\n',
        ["tables", "md_in_html", "attr_list", "intility_bifrost_zensical.table_ext"],
    )

    assert 'class="custom"' in html
    assert "bf-table" not in html
    assert "md-typeset__scrollwrap" not in html
