import streamlit as st

# Configuração da página - O primeiro passo do seu projeto
st.set_page_config(page_title="V-Vision VS", page_icon="✨")

# Título do seu app
st.title("V-Vision VS v0.1.0")
st.subheader("Bem-vindo ao meu motor de criação")

# Introdução pessoal
st.write("Projeto desenvolvido por Vânia Santos.")

# Caixa de entrada para o usuário
prompt = st.text_input("O que você quer criar hoje?")

if st.button("Gerar Vídeo"):
    if prompt:
        st.write(f"Processando seu pedido: {prompt}")
        st.info("O motor V-Vision VS está iniciando a conexão...")
    else:
        st.warning("Por favor, digite algo para criar.")

# Rodapé de longevidade
st.sidebar.markdown("---")
st.sidebar.write("V-Vision VS - Versão 0.1.0")
st.sidebar.write("Prosperidade e inovação constante.")
