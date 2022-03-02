"""Initialize markdown parser."""

__author__ = 'Jesse P. Johnson'
__title__ = 'mdparse'
__version__ = '0.1.0'
__license__ = 'LGPL-3.0'
__all__ = ['main']

import logging
import os
from pprint import pprint  # noqa
from typing import Any, Callable, Dict, List, Optional, Set  # noqa

from lark import Lark
# from lark.load_grammar import FromPackageLoader

from .transformer import MarkdownTransformer, TreeIndenter

logging.getLogger(__name__).addHandler(logging.NullHandler())

grammar_path = os.path.join(
    os.path.dirname(__file__), 'grammars', 'markdown.lark'
)


def loads(filepath: str) -> None:
    """Read markdown file."""
    # loader = FromPackageLoader(__name__, ('grammars',))
    # grammar = """
    # start: document

    # %import markdown.document
    # """
    with open(grammar_path) as grammar:
        markdown_parser = Lark(
            grammar,
            start='document',
            # parser='lalr',
            propagate_positions=False,
            maybe_placeholders=False,
            # import_paths=[loader],
            postlex=TreeIndenter(),  # type: ignore
        )
    with open(filepath) as f:
        markdown_tree = markdown_parser.parse('\n'.join(f))
    tree = MarkdownTransformer().transform(markdown_tree)
    pprint(tree)
    # print(tree.pretty())


def dumps() -> None:
    """Provide main function."""
    ...


def main() -> None:
    """Manage markdown."""
    # dumps()
    loads(filepath=os.path.join(os.getcwd(), 'CHANGELOG.md.example'))
