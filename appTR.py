# Integração direta com Streamlit concluída

import streamlit as st
from io import BytesIO
from importacao_e_combinacao_tr import (
    ler_modelo_docx, template_interno_padrao,
    combinar_secoes, gerar_docx
)

st.set_page_config(page_title="Agente Licitações - TR", layout="wide")
st.title("Agente de Licitações - Geração de Termos de Referência")

# Upload do arquivo modelo
tab1, tab2 = st.tabs(["Gerar Termo", "Sobre"])

with tab1:
    modelo = st.file_uploader("Envie o modelo DOCX (opcional)", type=["docx"])
    modo = st.selectbox(
        "Como combinar?",
        ["complementar", "modelo", "template"],
        index=0,
        help=(
            "complementar: usa o conteúdo do DOCX e preenche seções ausentes com o template interno;\n"
            "modelo: usa só o DOCX;\n"
            "template: usa só o template interno."
        ),
    )

    if st.button("Gerar TR Final"):
        secoes_template = template_interno_padrao()
        secoes_modelo = []
        if modelo is not None:
            secoes_modelo = ler_modelo_docx(modelo)

        secoes_final = combinar_secoes(secoes_modelo, secoes_template, modo=modo)

        caminho_saida = "/mnt/data/TR_final.docx"
        gerar_docx(
            secoes_final,
            caminho_saida,
            header_img="/mnt/data/logo-prefeitura.png",
            footer_img="/mnt/data/rodapé.png",
        )

        with open(caminho_saida, "rb") as f:
            st.download_button(
                label="Baixar TR final (DOCX)",
                data=f.read(),
                file_name="TR_final.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )

with tab2:
    st.markdown("""
    ### Sobre o Aplicativo
    Este aplicativo integra a leitura de modelos DOCX com numeração manual e o template interno 
    detalhado de Termos de Referência. Permite gerar documentos finais completos e padronizados.
    """)

# ==============================================
# appTR.py — Integração direta (pronto para uso)
# ==============================================
# Copie este trecho para o arquivo principal do seu app Streamlit (ex.: appTR.py)
# ou substitua o conteúdo existente. Ele utiliza o módulo acima.

if __name__ == "__main__":
    try:
        import streamlit as st
        from io import BytesIO

        st.set_page_config(page_title="TR Builder — Prefeitura de Brasnorte", layout="wide")
        st.title("Montar Termo de Referência (DOCX)")
        st.caption("Importa um modelo .docx com numeração manual, completa com o template interno e gera o DOCX final com cabeçalho e rodapé.")

        # Opções gerais
        col1, col2, col3 = st.columns([2,1,1])
        with col1:
            uploaded = st.file_uploader("Modelo (DOCX)", type=["docx"], help="Ex.: TR - SERVIÇOS POSTAIS - CORREIOS.docx")
        with col2:
            modo = st.selectbox(
                "Modo de combinação",
                ["complementar", "modelo", "template"],
                index=0,
                help=(
                    "complementar: usa o conteúdo do DOCX e preenche seções ausentes com o template interno;
"
                    "modelo: usa só o DOCX;
"
                    "template: usa só o template interno."
                ),
            )
        with col3:
            gerar_agora = st.checkbox("Gerar automaticamente ao carregar", value=False)

        st.markdown("---")
        c1, c2, c3, c4 = st.columns([1,1,1,1])
        with c1:
            header_on = st.checkbox("Incluir cabeçalho", value=True)
        with c2:
            footer_on = st.checkbox("Incluir rodapé", value=True)
        with c3:
            header_path = st.text_input("Caminho da imagem do cabeçalho", value="/mnt/data/logo-prefeitura.png")
        with c4:
            footer_path = st.text_input("Caminho da imagem do rodapé", value="/mnt/data/rodapé.png")

        st.markdown("---")
        prev, gerar = st.columns([1,1])
        with prev:
            if st.button("Pré-visualizar seções do modelo"):
                if uploaded:
                    try:
                        secoes_modelo = ler_modelo_docx(uploaded)
                        st.success(f"Seções detectadas no modelo: {len(secoes_modelo)}")
                        for s in secoes_modelo:
                            st.markdown(f"**{s.titulo}** — {len(s.elementos)} elemento(s)")
                    except Exception as e:
                        st.error(f"Erro ao ler o DOCX: {e}")
                else:
                    st.warning("Envie um arquivo DOCX para visualizar as seções.")

        with gerar:
            clicked = st.button("Gerar DOCX final")

        if (gerar_agora and uploaded) or clicked:
            try:
                secoes_template = template_interno_padrao()
                secoes_modelo = ler_modelo_docx(uploaded) if uploaded else []
                secoes_final = combinar_secoes(secoes_modelo, secoes_template, modo=modo)

                out_path = "/mnt/data/TR_final.docx"
                hpath = header_path if header_on else None
                fpath = footer_path if footer_on else None
                gerar_docx(secoes_final, out_path, header_img=hpath, footer_img=fpath)

                with open(out_path, "rb") as f:
                    st.download_button(
                        "Baixar TR_final.docx",
                        f.read(),
                        file_name="TR_final.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    )
                st.success("Documento gerado com sucesso!")
            except Exception as e:
                st.error(f"Falha ao gerar o DOCX: {e}")

        with st.expander("Requisitos (requirements.txt)"):
            st.code(
                """
streamlit>=1.36
python-docx==0.8.11
lxml>=4.9
pillow>=10.0
                """.strip(),
                language="text",
            )

    except Exception as _e:
        # Se estiver importando como módulo, ignore a execução do app.
        pass
