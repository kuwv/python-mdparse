# type: ignore
"""Test markdown backquote."""

from textwrap import dedent

from lark import Lark

from mdparse.transformer import MarkdownTransformer, TreeIndenter

list_grammar = r"""\
document: _NL* paragraph _NL*

paragraph: /\b.+\Z/

%declare _INDENT _DEDENT

%import common.CNAME
%import common.INT
// %import common.NEWLINE -> _NL
%import common.LETTER
%import common.NUMBER
%import common.WORD
// %import common.WS
%import common.WS_INLINE

// ignore whitespace
// %ignore WS
// or ignore inline whitespace
%ignore WS_INLINE

_NL: /(\r?\n[\t ]*)+/
"""

parser = Lark(
    list_grammar,
    start='document',
    propagate_positions=False,
    maybe_placeholders=False,
    # import_paths=[loader],
    postlex=TreeIndenter(),
)


def test_paragraphs(parser):
    """Test various backquote content."""
    parse_result = parser.parse(
        dedent(
            """\
            I really like using Markdown.

            I think I'll use it to format all of my documents from now on.
            """
        )
    )
    tree = MarkdownTransformer().transform(parse_result)
    print(tree)


def test_paragraph_line_breaks(parser):
    """Test nested backquote."""
    parse_result = parser.parse(
        dedent(
            """\
             This is the first line.
             And this is the second line.
            """
        )
    )
    tree = MarkdownTransformer().transform(parse_result)
    print(tree)
