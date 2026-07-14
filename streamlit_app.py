import streamlit as st

# Configuração da página para ficar bonitinha
st.set_page_config(page_title="Para o meu amor", page_icon="❤️")

# Título principal
st.title("Para a namorada mais linda do mundo! ")

# Pergunta o nome dela para personalizar a mensagem
nome = st.text_input('Digite seu nome aqui:')

if nome:
    st.write(f"### Olá, {nome}! ❤️")
    
    # Pergunta a idade logo abaixo do nome
    idade = st.text_input('Me diz sua idade atual ai:')
    
    # Se ela colocar a idade, calcula o ano
    if idade:
        ano = 2026 - int(idade)
        st.write(f"Sabia que o mundo ficou muito mais bonito em **{ano}**? Que foi o ano que você nasceuuu")
        st.write("---")
        
        # O botão da surpresa aparece no final como o grande prêmio!
        if st.button("Clique aqui para uma surpresa"):
            st.balloons() # Isso faz voar balões na tela do celular dela!
            st.success("EU TE AMO MUITO! Você é o amor da minha vida! ")
