from maqTuring import MaqTuring

def dosalan(cinta):
    estados = ['q0' , 'q1', 'q2', 'q3', 'q4', 'q_accept']
    transiciones = {
        ('q0', '0'): ('q1', '⊔', 'R'),
        
        ('q1', '⊔'): ('q_accept', '⊔', 'R'),
        ('q1', 'x'): ('q1', 'x', 'R'),
        ('q1', '0'): ('q2', 'x', 'R'),
        
        ('q2', '⊔'): ('q4', '⊔', 'L'),
        ('q2', 'x'): ('q2', 'x', 'R'),
        ('q2', '0'): ('q3', '0', 'R'),
        
        ('q3', 'x'): ('q3', 'x', 'R'),
        ('q3', '0'): ('q2', 'x', 'R'),
        
        ('q4', '⊔'): ('q1', '⊔', 'R'),
        ('q4', 'x'): ('q4', 'x', 'L'),
        ('q4', '0'): ('q4', '0', 'L'),
        
    }
    
    return MaqTuring(cinta, ["0"], ["0","⊔","x"], estados, transiciones)


maquina = dosalan("00000000")

print(f"cinta antes de consumir la cadena: {maquina.cinta}")

maquina.correr_cinta()

print(f"cinta después de consumir la cadena: {maquina.cinta}")
