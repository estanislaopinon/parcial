# Se recuperó la bitácora de la nave del cazarrecompensas Boba Fett, la
# cual se almacenaban en una pila en cada misión de caza que
# emprendió (con la siguiente información planeta visitado, a quien
# capturado, costo de la recompensa), resolver las siguientes
# actividades:
# a. Mostrar los planetas visitados en el orden hizo las misiones.
# b. Determinar cuántos créditos galácticos recaudo en total.
# c. Determinar el número de la misión en que capturo a Han Solo
# y en que planeta fue, suponga que dicha misión está cargada.

from pila import Pila

bitacora = Pila()
bitacora_aux = Pila()

class Registro():
    def __init__(self, planeta, capturado, recompensa):
        self.planeta = planeta
        self.capturado = capturado
        self.recompensa = recompensa

    def __str__(self):
        return f'{self.planeta} - {self.capturado} - {self.recompensa}'


def carga_pila():
    bitacora.push(Registro('Tatooine', 'Han Solo', '100.000 creditos'))
    bitacora.push(Registro('Coruscant', 'Greedo', '50.000 creditos'))
    bitacora.push(Registro('Endor', 'Wicket W.Warrick', '25.000 creditos'))
    bitacora.push(Registro('Hoth', 'General Veers', '75.000 creditos'))
    bitacora.push(Registro('Bespin', 'Lando Calrissian', '150.000 creditos'))


carga_pila()

def planetas_visitados(bitacora):
    bitacora_aux=Pila()
    planetas_visitados=[]
    while bitacora.size()>=:
        mision=bitacora.pop()
        planetas_visitados.push(mision[0])
        bitacora_aux.push(mision)
    while bitacora_aux.size()>0:
        bitacora.push(bitacora_aux.pop())
    
    return planetas_visitados

def total_creditos(bitacora):
    bitacora_aux=Pila()
    creditos_total=0
    while bitacora.size()>0:
        valor= bitacora.pop()
        creditos_total+= valor[2]
        bitacora_aux.push(valor)
    while bitacora_aux.size()>0:
        bitacora.push(bitacora_aux.pop())
    
    return total_creditos

