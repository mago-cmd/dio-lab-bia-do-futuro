import streamlit as st
import json
import pandas as pd
import os
from google import genai

# ============================
# Configuração da API Gemini
# ============================
# Recomendo salvar sua chave em variável de ambiente (GOOGLE_API_KEY)
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# ============================
# Funções utilitárias
# ============================

def carregar_dados():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")

    perfil = json.load(open(os.path.join(data_dir, "perfil_investidor.json"), "r", encoding="utf-8"))
    produtos = json.load(open(os.path.join(data_dir, "produtos_financeiros.json"), "r", encoding="utf-8"))
    transacoes = pd.read_csv(os.path.join(data_dir, "transacoes.csv"))
    historico = pd.read_csv(os.path.join(data_dir, "historico_atendimento.csv"))
    return perfil, produtos, transacoes, historico

def montar_contexto(perfil, produtos, transacoes, historico):
    contexto = "### Contexto da Base de Conhecimento\n\n"
    contexto += "Perfis de Investidor:\n"
    for p in perfil:
        contexto += f"- {p['tipo']}: {p['descricao']} (Horizonte: {p.get('horizonte_investimento','N/A')})\n"

    contexto += "\nProdutos Financeiros:\n"
    for prod in produtos:
        contexto += f"- {prod['nome']} ({prod['tipo']}, risco {prod['risco']}, liquidez {prod['liquidez']})\n"

    contexto += "\nTransações Recentes:\n"
    for _, row in transacoes.iterrows():
        contexto += f"- {row['data']}: {row['descricao']} ({row['categoria']}) - R$ {row['valor']}\n"

    contexto += "\nHistórico de Atendimento:\n"
    for _, row in historico.iterrows():
        contexto += f"- {row['data']} [{row['usuario']}]: {row['pergunta']} -> {row['resposta']}\n"

    return contexto

# ============================
# System Prompt Expandido
# ============================

SYSTEM_PROMPT = """
Você é um agente financeiro inteligente especializado em educação financeira e gestão de carteira de ativos.
Seu objetivo é orientar usuários de forma clara e didática, ajudando em simulações financeiras e explicações de produtos.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos (JSON/CSV mockados).
2. Nunca invente informações financeiras ou dados de mercado.
3. Se não souber algo, admita e ofereça alternativas ou conceitos gerais.
4. Use linguagem acessível e empática, evitando jargões técnicos.
5. Explique vantagens e riscos de forma equilibrada.
6. Não recomende produtos específicos de instituições financeiras.
7. Respeite o perfil do investidor (conservador, moderado, arrojado).
8. Mantenha consistência e clareza nas respostas.
9. Utilize exemplos práticos e simulações para aumentar o engajamento.
10. Mantenha transparência sobre limitações (não substitui consultoria profissional).
11. Quando o usuário disser "Mag" ou se referir a você pelo nome, responda de forma breve e simpática, sem repetir sua apresentação completa.
"""

# ============================
# Interface Streamlit
# ============================

def main():
    st.set_page_config(page_title="Mag - Orientadora de Investimento", page_icon="🤖")
    st.title("🤖 Mag - Orientadora de Investimento")
    st.write("Assistente virtual para educação financeira e gestão de ativos.")

    perfil, produtos, transacoes, historico = carregar_dados()
    contexto = montar_contexto(perfil, produtos, transacoes, historico)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.chat_input("Digite sua pergunta:")

    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        try:
            # Chamada à API Gemini usando google.genai
            response = client.models.generate_content(
                model="models/gemini-flash-latest",  # sempre pega a versão mais atual
                contents=SYSTEM_PROMPT + "\n\n" + contexto + "\n\nUsuário: " + user_input
            )

            st.session_state.chat_history.append(
                {"role": "assistant", "content": response.text}
            )
        except Exception as e:
            st.error(f"Erro ao gerar resposta: {e}")

    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.chat_message("user").text(msg["content"])  # texto puro
        else:
            st.chat_message("assistant").text(msg["content"])  # texto puro

if __name__ == "__main__":
    main()
