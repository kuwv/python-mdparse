"""Transform markdown to another format."""

import logging
from typing import Any, Dict, List

from lark import Transformer
from lark.indenter import Indenter

logging.getLogger(__name__).addHandler(logging.NullHandler())


class MarkdownTransformer(Transformer):
    """Transform markdown parse tree."""

    TEXT = str
    INT = int
    center = (lambda self, _: 'center')
    left = (lambda self, _: 'left')
    right = (lambda self, _: 'right')
    fill = (lambda self, _: 'fill')
    language = str

    # Table
    def table(self, rows: List[Any]) -> Dict[str, Any]:
        """Convert attribute to str."""
        table: Dict[str, Any] = {}
        for row in rows:
            table.update(**row)
        return {'table': table}

    def header(self, x) -> Dict[str, List[Any]]:
        """Convert attribute to list."""
        return {'header': list(x)}

    def alignment(self, x) -> Dict[str, List[Any]]:
        """Convert attribute to list."""
        return {'alignment': list(x)}

    def item(self, x) -> Dict[str, List[Any]]:
        """Convert attribute to list."""
        return {'rows': list(x)}

    def document(self, content) -> Dict[str, Any]:
        """Convvert content to dict."""
        return {'document': content[0]}

    def section(self, body):
        """Convert heading into string."""
        return {'sections': body}

    def heading1(self, header):
        """Convert heading into string."""
        return {'heading1': str(header[0])}

    def heading2(self, header):
        """Convert heading into string."""
        return {'heading2': str(header[0])}

    def heading3(self, header):
        """Convert heading into string."""
        return {'heading3': str(header[0])}

    def heading4(self, header):
        """Convert heading into string."""
        return {'heading4': str(header[0])}

    def heading5(self, header):
        """Convert heading into string."""
        return {'heading5': str(header[0])}

    def heading6(self, header):
        """Convert heading into string."""
        return {'heading6': str(header[0])}

    # Code block
    def code_block(self, content) -> str:
        """Convert content to list of strings."""
        return {'code_block': content}

    # Blockquote
    def blockquote(self, content) -> str:
        """Convert attribute to str."""
        return {'blockquote': content}

    # Lists
    def ordered_list(self, value) -> List:
        """Convert unordered list into set."""
        result = [{i: k} for i, k in zip(value[0::2], value[1::2])]
        return result

    def unordered_list(self, a: List[str]) -> List[str]:
        """Convert unordered list into set."""
        return list(a)


class TreeIndenter(Indenter):
    """Provide indenting."""

    NL_type: str = '_WS'
    OPEN_PAREN_types: List[str] = []
    CLOSE_PAREN_types: List[str] = []
    INDENT_type: str = '_INDENT'
    DEDENT_type: str = '_DEDENT'
    tab_len: int = 4
