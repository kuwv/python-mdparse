# type: ignore
"""Test markdown backquote."""

from textwrap import dedent
from mkdown.transformer import MarkdownTransformer


def test_headers(parser):
    """Test various backquote content."""
    parse_result = parser.parse(
        dedent(
            """\
            Header1
            =======

            # H1

            ## H2

            ### H3

            #### H4

            ##### H5

            ###### H6

            """
        )
    )
    tree = MarkdownTransformer().transform(parse_result)
    print(tree)
    assert tree['document']['sections'][0]['heading1'] == 'Header1'
    assert tree['document']['sections'][1]['sections'][0]['heading1'] == 'H1'
    assert tree['document']['sections'][1]['sections'][1]['sections'][0]['heading2'] == 'H2'
