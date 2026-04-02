class MaqTuring:
    # constructor
    def __init__(self, cinta, alfabeto, alfabeto_r, estados, transiciones):
        self.cinta = {i: simbolo for i, simbolo in enumerate(cinta)}
        self.alfabeto = alfabeto
        self.alfabeto_r = alfabeto_r # alfabeto + ⊔
        self.estados = estados
        self.transiciones = transiciones
        self.estado_actual = estados[0]
        self.posicion_cabezal = 0
    
    # funcion de transicion, necesito estado y caracter que lee
    def movimiento(self):
        # si la posicion no existe esta afuera de los limites se devuelve ⊔
        caracter_leido = self.cinta.get(self.posicion_cabezal, '⊔')
        
        clave = (self.estado_actual, caracter_leido)
        
        # devuelve estado al que va, caracter que escribe y L/R
        if clave in self.transiciones:
            estado_nuevo, caracter_escrito, direccion = self.transiciones[clave]
            
            # chequeo de que el estado_nuevo este dentro de mis estados posibles, por si se escribe mal
            if estado_nuevo not in self.estados:
                print(f"estado {estado_nuevo} no esta definido en Q")
            
            # el caracter se escribe en la cinta
            self.cinta[self.posicion_cabezal] = caracter_escrito

            if direccion == 'L' : 
                self.posicion_cabezal -= 1 
            elif direccion == 'R' : 
                self.posicion_cabezal += 1
            
            # el estado nuevo pasa al actual 
            self.estado_actual = estado_nuevo
            return True
        else:
            print(f"no existe tal transicion")
            return False

    def correr_cinta(self):
        termino = False
        
        # mientras no acepte y ademas que la cinta tenga caracteres
        while (self.estado_actual != 'q_accept' and not(termino)):
            
            # si hay movimiento
            hay_transicion = self.movimiento()
            
            if not hay_transicion:
                termino = True
        
        
        if not termino:
            print(f"para la cadena {sorted(self.cinta.items())} acepto")
        else:
            print(f"para la cadena {sorted(self.cinta.items())} rechazo o no termino")
            print(f"se trabo en estado {self.estado_actual}")

