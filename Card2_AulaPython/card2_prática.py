# Importando do nosso pacote e módulos
from pratica.funcoes_pratica import Aluno
from pratica.utilitarios_pratica import (
    aplicar_bonus_todas_notas,
    calcular_media_turma,
    filtrar_aprovados,
    arredondar
)

def menu_principal():
    # Dicionário para armazenar os alunos (chave: nome, valor: objeto Aluno)
    banco_alunos = {
        'João': Aluno('João', 8.5),
        'Maria': Aluno('Maria', 6.0),
        'Pedro': Aluno('Pedro', 4.5)
    }

    opcao = -1

    # Estrutura de Repetição While + Operador Relacional (!=)
    while opcao != 0:
        print("\n" + "="*40) # repete o texto "=" 40 vezes
        print('Bem-vindo ao sistema de gerenciamento de notas!')
        print('1 - Visualizar alunos e notas')
        print('2 - Visualizar estado dos alunos (Aprovados/Reprovados)')
        print('3 - Modificar nota de um aluno')
        print('4 - Aplicar bônus a TODOS os alunos (Map/Lambda)')
        print('5 - Ver média geral da turma (Reduce)')
        print('0 - Sair')
        print("="*40)
        # pega o valor de entrada do usuário
        opcao = int(input('Digite a ação desejada: '))

        # Estrutura Condicional If / Elif / Else
        if opcao == 1:
            print("\n--- Lista de Alunos ---")
            for nome, aluno in banco_alunos.items(): # Laço For
                print(f"Aluno: {nome} | Nota: {aluno.nota}")

        elif opcao == 2:
            print("\n--- Situação dos Alunos ---")
            # Extraindo apenas as notas com dicionário
            notas_dict = {nome: a.nota for nome, a in banco_alunos.items()}
            aprovados = filtrar_aprovados(notas_dict)

            for nome, aluno in banco_alunos.items():
                # Operador Ternário
                status = "Aprovado" if nome in aprovados else "Recuperação/Reprovado"
                print(f"{nome}: {status} (Nota: {aluno.nota})")

        elif opcao == 3:
            nome = input("Digite o nome do aluno: ")
            if nome in banco_alunos:
                nova_nota = float(input(f"Digite a nova nota para {nome}: "))
                banco_alunos[nome].atualizar_nota(nova_nota)
                print("Nota atualizada com sucesso!")
            else:
                print("Aluno não encontrado.")

        elif opcao == 4:
            bonus = float(input("Digite o bônus a adicionar para todos (ex: 0.5): "))
            notas_dict = {nome: a.nota for nome, a in banco_alunos.items()}
            
            # Usando a função com MAP
            novas_notas = aplicar_bonus_todas_notas(notas_dict, bonus)
            
            # Atualizando os objetos
            for nome, nova_n in novas_notas.items():
                banco_alunos[nome].nota = nova_n
            print("Bônus aplicado a todos os alunos!")

        elif opcao == 5:
            lista_de_notas = [a.nota for a in banco_alunos.values()]
            # Usando REDUCE para calcular a média
            media = calcular_media_turma(lista_de_notas)
            print(f"\nA média geral da turma é: {media}")

        elif opcao == 0:
            print("Saindo do sistema... Até logo!")
            
        else:
            print("Opção inválida! Tente novamente.")

# Garantindo que o arquivo só execute a função se for o módulo principal
if __name__ == "__main__":
    menu_principal()