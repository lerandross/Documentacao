import streamlit as st
def main():
    caminho_do_arquivo = 'README.md'
    # Abrir o arquivo em modo de leitura
    with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:
        # Ler o conteúdo do arquivo
        conteudo_markdown = arquivo.read()
        # Converter o conteúdo Markdown para HTML usando a biblioteca markdown2
        #conteudo_html = markdown2.markdown(conteudo_markdown)
    st.markdown(conteudo_markdown, unsafe_allow_html=True)


if __name__ == '__main__':
    main()