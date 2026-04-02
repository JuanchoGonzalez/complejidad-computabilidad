from maqTuring import MaqTuring

def iguales(cinta):
    estados = ['q0' , 'qa1', 'qb1', 'qa2', 'qb2', 'qa3', 'qb3', 'qa4', 'qb4', 'q5' ,'q_accept']
    transiciones = {
        ('q0', 'a'): ('qa1', 'x', 'R'),
        ('q0', 'b'): ('qb1', 'x', 'R'),
        ('q0', '#'): ('q5', '#', 'R'),

        ('qa1', 'a'): ('qa1', 'a', 'R'),
        ('qb1', 'a'): ('qb1', 'a', 'R'),
        ('qa1', 'b'): ('qa1', 'b', 'R'),
        ('qb1', 'b'): ('qb1', 'b', 'R'),
        ('qa1', '#'): ('qa2', '#', 'R'),
        ('qb1', '#'): ('qb2', '#', 'R'),
        
        ('qa2', 'x'): ('qa2', 'x', 'R'),
        ('qb2', 'x'): ('qb2', 'x', 'R'),
        ('qa2', 'a'): ('qa3', 'x', 'L'),
        ('qb2', 'a'): ('qb3', 'x', 'L'),
        ('qa2', 'b'): ('qa3', 'x', 'L'),
        ('qb2', 'b'): ('qb3', 'x', 'L'),
        
        ('qa3', 'x'): ('qa3', 'x', 'L'),
        ('qb3', 'x'): ('qb3', 'x', 'L'),
        ('qa3', 'a'): ('qa3', 'x', 'L'),
        ('qb3', 'a'): ('qb3', 'x', 'L'),
        ('qa3', 'b'): ('qa3', 'x', 'L'),
        ('qb3', 'b'): ('qb3', 'x', 'L'),
        
        ('qa3', '#'): ('qa4', '#', 'L'),
        ('qb3', '#'): ('qb4', '#', 'L'),

        ('qa4', 'a'): ('qa4', 'a', 'L'),
        ('qb4', 'a'): ('qb4', 'a', 'L'),
        ('qa4', 'b'): ('qa4', 'b', 'L'),
        ('qb4', 'b'): ('qb4', 'b', 'L'),
        ('qa4', 'x'): ('q0', 'x', 'R'),
        ('qb4', 'x'): ('q0', 'x', 'R'),

        ('q5', 'x'): ('q5', 'x', 'R'),    
        ('q5', '⊔'): ('q_accept', '⊔', 'R')
        
    }
    
    return MaqTuring(cinta, ["a","b"], ["a","b","⊔","x"], estados, transiciones)


maquina = iguales("ab#ab")

print(f"cinta antes de consumir la cadena: {maquina.cinta}")

maquina.correr_cinta()

print(f"cinta después de consumir la cadena: {maquina.cinta}")
