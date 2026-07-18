#!python3

class Contador:
    contador = 0 #atributo de classe


    def inst(self):
        return 'Estou bem!'


    def inc_maluco(self):
        self.contador += 1 #contador eh da classe ent ele cria um atributo do zero
        return self.contador



    @classmethod
    def inc(cls):
        cls.contador += 1
        return cls.contador
    
    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador
    

    @staticmethod
    def mais_um(n):
        return n + 1
    
c1 = Contador()

#print(Contador.inc)
#print(Contador.dec)

print(c1.inc())
print(c1.dec())

#Contador.inst <- inst precisa de uma instancia por nao ser um metodo de classe
print(Contador.mais_um(99))

print(c1.inst())