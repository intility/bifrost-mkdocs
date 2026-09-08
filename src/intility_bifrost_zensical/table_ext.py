"""Markdown extension that stamps Bifrost table classes onto generated tables."""

from __future__ import annotations

from xml.etree.ElementTree import Element, SubElement

from markdown import Markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

BIFROST_TABLE_CLASS = "bf-table bfc-base-3-bg"


class BifrostTableTreeprocessor(Treeprocessor):
    def run(self, root: Element) -> None:
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
        md.treeprocessors.register(BifrostTableTreeprocessor(md), "bifrost_table", 5)


def makeExtension(**kwargs: object) -> BifrostTableExtension:
    return BifrostTableExtension(**kwargs)
