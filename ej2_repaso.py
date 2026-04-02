from maqTuring import MaqTuring

def mover_elemento_final(cinta):
    estados = ['q0' , 'qa1','qb1', 'q_accept']
    transiciones = {
        ('q0', 'a'): ('qa1', '⊔', 'R'),
        ('q0', 'b'): ('qb1', '⊔', 'R'),
        ('qa1', 'a'): ('qa1', 'a', 'R'),
        ('qa1', 'b'): ('qa1', 'b', 'R'),
        ('qb1', 'b'): ('qb1', 'b', 'R'),
        ('qb1', 'a'): ('qb1', 'a', 'R'),
        ('qa1', '⊔'): ('q_accept', 'a', 'R'),
        ('qb1', '⊔'): ('q_accept', 'b', 'R')
    }
    
    return MaqTuring(cinta, ["a","b"], ["a","b","⊔"], estados, transiciones)


maquina = mover_elemento_final("abab")

print(f"cinta antes de consumir la cadena: {maquina.cinta}")

maquina.correr_cinta()

print(f"cinta después de consumir la cadena: {maquina.cinta}")
