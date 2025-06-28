class lapis:
    
    def __init__(self, cor, tipo):
        self.cor = cor
        self.tipo = tipo
    
    def escreve(self):
        return print(f"seu lapis do modelo {self.tipo} que tem a cor {self.cor} esta escrevendo")
    
    def apontar(self):
        return print(f"seu lapis esta sendo apontado")
    
    def muda_cor(self, nova_cor):
        self.cor = nova_cor
        return print(f"seu lapis mudou de cor agora é {nova_cor}")
    
    def __str__(self):
        return (f"seu lapis e do modelo{self.tipo} e tem a cor {self.cor}")

cor = input("qual a cor do seu lapis? ")
tipo = input("qual o tipo do seu lapis? ")

lapis1 = lapis(cor, tipo)
print(lapis1)
