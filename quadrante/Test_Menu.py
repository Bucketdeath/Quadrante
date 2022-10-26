from Cordenadas import Cordenadas
from Menu import Menu



def test_menu_cordenada_valida():

    #Arrange
    cordenadaX = 0
    cordenadaY = 0
    
    cordenadas = Cordenadas(cordenadaX, cordenadaY)
    valida = Menu(cordenadas)
    
    #Act
    resultado= valida.cordenada_valida(cordenadas)
    
    #Assert
    assert resultado == False


def test_menu_cordenada_valida2():
    #Arrange
    cordenadaX = 2
    cordenadaY = 4

    cordenadas = Cordenadas(cordenadaX, cordenadaY)
    valida = Menu(cordenadas)

    #Act
    resultado = valida.cordenada_valida(cordenadas)

    #Assert
    assert resultado == True



