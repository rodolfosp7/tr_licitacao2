# EXEMPLO DE AGENTE DE LICITAÇÕES EM PYTHON (TERMO DE REFERÊNCIA)
# Atualizado com base nos arts. 6º, 40 e 92 da Lei 14.133/2021 e no art. 30 do Decreto Municipal nº 09/2024

import streamlit as st
from docx import Document
from io import BytesIO

st.set_page_config(page_title="Gerador de Termo de Referência", layout="centered")

st.title("📑 Gerador de Termo de Referência Automático - Prefeitura de Brasnorte")

st.markdown(
    "Informe apenas o objeto da contratação. O sistema irá gerar automaticamente o Termo de Referência completo e detalhado, com base na Lei 14.133/2021 e no Decreto Municipal nº 09/2024. As respostas seguirão o modelo detalhado e aprofundado indicado pelo usuário."
)

# Entrada única
objeto = st.text_area(
    "📝 Objeto da contratação",
    placeholder=(
        "Ex: Contratação de empresa especializada para fornecimento de gás de cozinha "
        "para unidades administrativas e escolares."
    ),
    height=150,
)

# Geração do TR + Exportação para DOCX (tudo no mesmo bloco para evitar NameError)
if st.button("🔧 Gerar Termo de Referência") and objeto:
    termo = f"""
PREFEITURA MUNICIPAL DE BRASNORTE - MT
SECRETARIA MUNICIONAL DE ADMINISTRAÇÃO

TERMO DE REFERÊNCIA

1. DAS CONDIÇÕES GERAIS DA CONTRATAÇÃO

1.1 O presente termo de referência tem por objeto o {objeto.upper()}, com sede localizada no município de Brasnorte-MT, em conformidade com as especificações de descrição e quantidade detalhadamente elencadas neste documento, amparada pelas disposições legais vigentes que regulam tal procedimento, visando atender as necessidades da Prefeitura Municipal de Brasnorte-MT e de suas Secretarias Municipais;

1.2 O objeto desta contratação não se enquadra como sendo de bem de luxo, conforme Decreto Municipal nº 03/2024;

1.3 O prazo de vigência da contratação é de 12 (doze) meses, contados da data de assinatura da ARP (Ata Registro de Preço) ou do Contrato conforme celebrado, na forma do artigo 105 da Lei n° 14.133/2021, podendo o mesmo ser prorrogado a critério da Administração Pública.

1.4 O prazo de vigência poderá ser prorrogado, desde que haja interesse de ambas as partes, na forma autorizada pelos artigos 106 e 107, da Lei nº 14.133/2021.

2. DESCRIÇÃO DA NECESSIDADE DA CONTRATAÇÃO E FUNDAMENTAÇÃO LEGAL

2.1 A presente contratação se fundamenta na necessidade institucional de garantir o fornecimento contínuo de bens ou a prestação de serviços essenciais relacionados ao objeto {objeto.lower()}, indispensáveis ao funcionamento e à continuidade dos serviços públicos municipais.

2.2 A contratação tem por finalidade atender às Secretarias Municipais, promovendo suporte às atividades administrativas, operacionais e técnicas essenciais à execução das políticas públicas locais;

2.3 Justifica-se pela inexistência de estrutura própria que permita a realização direta do fornecimento ou execução do objeto, de forma a garantir eficiência, economicidade e regularidade dos serviços;

2.4 A contratação será formalizada por meio de procedimento licitatório na modalidade de Pregão Eletrônico, com critério de julgamento por menor preço por item, nos termos do artigo 82 e seguintes da Lei nº 14.133/2021.

2.5 Será adotado o Sistema de Registro de Preços, regido conforme Decreto Federal nº 11.462/2023, proporcionando maior flexibilidade, economicidade e planejamento orçamentário.

3. DESCRIÇÃO DA SOLUÇÃO COMO UM TODO CONSIDERADO O CICLO DE VIDA DO OBJETO E ESPECIFICAÇÃO DOS SERVIÇOS

3.1 O ciclo de vida do objeto abrange as fases de planejamento da demanda, seleção do fornecedor, formalização contratual, execução, acompanhamento da entrega, fiscalização e encerramento contratual, incluindo avaliação da qualidade e desempenho.

3.2 Foram analisadas as seguintes soluções:

Solução 1: Execução direta pela Administração Pública – inviável por ausência de estrutura, equipe técnica, equipamentos e logística adequada.

Solução 2: Contratação de empresa especializada via licitação – viável e recomendada, possibilita controle de qualidade, cumprimento de prazos e maior eficiência administrativa.

3.3 Conclusão: Opta-se pela execução indireta, por meio de licitação, com contratação de empresa especializada, conforme previsto na Lei nº 14.133/2021, garantindo atendimento das necessidades públicas com qualidade, regularidade e economicidade.

4. REQUISITOS DA CONTRATAÇÃO

4.1 A contratada deverá comprovar:
- Regularidade fiscal e trabalhista;
- Capacidade técnica compatível com o objeto;
- Equipe técnica qualificada;
- Atendimento contínuo conforme demanda;
- Atendimento às normas de segurança, qualidade e meio ambiente;
- Disponibilidade de infraestrutura compatível com o serviço ou fornecimento;
- Responsabilidade socioambiental.

4.2 A prestação dos serviços ou fornecimentos deverá respeitar todas as exigências estabelecidas no edital, plano de trabalho e cronograma físico-financeiro aprovado.

5. MODELO DE EXECUÇÃO CONTRATUAL

5.1 A execução contratual se dará por meio de ordens de fornecimento ou serviço emitidas pela Administração, com acompanhamento do fiscal designado.

5.2 Os pagamentos serão realizados após aceite formal, com apresentação de nota fiscal, relatório de entrega ou execução, e comprovação da conformidade com os critérios técnicos e quantitativos definidos no contrato.

5.3 A gestão e fiscalização do contrato observará o disposto nos artigos 117 a 124 da Lei nº 14.133/2021, incluindo a designação de fiscais, emissão de notificações, e elaboração de relatórios de acompanhamento.

6. CRITÉRIOS DE MEDIÇÃO

6.1 A medição será feita com base em documentos comprobatórios de execução (relatórios, notas fiscais, ordens de serviço, comprovantes de entrega etc.), validados pelo fiscal designado.

6.2 O pagamento será condicionado à entrega efetiva e ao cumprimento dos padrões de qualidade, prazos e especificações técnicas estabelecidas no edital e contrato.

**Brasnorte - MT, Julho de 2025**

---

Este documento é gerado automaticamente com base nas diretrizes legais vigentes e poderá ser personalizado conforme peculiaridades do objeto. Recomenda-se revisão da Procuradoria Jurídica e do Controle Interno.
"""

    # Exibe o texto gerado
    st.markdown("### 📄 Resultado do Termo de Referência")
    st.text_area("Termo Gerado:", termo, height=600)

    # ===== Exportação para Word (.docx) =====
    def gerar_docx(texto: str) -> BytesIO:
        doc = Document()
        for linha in texto.strip().split("\n"):
            doc.add_paragraph(linha)
        buf = BytesIO()
        doc.save(buf)
        buf.seek(0)
        return buf

    arquivo_docx = gerar_docx(termo)

    st.download_button(
        label="📥 Baixar Termo em Word (.docx)",
        data=arquivo_docx,
        file_name="Termo_de_Referencia_Brasnorte.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
