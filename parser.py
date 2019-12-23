from rply import ParserGenerator
from ast import Number, Print, Range, Position, Scale, Move, Image, Total


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'IMAGE', 'OPEN_PAREN', 'CLOSE_PAREN',
             'POSITION', 'SCALE', 'MOVE', 'RANGE', 'TOTAL', 'COMMA']
        )

    def parse(self):
        @self.pg.production('program : expression')
        def program(p):
            return Print(p[0])

        @self.pg.production('expression : RANGE OPEN_PAREN expression COMMA expression CLOSE_PAREN')
        def expression(p):
            left = p[2]
            right = p[4]
            return Range(left, right)

        @self.pg.production('expression : TOTAL OPEN_PAREN expression CLOSE_PAREN')
        def expression(p):
            num = p[2]
            return Total(num)

        @self.pg.production('expression : POSITION OPEN_PAREN expression COMMA expression CLOSE_PAREN')
        def expression(p):
            left = p[2]
            right = p[4]
            return Position(left, right)

        @self.pg.production('expression : SCALE OPEN_PAREN expression COMMA expression COMMA expression CLOSE_PAREN')
        def expression(p):
            percent = p[2]
            left = p[4]
            right = p[6]
            return Scale(percent, left, right)

        @self.pg.production('expression : MOVE OPEN_PAREN expression COMMA expression COMMA expression CLOSE_PAREN')
        def expression(p):
            percent = p[2]
            left = p[4]
            right = p[6]
            return Move(percent, left, right)

        @self.pg.production('expression : IMAGE')
        def number(p):
            return Image(p[0])

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()