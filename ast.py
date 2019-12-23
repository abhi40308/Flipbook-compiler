class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


# generate pdf for the program
class Print():
	


class Total():
	def _init_(self, num):
		self.num = num
	

class TernaryOp():
    def __init__(self, percent, left, right):
        self.percent = percent
        self.left = left
        self.right = right


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Position(BinaryOp):
	def eval(self):
		return self.left.eval() 


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())