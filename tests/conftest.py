# type: ignore
"""Provide PyTest configuration."""

from lark import Lark
# from lark.load_grammar import FromPackageLoader
from pytest import fixture

from mdparse import grammar_path
from mdparse.transformer import TreeIndenter


@fixture()
def parser():
    """Create parser for tests."""
    # XXX: this changes namespace with
    # loader = FromPackageLoader('mdparse', ('grammars',))
    # grammar = """
    # start: document

    # %import markdown.document -> document
    # """
    with open(grammar_path) as f:
        return Lark(
            '\n'.join(f),
            start='document',
            # parser='lalr',
            propagate_positions=False,
            maybe_placeholders=False,
            # import_paths=[loader],
            postlex=TreeIndenter(),
        )
