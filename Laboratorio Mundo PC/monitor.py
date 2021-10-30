class Monitor:
	contador_monitores = 0
	def __init__(self, marca, tamaño):
		Monitor.contador_monitores+=1
		self._id_monitor = Monitor.contador_monitores
		self._marca = marca
		self._tamaño = tamaño


	def __str__(self):
		return f" ID: {self._id_monitor}, MARCA: {self._marca}, TAMAÑO: {self._tamaño }"

Monitor1 = Monitor("LG", 22)

print(Monitor1)