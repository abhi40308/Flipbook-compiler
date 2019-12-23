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

        @self.pg.production('expression : PRINT OPEN_PAREN TOTAL OPEN_PAREN expression CLOSE_PAREN POSITION OPEN_PAREN expression COMMA expression CLOSE_PAREN SCALE OPEN_PAREN expression COMMA expression COMMA expression CLOSE_PAREN MOVE OPEN_PAREN expression COMMA expression COMMA expression COMMA expression CLOSE_PAREN expression DIMENSIONS OPEN_PAREN expression COMMA expression CLOSE_PAREN CLOSE_PAREN')
        def expression(p): 
            total = p[4]
            pos_left = p[8]
            pos_right = p[10]
            percent_scale = p[14]
            scale_left = p[16]
            scale_right = p[18]
            percent_move_x = p[22]
            percent_move_y = p[24]
            move_left = p[26]
            move_right = p[28]
            image = p[30]
            height = p[33]
            width = p[35]
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