"""
Modelo da entidade Tarefa.
Representa a estrutura principal do sistema.
"""

class Tarefa:
    contador = 1  # Gera IDs automáticos

    def __init__(self, titulo, descricao, status="To Do", prioridade="Média"):
        self.id = Tarefa.contador
        Tarefa.contador += 1

        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.prioridade = prioridade
