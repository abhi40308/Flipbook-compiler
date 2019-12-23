from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Image
        self.lexer.add('IMAGE', r'[^\s]+(\.(?i)(jpg|png|gif|bmp))')
        # Position
        self.lexer.add('POSITION', r'position')
        # Scale
        self.lexer.add('SCALE', r'scale')
        # Move
        self.lexer.add('MOVE', r'move')
        # Dimensions
        self.lexer.add('DIMENSIONS', r'dimensions')
        # Total
        self.lexer.add('TOTAL', r'total')
        # Print
        self.lexer.add('PRINT', r'print')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Comma separator
        self.lexer.add('COMMA', r'\,')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()