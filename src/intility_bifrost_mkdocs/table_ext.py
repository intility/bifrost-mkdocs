"""Markdown extension that stamps Bifrost table classes onto generated tables.

Material renders Markdown tables as bare ``<table>`` elements. Bifrost's CSS
framework styles tables via the ``.bf-table`` class (see the vendored
``bifrost-all.css``). Rather than reimplement that look in our override layer,
this treeprocessor adds ``class="bf-table bfc-base-3-bg"`` to every generated
table at build time, so the real vendored rules apply verbatim. That means the
table styling automatically follows future Bifrost framework updates, structure
included, with no runtime JS and no flash of unstyled content.

Tables that already carry a class are left untouched, so authors who hand-class
a table keep full control (mirroring Material's own ``table:not([class])``
styling scope).
"""

from __future__ import annotations

from xml.etree.ElementTree import Element, SubElement

from markdown import Markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

BIFROST_TABLE_CLASS = "bf-table bfc-base-3-bg"


class BifrostTableTreeprocessor(Treeprocessor):
    """Style generated tables with Bifrost and restore the responsive wrapper.

    Two things happen to every classless ``<table>``:

    1. It gets ``class="bf-table bfc-base-3-bg"`` so the vendored Bifrost
       framework CSS styles it.
    2. It is wrapped in Material's ``.md-typeset__scrollwrap`` /
       ``.md-typeset__table`` structure so wide tables scroll horizontally
       instead of overflowing the page.

    Why we wrap it ourselves: Material adds that wrapper at runtime via JS, but
    its selector is ``table:not([class])`` -- so the moment we add a class, the
    table opts out of the wrapper and loses responsive scrolling. Emitting the
    same wrapper at build time restores the behaviour (and does so without a
    flash of unstyled content). Material's JS skips our already-classed table,
    so there is no double-wrap.

    Tables that already carry a class are left untouched, so authors keep full
    control (mirroring Material's own ``table:not([class])`` scope).
    """

    def run(self, root: Element) -> None:
        # ElementTree has no parent pointers, so build a child -> parent map.
        parents = {child: parent for parent in root.iter() for child in parent}

        for table in list(root.iter("table")):
            if table.get("class"):
                continue
            table.set("class", BIFROST_TABLE_CLASS)

            parent = parents.get(table)
            if parent is None:
                continue

            index = list(parent).index(table)
            scrollwrap = Element("div", {"class": "md-typeset__scrollwrap"})
            inner = SubElement(scrollwrap, "div", {"class": "md-typeset__table"})
            parent.remove(table)
            inner.append(table)
            parent.insert(index, scrollwrap)


class BifrostTableExtension(Extension):
    def extendMarkdown(self, md: Markdown) -> None:
        # Treeprocessors run after block parsing, so the <table> elements built
        # by the `tables` extension already exist in the tree. Priority only
        # orders among treeprocessors; a low value runs late, which is fine
        # since we only add an attribute. Register a stable name so it is
        # idempotent if the extension is added twice.
        md.treeprocessors.register(BifrostTableTreeprocessor(md), "bifrost_table", 5)


def makeExtension(**kwargs: object) -> BifrostTableExtension:
    """Python-Markdown entry point."""
    return BifrostTableExtension(**kwargs)
