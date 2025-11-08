class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def buzinar(self):
        print("Biiii biiii")

    def ligar(self):
        print("PHAM PHAM BRRRRRRRR.... o motor ligou!")

    def exibir_info(self):
        print(f"Carro: {self.marca} - {self.modelo} | Ano: {self.ano} | Cor: {self.cor}")


c1 = Carro("Nissan", "GT3", 2006, "Verde Ben 10")

c1.exibir_info()
c1.ligar()
c1.buzinar()
