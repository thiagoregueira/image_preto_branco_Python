import streamlit as st
from PIL import Image


def transformar_em_preto_e_branco(imagem):
    imagem_preto_branco = imagem.convert("L")  # Converte para preto e branco
    return imagem_preto_branco


st.set_page_config(
    page_title="Imagem em Preto e Branco",
    initial_sidebar_state="collapsed",
    page_icon="📷",
)


st.markdown(
    "<h2 style='text-align: center;'> Transformador de Imagem Preto e Branco </h2>",
    unsafe_allow_html=True,
)

# Adiciona um campo para fazer upload da foto
st.container()
uploaded_file = st.file_uploader("Escolha uma imagem", type=["png", "jpg"])

if uploaded_file is not None:
    imagem = Image.open(uploaded_file)

    st.markdown(
        "<h3 style='text-align: center;'> Imagem Original e Resultado </h3>",
        unsafe_allow_html=True,
    )

    # Cria duas colunas
    col1, col2 = st.columns(2)

    # Na primeira coluna, mostra a imagem original
    col1.image(imagem, caption="Imagem Original", use_column_width=True)

    # Transforma a imagem em preto e branco
    imagem_preto_branco = transformar_em_preto_e_branco(imagem)

    # Na segunda coluna, mostra o resultado da foto transformada em preto e branco
    col2.image(
        imagem_preto_branco,
        caption="Imagem em Preto e Branco",
        use_column_width=True,
    )
