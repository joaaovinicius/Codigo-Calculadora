📘 Calculadora – Projeto com Testes Automatizados

👨‍💻 Autores:

João Vinicius – RA 006533

Eduarda Helena – RA 006687

Rodrigo Assis – RA 006606

🧠 Sobre o Projeto
Esta é uma calculadora completa desenvolvida para demonstrar boas práticas de desenvolvimento, testes e automação.
O projeto inclui operações matemáticas, interface web funcional e uma pipeline CI/CD com GitHub Actions e Codecov.

✨ Funcionalidades

➕ Soma

➖ Subtração

✖️ Multiplicação

➗ Divisão

🔼 Potência

🖥️ Interface Web simples e intuitiva

🧪 Testes Unitários

🔗 Testes de Integração

🌐 Testes End-to-End (E2E)

🤖 Pipeline CI/CD

📊 Análise de cobertura com Codecov

🎯 Meta: +90% de cobertura

🛠️ Tecnologias Utilizadas

🐍 Backend (Python)

Python 3.12

Pytest

Pytest-Cov

Playwright

🌐 Frontend

HTML

CSS

JavaScript

⚙️ DevOps

GitHub Actions

Codecov

🧪 Testes Implementados

🔹 Testes Unitários
Local: calculator/tests/unit/
Validam funções isoladas.

🔹 Testes de Integração
Local: calculator/tests/integration/
Validam a interação entre módulos.

🔹 Testes End-to-End (E2E)
Local: calculator/tests/e2e/
Simulam o uso real da calculadora no navegador.

🚀 CI/CD – GitHub Actions
O pipeline executa automaticamente a cada push ou pull request:

1️⃣ Instala dependências
2️⃣ Executa os testes
3️⃣ Gera o relatório de cobertura
4️⃣ Envia dados ao Codecov

Workflow: .github/workflows/ci.yml

📈 Codecov
Usado para monitorar a cobertura dos testes.

Badge (será exibido após sincronizar):
![coverage](https://codecov.io/gh/joaaovinicius/Codigo-Calculadora/branch/main/graph/badge.svg)

📁 Estrutura do Projeto

Codigo-Calculadora
├── calculator/
│ ├── calculator.py
│ ├── frontend/
│ ├── tests/
│ │ ├── unit/
│ │ ├── integration/
│ │ └── e2e/
├── requirements.txt
├── README.md
└── .github/workflows/ci.yml
🏆 Importância do Projeto
Este trabalho demonstra:

✔️ boas práticas de testes

✔️ uso de CI/CD

✔️ automação profissional

✔️ arquitetura limpa

✔️ versionamento no GitHub

✔️ relatório de qualidade com Codecov

📜 Licença
Projeto acadêmico – Libertas.
