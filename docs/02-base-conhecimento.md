# 📚 Base de Conhecimento

## Dados Utilizados

| Arquivo                     | Formato | Utilização no Agente                                   |
|------------------------------|---------|--------------------------------------------------------|
| `historico_atendimento.csv` | CSV     | Contextualizar interações anteriores                   |
| `perfil_investidor.json`    | JSON    | Personalizar recomendações conforme perfil do usuário  |
| `produtos_financeiros.json` | JSON    | Sugerir produtos adequados ao perfil                   |
| `transacoes.csv`            | CSV     | Analisar padrão de gastos do cliente                   |


---

## Adaptações nos Dados

- Os dados mockados foram expandidos para incluir:
  - **Perfis de investidor** (conservador, moderado, arrojado).
  - **Produtos financeiros simulados** (Tesouro Direto, CDB, fundos de investimento).
  - **Histórico de transações fictícias** para testes de análise de gastos.
- Estrutura simplificada para garantir **tempo de resposta rápido** e **clareza nas respostas**.

---

## Estratégia de Integração

### Como os dados são carregados?
- Os arquivos **JSON/CSV** são carregados no início da sessão.
- São armazenados em memória para consultas rápidas.
- O agente acessa os dados dinamicamente conforme a interação do usuário.

### Como os dados são usados no prompt?
- FAQs e conceitos básicos são incluídos no **system prompt** para dar contexto inicial.
- Dados específicos do usuário (perfil, histórico, transações) são consultados **dinamicamente** durante a conversa.
- As respostas são formatadas de forma **didática e contextualizada**, alinhadas às métricas de clareza e precisão.

---

## Exemplo de Contexto Montado

## Dados do Cliente:

Nome: João Silva

Perfil: Moderado

Saldo disponível: R$ 5.000

Últimas transações:

01/02: Supermercado - R$ 450

03/02: Streaming - R$ 55

05/02: Farmácia - R$ 120

Produtos sugeridos:

Tesouro Selic (baixo risco, liquidez diária)

CDB 12% a.a. (risco moderado, prazo 2 anos)


---

## Relação com Métricas

- **Precisão das respostas**: dados validados e estruturados em JSON/CSV.  
- **Clareza**: respostas curtas e didáticas, sem jargão técnico.  
- **Tempo de resposta**: arquivos leves, carregados em memória.  
- **Engajamento**: simulações e exemplos práticos estimulam interação.  
- **Retenção de contexto**: histórico de transações e perfil do investidor mantidos durante a sessão.  

