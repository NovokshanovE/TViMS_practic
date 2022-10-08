class mylogger(object):
	def __init__(self, fn='', tofile=False):
		self.fn = fn
		self.tofile = tofile
		return
	def printml(self, *args):
		toprint = ''
		for v in args:
			toprint = toprint + str(v) + ' '
		if self.tofile:
			f = open(self.fn, 'a')
			f.write(toprint + "\n")
			f.close()
		else: print(toprint)
		return