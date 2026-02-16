# 📊 Avaliação e Métricas da Mag – Orientadora de Investimento

Este documento descreve como avaliar a performance da **Mag**, assistente virtual de educação financeira, e apresenta resultados obtidos a partir das interações já realizadas.

---

## 1. Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** perguntas e respostas esperadas.  
2. **Feedback real:** pessoas testam a Mag e dão notas sobre clareza, assertividade e utilidade.

---

## 2. Métricas de Qualidade

| Métrica          | O que avalia                                   | Exemplo de teste | Resultado observado |
|------------------|-----------------------------------------------|------------------|---------------------|
| **Assertividade** | Se a Mag respondeu corretamente ao que foi perguntado. | Perguntar gastos de fevereiro. | ✅ Retornou R$ 3.435,00 conforme transações mockadas. |
| **Segurança**     | Se a Mag evitou inventar informações ou acessar dados sensíveis. | Pergunta fora do escopo (ex.: previsão do tempo). | ✅ Informou que só trata de finanças. |
| **Coerência**     | Se a resposta faz sentido para o perfil do cliente. | Usuário conservador pede recomendação. | ✅ Sugeriu Tesouro Selic e LCI, alinhado ao perfil conservador. |
| **Clareza**       | Se a linguagem foi acessível e didática. | Explicação sobre Tesouro Direto. | ✅ Explicou riscos em linguagem simples, sem jargões. |
| **Tempo de resposta** | Latência média entre pergunta e resposta. | Medição em testes. | ~30–50 segundos por interação. |
| **Engajamento**   | Se o usuário mantém a interação ativa. | Número de perguntas em uma sessão. | ✅ Sessão com 5+ interações contínuas. |
| **Retenção de contexto** | Se a Mag mantém coerência em diálogos longos. | Perguntar sobre investimentos após análise de gastos. | ✅ Conectou gastos altos em lazer com sugestão de economia e investimento. |

---

## 3. Exemplos de Cenários de Teste

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei em fevereiro?"  
- **Resposta esperada:** Valor baseado no `transacoes.csv`.  
- **Resultado:** ✅ Correto (R$ 3.435,00).  

### Teste 2: Recomendação de produto
- **Pergunta:** "Sou conservador, onde devo investir?"  
- **Resposta esperada:** Produtos compatíveis com perfil conservador.  
- **Resultado:** ✅ Correto (Tesouro Selic, LCI).  

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"  
- **Resposta esperada:** Mag informa que só trata de finanças.  
- **Resultado:** ✅ Correto.  

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"  
- **Resposta esperada:** Mag admite não ter essa informação.  
- **Resultado:** ✅ Correto.  

---

## 4. Resultados

**O que funcionou bem:**  
- Respostas assertivas e alinhadas ao perfil do investidor.  
- Clareza na explicação de produtos financeiros.  
- Boa retenção de contexto entre gastos e recomendações.  
- Engajamento alto (usuário manteve várias interações).  

**O que pode melhorar:**  
- Reduzir tempo de resposta em interações mais longas.  
- Tornar algumas simulações mais detalhadas (ex.: incluir impostos quando relevante).  
- Expandir variedade de exemplos práticos para diferentes perfis.  

---

## 5. Métricas Avançadas

- **Latência média:** 30-50 segundos por resposta.  
- **Consumo de tokens:** variável conforme tamanho do contexto (não monitorado em detalhe). 

