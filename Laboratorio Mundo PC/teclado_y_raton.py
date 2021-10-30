class DispositivoEntrada:

	def __init__(self, marca, entrada):

		self._entrada = entrada
		self._marca = marca


class Raton(DispositivoEntrada):

		contador_entradas = 0
def __init__(self, marca, entrada):
		Raton.contador_entradas +=1
		self._id_raton = Raton.contador_entradas
		super().__init__(marca, entrada)
	
def __str__(self):
	return f"ID{self._id_raton}, Marca: {self._marca}, Tipo de entrada: {self._entrada}"



class Teclado(DispositivoEntrada):
	contador_entradas = 0
	def __init__(self, marca, entrada):
		Raton.contador_entradas +=1
		self._id_teclado = Raton.contador_entradas
		super().__init__(marca, entrada)

	def __str__(self):
		return f"ID{self._id_teclado},Marca: {self._marca}, Tipo de entrada: {self._entrada}"

raton1 = Raton("HP", "USB",)
teclado1 = Teclado("teclado","Genius")

print(raton1)
print(teclado1)