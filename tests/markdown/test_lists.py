# type: ignore
"""Test markdown backquote."""

from lark import Lark

from textwrap import dedent
from mdparse.transformer import MarkdownTransformer, TreeIndenter

list_grammar = r"""\
document: _NL* (unordered_list | ordered_list)

unordered_list: ("-" TEXT _NL | sublist)+

ordered_list: (num_item _NL | sublist)+
?num_item: INT "." TEXT

?sublist: _INDENT lists _DEDENT
?lists: ordered_list | unordered_list

ATEXT: /.*/
TEXT: LETTER (CNAME | NUMBER | WS_INLINE | ESCAPE_CHAR)+
ESCAPE_CHAR: "'"
    | "/"
    | "\\"
    | "`"
    | "*"
    | "["
    | "]"
    | "("
    | ")"
    | "\""
    | ","
    | "{"
    | "}"
    | ":"
    | "."
    | "-"
    | "_"
    | "!"
    | "*"

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


def test_unordered_list():
    """Test various backquote content."""
    parse_result = parser.parse(
        dedent(
            """\
            - First item
            - Second item
            - Third item
            """
        )
    )
    tree = MarkdownTransformer().transform(parse_result)
    assert tree['document'] == ['First item', 'Second item', 'Third item']


def test_ordered_list():
    """Test nested backquote."""
    parse_result = parser.parse(
        dedent(
            """\

            1. First item
            2. Second item
            3. Third item

            """
        )
    )
    tree = MarkdownTransformer().transform(parse_result)
    print(tree)


def test_nested_list():
    """Test various backquote content."""
    parse_result = parser.parse(
        dedent(
            """\
            - First item
            - Second item
            - Third item
                - Indented item
                - Indented item
            - Fourth item
            """
        )
    )
    tree = MarkdownTransformer().transform(parse_result)
    print(tree)
