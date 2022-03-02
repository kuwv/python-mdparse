# type: ignore
"""Test markdown backquote."""

from textwrap import dedent

from mkdown.transformer import MarkdownTransformer


def test_mixed_content_backquote(parser):
    """Test various backquote content."""
    parse_result = parser.parse(
        dedent(
            """\
            > #### The quarterly results look great!
            >
            > - Revenue was off the chart.
            > - Profits were higher than ever.
            >
            > *Everything* is going according to **plan**.
            """
        )
    )
    tree = MarkdownTransformer().transform(parse_result)
    print(tree)


def test_nested_backquote(parser):
    """Test nested backquote."""
    parse_result = parser.parse(
        dedent(
            """\
            > Dorothy followed her through many of the beautiful rooms in her
            > castle.
            >
            >> The Witch bade her clean the pots and kettles and sweep the
            >> floor and keep the fire fed with wood.
            """
        )
    )
    tree = MarkdownTransformer().transform(parse_result)
    print(tree)
