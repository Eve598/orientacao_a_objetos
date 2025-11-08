class carro: 
    marca = "" 
    modelo = "" 
    ano = 0
    cor = "" 

    def buzinar(self):
        print("biiii biiii")

    def ligar(self):
        print("PHAM PHAM BRRRRRRRR....")

c1 = carro()
c1.marca = "Nissan"
c1.modelo = "nissa GT3"
c1.ano = 2006
c1.cor = "verde de ben10"

print("carro: ", c1.marca, "-", c1.modelo," ano: ", c1.ano, " cor: ", c1.cor)

c1.ligar()
c1.buzinar()