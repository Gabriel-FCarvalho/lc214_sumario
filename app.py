import streamlit as st

# Título
st.title("Sumário Interativo - Lei Complementar 214/2025")

# Menu lateral
menu = st.sidebar.radio("Navegação", [
    "Art. 1º – Instituição da CBS e IBS",
    "Art. 3º – Regras de não cumulatividade",
    "Art. 4º – Split Payment",
    "Art. 5º – Comitê Gestor do IBS",
    "Art. 6º – Benefícios fiscais",
])

# Conteúdo dinâmico
if menu == "Art. 1º – Instituição da CBS e IBS":
    st.header("Art. 1º – Instituição da CBS e IBS")
    st.subheader("📖 Redação original")
    st.write("Institui-se a Contribuição sobre Bens e Serviços (CBS) e o Imposto sobre Bens e Serviços (IBS).")
    st.subheader("⚖️ Jurisprudência")
    st.write("Ainda não há jurisprudência específica. Referência: EC 132/2023.")
    st.subheader("🛠️ Exemplo prático")
    st.write("Uma empresa que hoje paga ICMS e ISS passará a pagar apenas IBS.")

elif menu == "Art. 3º – Regras de não cumulatividade":
    st.header("Art. 3º – Regras de não cumulatividade")
    st.subheader("📖 Redação original")
    st.write("O IBS e a CBS serão não cumulativos, assegurando créditos em todas as operações.")
    st.subheader("⚖️ Jurisprudência")
    st.write("STF, RE 607056, Tema 118 – reconheceu o direito ao crédito de PIS/Cofins.")
    st.subheader("🛠️ Exemplo prático")
    st.write("Hotel que compra mobiliário poderá aproveitar crédito integral de IBS/CBS.")

elif menu == "Art. 4º – Split Payment":
    st.header("Art. 4º – Split Payment")
    st.subheader("📖 Redação original")
    st.write("O recolhimento dos tributos dar-se-á por meio do pagamento fracionado no ato da operação.")
    st.subheader("⚖️ Jurisprudência")
    st.write("Ainda sem jurisprudência. Tema discutido em reformas internacionais de IVA (ex.: União Europeia).")
    st.subheader("🛠️ Exemplo prático")
    st.write("Na compra com cartão, parte do valor já vai direto para o Fisco.")

elif menu == "Art. 5º – Comitê Gestor do IBS":
    st.header("Art. 5º – Comitê Gestor do IBS")
    st.subheader("📖 Redação original")
    st.write("Fica instituído o Comitê Gestor do IBS, composto por representantes dos Estados e Municípios.")
    st.subheader("⚖️ Jurisprudência")
    st.write("Sem precedentes ainda. Discussões em ADIs futuras são esperadas.")
    st.subheader("🛠️ Exemplo prático")
    st.write("O comitê definirá regras de repasse de arrecadação entre estados e municípios.")

elif menu == "Art. 6º – Benefícios fiscais":
    st.header("Art. 6º – Benefícios fiscais")
    st.subheader("📖 Redação original")
    st.write("Estabelece regimes diferenciados como cashback, alíquotas reduzidas e isenções.")
    st.subheader("⚖️ Jurisprudência")
    st.write("Ainda não há, mas STF já decidiu sobre devolução tributária em programas sociais.")
    st.subheader("🛠️ Exemplo prático")
    st.write("Famílias de baixa renda terão cashback de energia elétrica e telecomunicações.")
