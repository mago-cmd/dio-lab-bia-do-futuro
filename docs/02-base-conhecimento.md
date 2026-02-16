# 📚 Base de Conhecimento da Mag

## Dados Utilizados

| Arquivo                     | Formato | Utilização na Mag                                      |
|------------------------------|---------|--------------------------------------------------------|
| `historico_atendimento.csv` | CSV     | Contextualizar interações anteriores                   |
| `perfil_investidor.json`    | JSON    | Personalizar recomendações conforme perfil do usuário  |
| `produtos_financeiros.json` | JSON    | Sugerir produtos adequados ao perfil                   |
| `transacoes.csv`            | CSV     | Analisar padrão de gastos do cliente                   |

---

## Adaptações nos Dados

- Os dados mockados foram expandidos para incluir:
  - **Perfis de investidor** (conservador, moderado, arrojado).
  - **Produtos financeiros simulados** (Tesouro Direto, CDB, LCI, fundos de investimento).
  - **Histórico de transações fictícias** para testes de análise de gastos.
- Estrutura simplificada para garantir **clareza nas respostas** e **boa performance**.  
- Observação: o tempo de resposta pode variar conforme o tamanho do contexto enviado ao modelo.

---

## Estratégia de Integração

### Como os dados são carregados?
- Os arquivos **JSON/CSV** são carregados no início da sessão pelo `app.py`.
- São armazenados em memória para consultas rápidas.
- A Mag acessa os dados dinamicamente conforme a interação do usuário.

### Como os dados são usados no prompt?
- O **System Prompt expandido** define regras de clareza, didática e transparência.  
- Dados específicos do usuário (perfil, histórico, transações) são consultados **dinamicamente** durante a conversa.  
- As respostas são formatadas de forma **educativa e contextualizada**, alinhadas às métricas de clareza e precisão.  

---

## Exemplo de Contexto Montado

### Perfis de Investidor:
- Conservador: foco em segurança e liquidez.  
- Moderado: equilíbrio entre segurança e rentabilidade.  
- Arrojado: busca de maior retorno aceitando riscos.  

### Produtos Financeiros:
- Tesouro Selic (baixo risco, liquidez diária).  
- CDB 12% a.a. (risco moderado, prazo 2 anos).  
- LCI 10% a.a. (isenta de IR, prazo 1 ano).  

### Transações Recentes:
- 01/02: Supermercado – R$ 450  
- 03/02: Streaming – R$ 55  
- 05/02: Farmácia – R$ 120  

### Histórico de Atendimento:
- 10/02 [Usuário]: “Quais foram meus gastos em fevereiro?” → “Total de R$ 3.435,00, maior impacto em entretenimento.”  

---

## Relação com Métricas

- **Precisão das respostas**: dados validados e estruturados em JSON/CSV.  
- **Clareza**: linguagem acessível e didática, sem jargão técnico.  
- **Tempo de resposta**: arquivos leves, mas pode variar conforme o contexto enviado.  
- **Engajamento**: simulações e exemplos práticos estimulam interação.  
- **Retenção de contexto**: histórico de transações e perfil do investidor mantidos durante a sessão.  
