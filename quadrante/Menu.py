from Cordenadas import Cordenadas

class Menu:
    
    def __init__(self, Cordenadas):
        pass

    def entradas_cordenadas(self):

        cordenadaX = int(input("Informe a Cordenada X: \n\n"))
        cordenadaY = int(input("Informe a Cordenada Y: \n\n"))
        self.cordenadas = Cordenadas(cordenadaX, cordenadaY)
        return self.cordenadas


    def cordenada_valida(self, cordenadas):

        if (cordenadas.cordenadaX == 0 or cordenadas.cordenadaY == 0):
            return False
        else:
            return True

    def mostrar_menu(self):

        self.entradas_cordenadas()
        return not self.cordenada_valida(self.cordenadas)
