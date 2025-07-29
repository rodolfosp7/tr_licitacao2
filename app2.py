# EXEMPLO DE AGENTE DE LICITAÇÕES EM PYTHON (TERMO DE REFERÊNCIA)
# Atualizado com base nos arts. 6º, 40 e 92 da Lei 14.133/2021 e no art. 30 do Decreto Municipal nº 09/2024

import streamlit as st

st.set_page_config(page_title="Gerador de Termo de Referência", layout="centered")

st.title("📑 Gerador de Termo de Referência Automático - Prefeitura de Brasnorte")

st.markdown("Informe apenas o objeto da contratação. O sistema irá gerar automaticamente o Termo de Referência completo e detalhado, com base na Lei 14.133/2021 e no Decreto Municipal nº 09/2024.")

# Entrada única
objeto = st.text_area("📝 Objeto da contratação", placeholder="Ex: Contratação de empresa especializada para fornecimento de refeições prontas para servidores em viagem técnica.", height=150)

if st.button("🔧 Gerar Termo de Referência") and objeto:
    termo = f"""
PREFEITURA MUNICIPAL DE BRASNORTE - MT
SECRETARIA MUNICIPAL DE ADMINISTRAÇÃO

TERMO DE REFERÊNCIA

1. DAS CONDIÇÕES GERAIS DA CONTRATAÇÃO

1.1 O presente termo de referência tem por objeto {objeto.upper()} com sede localizada no município de Brasnorte-MT, em conformidade com as especificações de descrição e quantidade detalhadamente elencadas neste documento, amparada pelas disposições legais vigentes que regulam tal procedimento, visando atender as necessidades da Prefeitura Municipal de Brasnorte-MT e de suas Secretarias Municipais;

1.2 O objeto desta contratação não se enquadra como sendo de bem de luxo, conforme Decreto Municipal nº 03/2024;

1.3 O prazo de vigência da contratação é de 12 (doze) meses, contados da data de assinatura da ARP (Ata Registro de Preço) ou do Contrato conforme celebrado, na forma do artigo 105 da Lei n° 14.133/2021, podendo o mesmo ser prorrogado a critério da Administração Pública.

1.4 O prazo de vigência poderá ser prorrogado, desde que haja interesse de ambas as partes, na forma autorizada pelos artigos 106 e 107, da Lei nº 14.133/2021.

2. DESCRIÇÃO DA NECESSIDADE DA CONTRATAÇÃO E FUNDAMENTAÇÃO LEGAL

2.1 A presente contratação se fundamenta na necessidade em possuir serviços relacionados ao objeto mencionado para atender as necessidades do Município de Brasnorte/MT, em todas as suas Secretarias Municipais, utilizados no desempenho de suas atividades e cumprimento de sua missão institucional;

2.2 A demanda se destina ao atendimento de pessoas, profissionais, consultores, técnicos, representantes de órgãos públicos, fornecedores, palestrantes, prestadores de serviços, autoridades ou demais colaboradores que se deslocam de outras localidades até o município de Brasnorte-MT para realizarem atividades de interesse público;

2.3 A contratação se justifica pela necessidade de oferecer suporte adequado à realização de atividades administrativas, técnicas e operacionais da Administração Pública;

2.4 Considerando que o município não dispõe de estrutura própria para suprir a demanda, torna-se indispensável a contratação especializada para garantir eficiência, economicidade e qualidade na execução do serviço.

2.5 A medida visa proporcionar condições dignas e adequadas para as finalidades públicas previstas, atendendo aos princípios da dignidade, da eficiência administrativa, do interesse público e da economicidade.

2.6 FUNDAMENTAÇÃO LEGAL: A presente contratação será realizada na forma de Pregão Eletrônico, com critério de julgamento por menor preço por item, adotando-se o Sistema de Registro de Preços (SRP), nos termos do artigo 82 e seguintes da Lei nº 14.133/2021, observando também o Decreto Federal nº 11.462/2023.

3. DESCRIÇÃO DA SOLUÇÃO COMO UM TODO CONSIDERADO O CICLO DE VIDA DO OBJETO E ESPECIFICAÇÃO DOS SERVIÇOS

3.1 O ciclo de vida do objeto abrange desde o planejamento da demanda, seleção da empresa, contratação, execução, fiscalização, encerramento contratual e avaliação de desempenho. A especificação do serviço deverá considerar qualidade, segurança, funcionalidade, durabilidade e sustentabilidade.

3.2 Foram avaliadas as seguintes alternativas:

- Solução 1: Execução direta pela Prefeitura – inviável por falta de estrutura, equipe técnica e custos elevados.
- Solução 2: Contratação de empresa especializada – viável, eficiente e em conformidade com a Lei nº 14.133/2021.

3.3 Conclusão: Recomenda-se a execução indireta por meio de licitação, garantindo maior efetividade, segurança jurídica, economia e atendimento às exigências legais.

4. REQUISITOS DA CONTRATAÇÃO

4.1 A empresa contratada deverá atender aos seguintes requisitos mínimos:

- Regularidade fiscal, trabalhista e técnica;
- Comprovação de capacidade técnica por meio de atestados;
- Atendimento integral às normas de segurança, higiene e qualidade;
- Infraestrutura compatível com a demanda;
- Atendimento contínuo e ininterrupto durante a vigência contratual;
- Cumprimento de cronograma físico-financeiro e plano de trabalho aprovado;
- Responsabilidade socioambiental, se aplicável.

5. MODELO DE EXECUÇÃO CONTRATUAL

5.1 A execução será realizada conforme ordens emitidas pela Administração, com fiscalização contínua.

5.2 O contratado deverá cumprir prazos, especificações e quantitativos conforme definidos.

5.3 O pagamento será condicionado ao aceite formal, mediante apresentação de nota fiscal e relatório de execução.

5.4 A fiscalização e gestão do contrato seguirão os artigos 117 a 124 da Lei nº 14.133/2021, com designação de fiscais e emissão de relatórios de acompanhamento e avaliação.

6. CRITÉRIOS DE MEDIÇÃO

6.1 A medição será mensal e baseada em relatórios de execução validados pela Administração.

6.2 Serão considerados itens como tipo de serviço, quantidade, prazos, conformidade técnica e qualidade.

6.3 O pagamento será efetuado após aceitação formal, observadas as glosas por eventuais inconsistências ou inadimplementos contratuais.

**Brasnorte - MT, Julho de 2025**

---

Este modelo poderá ser ajustado conforme peculiaridades do objeto. Recomenda-se análise prévia da Procuradoria Jurídica e Controle Interno.
"""

    st.markdown("### 📄 Resultado do Termo de Referência")
    st.text_area("Termo Gerado:", termo, height=600)
