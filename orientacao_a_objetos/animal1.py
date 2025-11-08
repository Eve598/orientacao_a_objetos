class Animal:
    nome = ""
    especie = ""
    idade = 0

    def som(self):
        print("Esse animal faz um som.")


a1 = Animal()
a1.nome = "Rex"
a1.especie = "Cachorro"
a1.idade = 5
def latir():
    print("Au au au!")
a1.som = latir

a2 = Animal()
a2.nome = "Mimi"
a2.especie = "Gato"
a2.idade = 3
def miar():
    print("Miau miau!")
a2.som = miar

a3 = Animal()
a3.nome = "Loló"
a3.especie = "Papagaio"
a3.idade = 2
def falar():
    print("Curupaco!")
a3.som = falar

a4 = Animal()
a4.nome = "Dudu"
a4.especie = "Pato"
a4.idade = 1
def grasnar():
    print("Quack quack!")
a4.som = grasnar

a5 = Animal()
a5.nome = "Mumu"
a5.especie = "Vaca"
a5.idade = 4
def mugir():
    print("Muuu!")
a5.som = mugir


print("Animal:", a1.nome, "-", a1.especie, "idade:", a1.idade)
a1.som()

print("Animal:", a2.nome, "-", a2.especie, "idade:", a2.idade)
a2.som()

print("Animal:", a3.nome, "-", a3.especie, "idade:", a3.idade)
a3.som()

print("Animal:", a4.nome, "-", a4.especie, "idade:", a4.idade)
a4.som()

print("Animal:", a5.nome, "-", a5.especie, "idade:", a5.idade)
a5.som()
