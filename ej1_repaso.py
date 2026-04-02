from maqTuring import MaqTuring

def borrar_primer_elemento(cinta):
    estados = ['q0', 'q1', 'q_cargandoA', 'q_cargandoB' , 'q3' , 'q_accept']
    transiciones = {
        ('q0', 'a'): ('q1', '⊔', 'R'),
        ('q0', 'b'): ('q1', '⊔', 'R'),

        ('q1', 'a'): ('q_cargandoA', '⊔', 'L'),
        ('q1', 'b'): ('q_cargandoB', '⊔', 'L'),
        
        ('q1', '⊔'): ('q_accept', '⊔', 'L'),  # no hay mas elementos, termino

        # q_cargandoA: a en el hueco y vuelvo derecha
        ('q_cargandoA', '⊔'): ('q3', 'a', 'R'),

        # q_cargandoB: b en el hueco y vuelvo derecha
        ('q_cargandoB', '⊔'): ('q3', 'b', 'R'),
        
        # saltamos uno
        ('q3', '⊔'): ('q1','⊔','R')
    }
        
    return MaqTuring(cinta, ["a", "b"], ["a","b","⊔"], estados, transiciones)

maquina = borrar_primer_elemento("aba")

print(f"cinta antes de consumir la cadena: {maquina.cinta}")

maquina.correr_cinta()

print(f"cinta después de consumir la cadena: {maquina.cinta}")
