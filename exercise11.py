n1 = int(input("Me diga quantos metros de altura e largura tem uma parede que te direi a quantidade de litros que você irá precisar para pintá-la, comece com a altura: "))
n2 = int(input("Agora me diga a largura da parede: "))
m = n1*n2
t = m/2
print("Para pintar a sua parede de {} metros quadrados serão necessários {} litros de tinta".format(m, t))
