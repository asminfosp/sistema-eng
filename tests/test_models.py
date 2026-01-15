import sys
import os

# Adiciona a pasta raiz do projeto no caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.models import Tarefa

def test_criacao_tarefa():
    t = Tarefa("Teste", "Descricao")
    assert t.titulo == "Teste"
    assert t.status == "To Do"
    assert t.prioridade == "Média"

def test_alteracao_status():
    t = Tarefa("Teste", "Desc")
    t.status = "Done"
    assert t.status == "Done"
