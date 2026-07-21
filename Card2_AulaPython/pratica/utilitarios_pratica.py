from functools import reduce

# constantes (convenção em maiúsculas)
MEDIA_APROVACAO = 7.0

# lambda para arredondar notas
arredondar = lambda nota: round(nota, 2)

def aplicar_bonus_todas_notas(alunos_dict, bonus):
    """
    Usa MAP e LAMBDA para aumentar a nota de todos os alunos.
    """
    # exemplo com map + lambda
    return {nome: round(nota + bonus, 2) for nome, nota in alunos_dict.items()}

def calcular_media_turma(lista_notas):
    """
    Usa REDUCE para somar todas as notas e calcular a média da turma.
    """
    if not lista_notas:
        return 0.0
    soma_total = reduce(lambda acumulador, nota: acumulador + nota, lista_notas)
    return round(soma_total / len(lista_notas), 2)

def filtrar_aprovados(alunos_dict):
    """
    Usa LIST COMPREHENSION e Operador Ternário para filtrar aprovados.
    """
    return [nome for nome, nota in alunos_dict.items() if nota >= MEDIA_APROVACAO]