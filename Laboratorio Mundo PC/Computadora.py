from monitor import *
from teclado_y_raton import *

class Computadora:

	contador = 0
	def __init__(self, nombre, monitor, teclado, raton):
		Computadora.contador +=1
		self.id_compu = Computadora.contador
		self._nombre = nombre
		self._monitor = monitor
		self._teclado = teclado
		self._raton = raton


	def __str__(self):
		return f"""
		{self._nombre}: {self.id_compu}
		Monitor: {self._monitor}
		Teclado: {self._teclado}
		Raton: {self._raton}
		"""


teclado1 = Teclado("HP, USB")
raton1 = Raton("logitech", "USB")
Monitor1 = Monitor("HP", 15)
computadora1 = Computadora()

print(computadora1)