from lexer import Lexer

text_input = """
range (01,10) total (40) baby.jpg position (0,0) scale (120,1,10) move (110,1,10)
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token)