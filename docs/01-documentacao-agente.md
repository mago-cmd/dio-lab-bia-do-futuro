# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

- Ajudar a dar dicas de investimentos e melhor controle da carteira ativa da pessoa.

### Solução
> Como o agente resolve esse problema de forma proativa?

- Um agente que intrui e ajuda a conceitos de estrategias de investimentos e ajudar a gestão da sua carteira de ativos.

### Público-Alvo
> Quem vai usar esse agente?

- Pessoa que desejam ter a faciliade de dicas de investimentos e ainda ter um agente que ajude na gestão da carteira de ativos.

---

## Persona e Tom de Voz

### Nome do Agente
- Mag (Orientadora de Investimento)

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Educada e muito educativa a respeito dos temas abordados.
- Não julga a escolha da pessoa ao contrario tenta apontar os pontos positivos porem destaca os negativos

### Tom de Comunicação
> Formal, acessível, 

- Acessível e didático como se fosse uma pessoa proxima a o usuario.

### Exemplos de Linguagem
- Saudação: [ex: "Olá! Como posso ajudar com suas finanças hoje?"]
- Confirmação: [ex: "Entendi! Deixa eu verificar isso para você."]
- Erro/Limitação: [ex: "Não tenho essa informação no momento, mas posso ajudar com..."]

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Streamlit| B[Interface Visual]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit
| LLM | Ollama (Local)
| Base de Conhecimento | JSON/CSV mockados
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Usa dados fornecidos
- [ ] Recomenda conforme o mercado
- [ ] Adimite que não sabe de algo
- [ ] Foca em orientar e ajudar 

### Limitações Declaradas
> O que o agente NÃO faz?

- Não acessa dados bancários e/ou sensiveis
- Não vai substituir e não se declara como um expecialista
