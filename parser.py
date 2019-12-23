from rply import ParserGenerator
from ast import Number, Print, Image


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['PRINT', 'NUMBER', 'IMAGE', 'OPEN_PAREN', 'CLOSE_PAREN',
             'POSITION', 'TOTAL', 'COMMA', 'SCALE', 'MOVE', 'DIMENSIONS']
        )

    def parse(self):
        @self.pg.production('program : expression')
        def program(p):
            return (p[0])

        @self.pg.production('expression : PRINT OPEN_PAREN expression CLOSE_PAREN')
        def expression(p):
            return (p[2])

        @self.pg.production('expression : TOTAL OPEN_PAREN expression CLOSE_PAREN POSITION OPEN_PAREN expression COMMA expression CLOSE_PAREN SCALE OPEN_PAREN expression COMMA expression COMMA expression CLOSE_PAREN MOVE OPEN_PAREN expression COMMA expression COMMA expression COMMA expression CLOSE_PAREN expression DIMENSIONS OPEN_PAREN expression COMMA expression CLOSE_PAREN')
        def expression(p):
            total = p[2]
            pos_left = p[6]
            pos_right = p[8]
            percent_scale = p[12]
            scale_left = p[14]
            scale_right = p[16]
            percent_move_x = p[20]
            percent_move_y = p[22]
            move_left = p[24]
            move_right = p[26]
            image = p[28]
            height = p[31]
            width = p[33]
            return Print(total, pos_left, pos_right, percent_scale, scale_left, scale_right, percent_move_x, percent_move_y, move_left, move_right, image, height, width)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value).eval()

        @self.pg.production('expression : IMAGE')
        def image(p):
            return Image(p[0].value).eval()

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()