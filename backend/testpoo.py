class lapis:
    
    def __init__(self, cor, tipo):
        self.cor = cor
        self.tipo = tipo
    
    def escreve(self):
        return print(f"seu lapis do modelo {self.tipo} que tem a cor {self.cor} esta escrevendo")
    
    def apontar(self):
        return print(f"seu lapis esta sendo apontado")
    
    def altera(self, nova_cor):
        self.cor = nova_cor
        return print(f"seu lapis mudou de cor agora é {self.cor}")
    
    def __str__(self):
        return (f"seu lapis e do modelo {self.tipo} e tem a cor {self.cor}")

cor = input("qual a cor do seu lapis? ")
tipo = input("qual o tipo do seu lapis? ")
lapis1 = lapis(cor, tipo)

def muda_cor():
    while True:
        decisao = input("quer mudar de cor? reponda com sim ou nao").lower()
        if decisao == "sim":
             return input("qual cor voce vai colocar? ")
        elif decisao == "nao":
            print("a cor nao sera alterada")
            return None
        else:
            print("insira 'sim' ou 'nao'.") 


nova_cor = muda_cor()
if nova_cor:
    lapis1.altera(nova_cor)
print(lapis1)
#teste de commit