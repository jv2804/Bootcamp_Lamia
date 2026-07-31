#!python3

# Imprime a mensagem no terminal
print('Bem vindo!')

# importa um pacote/módulo para esse módulo
import pacote.sub.arquivo_aula

import pacote.sub.arquivo_aula

import tipos.variaveis_aula
# Faz a mesma coisa que o comando import tipos.variaveis mas coloca tambem o basicos
#from tipos import variaveis,basicos
import tipos.lista_aula
import tipos.tuplas_aula
import tipos.conjuntos_aula
import tipos.dicionario_aula

import operadores.unarios_aula
import operadores.aritmeticos_aula
import operadores.relacionais_aula
import operadores.atribuicao_aula
import operadores.logicos_aula
import operadores.ternario_aula

import controle.if_1_aula
import controle.if_2_aula
import controle.for_1_aula
import controle.while_1_aula
import controle.outros_exemplos_aula

from funcoes import basico_aula

basico_aula.saudacao()
basico_aula.saudacao('Maria')
basico_aula.saudacao('João', 33)
basico_aula.saudacao(idade = 33)

a = basico_aula.soma_e_multi(x=10, a=2, b=3)
b = basico_aula.soma_e_multi(x=20, a=3, b=7)
resultado = a + b
print(resultado)

from funcoes import args_aula

s = args_aula.soma(1, 2, 3, 7, 8, 9, 10)
print(s)

resultado = args_aula.resultado_final(nome='Pedro', nota=6.3)
print(resultado)

from funcoes import funcional_aula
import funcoes.map_reduce_aula
import funcoes.lambdas_aula
import funcoes.comprehension_aula

import oo.produto_aula
import oo.heranca_aula
import oo.membros_aula