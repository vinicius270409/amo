import streamlit as st

# Configuração da página para ficar bonitinha
st.set_page_config(page_title="Para o meu amor", page_icon="❤️")

# Título principal
st.title("Para a namorada mais linda do mundo! ")

# Pergunta o nome dela para personalizar a mensagem
nome = st.text_input('Digite seu nome aqui:')

if nome:
    st.write(f"### Olá, {nome}! ❤️")
    st.write("Eu criei esse site em Python só para te dizer o quanto você é especial para mim.")
    
    # Botão surpresa
    if st.button("Clique aqui para uma surpresa"):
        st.balloons() # Isso faz voar balões na tela do celular dela!
        st.success("EU TE AMO MUITO! Você é o amor da minha vida! ")
        
        # Código da idade que você já tinha feito, integrado de forma fofa
        st.write("---")
        idade = st.text_input('Me diz sua idade atual ai:')
        
        if idade:
            ano = 2026 - int(idade)
            st.write(f"Sabia que o mundo ficou muito mais bonito em **{ano}**? Que foi o ano que você nasceuuu")
