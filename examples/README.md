## 🤖 Mag – Orientadora de Investimento

## Assistente virtual para educação financeira e gestão de ativos, desenvolvida como parte do Bootcamp DIO Lab BIA do Futuro.

A Mag simula o comportamento de uma orientadora financeira, ajudando usuários a:

- Entender seus gastos.

- Receber recomendações de investimento.

- Desenvolver hábitos financeiros mais saudáveis.

## 📂 Estrutura do Projeto

```DIO-LAB-BIA-DO-FUTURO-MAIN/
│
├── data/          # Dados mockados (JSON/CSV)
├── docs/          # Documentação detalhada (agente, base, prompts, métricas, pitch)
├── examples/      # Exemplos de interações
├── src/           # Código principal da aplicação
│   └── app.py
└── README.md      # Este arquivo
```

## 🚀 Quickstart (Instalação Rápida)
- Clone o repositório
- git clone https://github.com/seu-usuario/DIO-LAB-BIA-DO-FUTURO-MAIN.git
- cd DIO-LAB-BIA-DO-FUTURO-MAIN

## 2. Instale as dependências
- pip install -r requirements.txt

## 3. Configure sua chave de API
- export GOOGLE_API_KEY="sua_chave_aqui"

## No Windows (PowerShell):

- setx GOOGLE_API_KEY "sua_chave_aqui"

4. Execute a aplicação
streamlit run src/app.py

## 📊 Dados Mockados

 A Mag utiliza dados fictícios para simulações:

- perfil_investidor.json → Perfil do cliente (conservador, moderado, arrojado)

- produtos_financeiros.json → Produtos disponíveis para recomendação

- transacoes.csv → Histórico de gastos mensais

- historico_atendimento.csv → Registro de interações anteriores

## 📖 Documentação

Toda a documentação está organizada na pasta docs/:

- 01-documentacao-agente.md → Descrição da Mag.

- 02-base-conhecimento.md → Estrutura da base de dados.

- 03-prompts.md → System prompt e exemplos de interação.

- 04-metricas.md → Avaliação e métricas de qualidade.

- 05-pitch.md → Roteiro para apresentação (Pitch).

## 🧪 Testes Realizados

## Durante os testes, a Mag demonstrou capacidade de:

- 📌 Resumir gastos mensais.

- Exemplo: Fevereiro = R$ 3.435,00, com destaque para viagens (35%).

- 💡 Sugerir economia.

- Redução de gastos com restaurantes e melhor planejamento de viagens.

## 📈 Recomendar investimentos

- Aplicação mensal de R$ 500 em Tesouro Selic e LCI, alinhado ao perfil conservador.

- 📊 Simular crescimento de carteira ao longo do tempo.

## ✅ Checklist dos Testes

 - Problema claramente definido.

 - Interações realizadas com base nos dados mockados.

 - Respostas claras e contextualizadas.

 - Recomendações alinhadas ao perfil do usuário.

 - Simulações apresentadas de forma prática.

📄 Veja o PDF com as interações: [PDF](https://drive.google.com/file/d/19fK39jS-zmGcT-dK2YQSM3C8eunJmITy/view?usp=sharing)

## 🎯 Objetivo do Projeto

- A Mag foi criada para:

- Explicar produtos financeiros em linguagem simples.

- Simular investimentos e analisar gastos.

- Reforçar hábitos positivos de educação financeira.

- Servir como protótipo de agente de IA generativa aplicado a finanças.

## 📹 Pitch

- 🎥 Assista ao Pitch no [YouTube](https://www.youtube.com/watch?v=XwixbT7c7uc)
- O pitch foi baseado em interações reais registradas em [PDF](https://drive.google.com/file/d/19fK39jS-zmGcT-dK2YQSM3C8eunJmITy/view?usp=sharing)

## 🛠️ Tecnologias Utilizadas

- Python

- Streamlit

## API de IA Generativa (Google Gemini)

- JSON / CSV para dados mockados

## 📌 Status do Projeto

- ✅ Projeto funcional com dados mockados.
- 📚 Documentação completa para o Bootcamp.
- 🚀 Em evolução para futuras integrações com dados reais.
