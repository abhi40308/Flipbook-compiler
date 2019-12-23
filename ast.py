from fpdf import FPDF
from rply.token import BaseBox
from PyPDF2 import PdfFileMerger
import os

class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class Total(BaseBox):
	def __init__(self, total):
		self.total = total


class Image(BaseBox):
	def __init__(self, image):
		self.image = image

	def eval(self):
		return (self.image)


class Position(BaseBox):
	def __init__(self, left_pos, right_pos):
		self.left_pos = left_pos
		self.right_pos = right_pos


class Dimensions(object):
	def __init__(self, height, width):
		self.height = height
		self.width = width
		

class Move(BaseBox):
	def __init__(self, percent_move_x, percent_move_y, move_left, move_right):
		self.percent_move_x = percent_move_x
		self.percent_move_y = percent_move_y
		self.move_left = move_left
		self.move_right = move_right


class Scale(BaseBox):
	def __init__(self, percent_scale, scale_left, scale_right):
		self.percent_scale = percent_scale
		self.scale_left = scale_left
		self.scale_right = scale_right


# generate pdf for the program
class Print(Total, Position, Image, Move, Scale):
	def __init__(self, total, left_pos, right_pos, percent_scale, scale_left, scale_right, percent_move_x, percent_move_y, move_left, move_right, image, height, width):
		Image.__init__(self, image)
		Position.__init__(self, left_pos, right_pos)
		Move.__init__(self, percent_move_x, percent_move_y, move_left, move_right)
		Scale.__init__(self, percent_scale, scale_left, scale_right)
		Total.__init__(self, total)
		Dimensions.__init__(self, height, width)
		
	def eval(self):
		image = self.image
		pos_x = self.left_pos
		pos_y = self.right_pos
		width = self.width
		height = self.height
		output_path = "flipbook.pdf"
		pdf_merger = PdfFileMerger()
		for i in range(1,self.total+1):
			if(i>= self.move_left and i <= self.move_right):
				pos_x = pos_x + self.percent_move_x
				pos_y = pos_y + self.percent_move_y
			if(i>= self.scale_left and i<=self.scale_right):
				width = width + self.percent_scale
				height = height + self.percent_scale
			pdf = FPDF()
			pdf.add_page()
			pdf.image(image, x = pos_x, y = pos_y, w = width, h = height, type = '', link = '')
			output = 'dummy_flipbook.pdf'
			pdf.output(output, 'F')
			pdf_merger.append(output)
			os.remove(output)
			print('done')
		with open(output_path, 'wb') as fileobj:
			pdf_merger.write(fileobj)

