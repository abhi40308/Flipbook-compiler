from lexer import Lexer
from parser import Parser
from PyPDF2 import PdfFileMerger
import os

# text_input = """
# print ( total (10) position(0,0) scale (5,1,10) move (10,5,1,10) images.png dimensions (50,50) )
# """


output_path = "flipbook.pdf"
pdf_merger = PdfFileMerger()


fname = "input.flip"
with open(fname) as f:
    text_input = f.read()
    lines = text_input.split('\n')
    for line in lines:
        if line == "":
            continue
        # print(line)
        lexer = Lexer().get_lexer()
        tokens = lexer.lex(line)

        pg = Parser()
        pg.parse()
        parser = pg.get_parser()
        parser.parse(tokens).eval()
        pdf_merger.append(output_path)
        os.remove(output_path)

with open(output_path, 'wb') as fileobj:
    pdf_merger.write(fileobj)