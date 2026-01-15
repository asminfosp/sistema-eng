from flask import Blueprint, render_template, request, redirect, url_for
from .models import Tarefa

main = Blueprint("main", __name__)

tarefas = []

@main.route("/")
def home():
    return render_template("index.html", tarefas=tarefas)

# ROTA DO FORMULÁRIO
@main.route("/add", methods=["POST"])
def add():
    titulo = request.form["titulo"]
    descricao = request.form["descricao"]
    prioridade = request.form["prioridade"]

    tarefas.append(Tarefa(titulo, descricao, "To Do", prioridade))
    return redirect(url_for("main.home"))

# EDITAR
@main.route("/edit/<int:id>")
def edit(id):
    tarefa = next(t for t in tarefas if t.id == id)
    return render_template("edit.html", tarefa=tarefa)

@main.route("/update/<int:id>", methods=["POST"])
def update(id):
    tarefa = next(t for t in tarefas if t.id == id)

    tarefa.titulo = request.form["titulo"]
    tarefa.descricao = request.form["descricao"]
    tarefa.status = request.form["status"]
    tarefa.prioridade = request.form["prioridade"]

    return redirect(url_for("main.home"))

# EXCLUIR
@main.route("/delete/<int:id>")
def delete(id):
    global tarefas
    tarefas = [t for t in tarefas if t.id != id]
    return redirect(url_for("main.home"))

# MUDAR STATUS
@main.route("/status/<int:id>/<status>")
def mudar_status(id, status):
    for t in tarefas:
        if t.id == id:
            t.status = status
    return redirect(url_for("main.home"))


@main.route("/kanban")
def kanban():
    # Reaproveita a mesma tela com o quadro Kanban
    return render_template("index.html", tarefas=tarefas)
