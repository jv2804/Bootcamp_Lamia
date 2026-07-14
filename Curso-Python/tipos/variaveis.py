# int
#a = 3

# float
#b = 4.4

#print(a + b)

#string(str)
#texto = 'Sua idade é... '

#idade = 23

#por idade ser int e texto ser str, a soma dá erro, para resolver, pode ser usado a função str(int var) para transformar em str.
#print(texto + str(idade))

#formata a mensagem, podendo ter partes que são texto e partes que podem ser interpretadas pela máquina({})
#print(f"{texto}{idade}")

#permite multiplicar textos
#print(3 * 'bom dia ')

#Constantes não existem no python nativamente, apenas convenções
PI = 3.14

# input pega o que o usuario escrever no terminar
raio = float(input('Informe o raio da circ? '))

# type informa o tipo de variavel que a variavel eh
#print(type(raio))

#pow funcao para potencializar
area = PI * pow(raio, 2)

print(f'A area do circ eh {area} m2.')