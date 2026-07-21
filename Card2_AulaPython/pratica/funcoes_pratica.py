class Aluno:
    #coloca os valores para o objeto na classe
    def __init__(self, nome, nota_inicial=0.0):
        self.nome = nome
        self.nota = float(nota_inicial)

    #função inbutida na classe
    def atualizar_nota(self, nova_nota):
        self.nota = float(nova_nota)

    # função usando *args e **kwargs para empacotamento
    def registrar_observacoes(self, *tags, **detalhes):
        """
        *args recebe tags adicionais como Tupla
        **kwargs recebe detalhes como Dicionário
        """
        print(f"Tags do aluno {self.nome}: {tags}")
        print(f"Detalhes adicionais: {detalhes}")