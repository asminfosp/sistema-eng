# 📌 Sistema de Gerenciamento de Tarefas
Projeto acadêmico desenvolvido para a disciplina de Engenharia de Software, com o objetivo de aplicar conceitos de desenvolvimento ágil, modelagem, versionamento de código, testes automatizados e integração contínua.


# 🎯 Objetivo do Projeto
Desenvolver um sistema web de gerenciamento de tarefas, permitindo ao usuário organizar atividades por meio de um quadro Kanban, facilitando o acompanhamento do progresso e a priorização das tarefas.


# 🧭 Escopo Inicial
O escopo inicial do projeto contemplava:
Cadastro de tarefas
Visualização das tarefas em um quadro Kanban
Alteração do status das tarefas (A Fazer, Em Progresso e Completo)


# 🔄 Metodologia Ágil Utilizada
Foi adotada a metodologia Kanban, utilizando o recurso GitHub Projects, permitindo:
Visualização clara do fluxo de trabalho
Organização das atividades em colunas
Acompanhamento da evolução do projeto


# ⚙️ Funcionalidades Implementadas

Criação, edição e exclusão de tarefas (CRUD)
Visualização em quadro Kanban
Alteração de status das tarefas
Definição de prioridade (Baixa, Média e Alta)
Interface web responsiva
Organização do código em camadas


# 🚀 Mudança de Escopo
Durante o desenvolvimento, identificou-se a necessidade de uma melhor organização das tarefas.
Como mudança de escopo, foi adicionada a funcionalidade de prioridade das tarefas, permitindo classificá-las como Baixa, Média ou Alta.
Essa alteração foi registrada no Kanban e implementada no código, respeitando o fluxo de desenvolvimento ágil.


# 🧪 Qualidade e Testes Automatizados
O projeto conta com testes automatizados utilizando Pytest, validando:
Modelo de dados
Rotas principais da aplicação
Além disso, foi configurada integração contínua com GitHub Actions, garantindo que os testes sejam executados automaticamente a cada alteração no repositório.


# 🔁 Integração Contínua (CI)
A integração contínua foi implementada por meio do GitHub Actions, assegurando:
Execução automática dos testes
Validação da qualidade do código
Maior confiabilidade no processo de desenvolvimento


# 🛠️ Tecnologias Utilizadas
Python
Flask
HTML5 e CSS3
Pytest
GitHub Actions
GitHub Projects (Kanban)

# ▶️ Como Executar o Projeto Localmente

# Criar ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar o sistema
python run.py

▶️ Como Executar os Testes
pytest

# 📁 Estrutura do Projeto
sistema-eng/
├── src/
│   ├── app.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   └── static/
├── tests/
├── docs/
├── .github/workflows/
├── README.md
└── requirements.txt

# 📌 Conclusão

O projeto permitiu aplicar, de forma prática, os principais conceitos da Engenharia de Software, integrando desenvolvimento ágil, versionamento, testes automatizados e integração contínua, resultando em um sistema funcional e bem estruturado.