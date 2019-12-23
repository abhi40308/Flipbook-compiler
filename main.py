from lexer import Lexer
from parser import Parser

text_input = """
print ( total (10) position(0,0) scale (5,1,10) move (10,5,1,10) images.png dimensions (50,50) )
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()