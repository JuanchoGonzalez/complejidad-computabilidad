from maqTuring import MaqTuring

def palindromo(cinta):
    estados = ['q0' , 'qa1', 'qb1', 'qa2', 'qb2', 'q3', 'q_accept']
    transiciones = {
        ('q0', 'a'): ('qa1', 'x', 'R'),
        ('q0', 'b'): ('qb1', 'x', 'R'),
        
        ('q0', 'x'): ('q0', 'x', 'R'),
        ('q0', '#'): ('q0', '#', 'R'),
        ('q0', '⊔'): ('q_accept', '⊔', 'R'),
        
        ('qa1', 'a'): ('qa1', 'a', 'R'),
        ('qa1', 'b'): ('qa1', 'b', 'R'),
        ('qa1', '#'): ('qa1', '#', 'R'),
        ('qa1', 'x'): ('qa1', 'x', 'R'),
        ('qa1', '⊔'): ('qa2', '⊔', 'L'),
        
        ('qb1', 'b'): ('qb1', 'b', 'R'),
        ('qb1', 'a'): ('qb1', 'a', 'R'),
        ('qb1', '#'): ('qb1', '#', 'R'),
        ('qb1', 'x'): ('qb1', 'x', 'R'),
        ('qb1', '⊔'): ('qb2', '⊔', 'L'),

        ('qa2', 'a'): ('q3', 'x', 'L'),
        ('qa2', 'x'): ('qa2', 'x', 'L'),
        ('qa2', '#'): ('qa2', '#', 'L'),
        ('qa2', '⊔'): ('q_accept', '⊔', 'R'),

        ('qb2', 'b'): ('q3', 'x', 'L'),
        ('qb2', 'x'): ('qb2', 'x', 'L'),
        ('qb2', '#'): ('qb2', '#', 'L'),
        ('qb2', '⊔'): ('q_accept', '⊔', 'R'),
        
        ('q3', 'a'): ('q3', 'a', 'L'),
        ('q3', 'b'): ('q3', 'b', 'L'),     
        ('q3', '#'): ('q3', '#', 'L'),
        ('q3', 'x'): ('q3', 'x', 'L'),
        ('q3', '⊔'): ('q0', '⊔', 'R'),

    }
    
    return MaqTuring(cinta, ["a","b","#"], ["a","b","⊔","x"], estados, transiciones)


maquina = palindromo("ba#aab")

print(f"cinta antes de consumir la cadena: {maquina.cinta}")

maquina.correr_cinta()

print(f"cinta después de consumir la cadena: {maquina.cinta}")
