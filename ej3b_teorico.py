from maqTuring import MaqTuring

def cant_doble_ceros_a_unos(cinta):
    estados = ['q0' , 'q1c', 'q1u', 'q1cc', 'q1' , 'q2', 'q_accept']
    transiciones = {
        ('q0', '0'): ('q1c', 'x', 'R'),
        ('q0', '1'): ('q1u', 'x', 'R'),
        ('q0', 'x'): ('q0', 'x', 'R'),
        ('q0', '⊔'): ('q_accept', '⊔', 'R'),
        
        ('q1c', '0'): ('q1cc', 'x', 'R'),
        ('q1c', '1'): ('q1', 'x', 'R'),
        ('q1c', 'x'): ('q1c', 'x', 'R'),
        
        ('q1u', '0'): ('q1', 'x', 'R'),
        ('q1u', '1'): ('q1u', '1', 'R'),
        ('q1u', 'x'): ('q1u', 'x', 'R'),
        
        ('q1cc', '0'): ('q1cc', '0', 'R'),
        ('q1cc', '1'): ('q2', 'x', 'L'),
        ('q1cc', 'x'): ('q1cc', 'x', 'R'),
        
        ('q1', '0'): ('q2', 'x', 'L'),
        ('q1', '1'): ('q1', '1', 'R'),
        ('q1', 'x'): ('q1', 'x', 'R'),
        
        ('q2', '0'): ('q2', '0', 'L'),        
        ('q2', '1'): ('q2', '1', 'L'), 
        ('q2', 'x'): ('q2', 'x', 'L'),
        ('q2', '⊔'): ('q0', '⊔', 'R')
        
    }
    
    return MaqTuring(cinta, ["0","1"], ["0","1","⊔","x"], estados, transiciones)


maquina = cant_doble_ceros_a_unos("010101000")

print(f"cinta antes de consumir la cadena: {maquina.cinta}")

maquina.correr_cinta()

print(f"cinta después de consumir la cadena: {maquina.cinta}")
