\
import json
import io
import base64
import streamlit as st

st.set_page_config(page_title="LC 214/2025 – Sumário Interativo", layout="wide")

@st.cache_data(show_spinner=False)
def load_schema() -> dict:
    with open("data/schema.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_schema_to_bytes(schema: dict) -> bytes:
    return json.dumps(schema, ensure_ascii=False, indent=2).encode("utf-8")

def download_button(label: str, data: bytes, file_name: str, mime: str = "application/octet-stream"):
    st.download_button(label, data=data, file_name=file_name, mime=mime, use_container_width=True)

schema = load_schema()

# --- Sidebar Navigation ---
st.sidebar.title("LC 214/2025 – Navegação")
mode = st.sidebar.radio("Seção", ["Artigos", "Anexos", "Sobre a Lei"])

if mode == "Sobre a Lei":
    st.header("Lei Complementar 214/2025 – Sumário Interativo")
    st.write("Versão da base:", schema.get("versao", ""))
    st.write(schema.get("observacoes", ""))
    st.subheader("Importar base (.json)")
    up = st.file_uploader("Carregue um arquivo JSON exportado pelo app", type=["json"], accept_multiple_files=False)
    if up:
        try:
            new_schema = json.load(io.TextIOWrapper(up, encoding="utf-8"))
            st.success("Base carregada com sucesso para esta sessão.")
            schema = new_schema
        except Exception as e:
            st.error(f"Falha ao carregar JSON: {e}")
    st.subheader("Exportar base atual")
    download_button("Exportar Base (.json)", save_schema_to_bytes(schema), "lc214_base.json", "application/json")
    st.stop()

# --- Common UI: search ---
with st.sidebar.expander("Pesquisar", expanded=False):
    q = st.text_input("Palavra-chave (título, redação, jurisprudência, exemplos)")

if mode == "Artigos":
    total = len(schema["artigos"])
    st.sidebar.markdown(f"**Total de artigos:** {total}")
    # Choose article number
    art_num = st.sidebar.number_input("Ir para o Artigo nº", min_value=1, max_value=total, value=1, step=1)
    # Search list
    artigos_items = list(schema["artigos"].items())
    if q:
        qlower = q.lower()
        artigos_items = [(k, v) for k, v in artigos_items if any(
            qlower in (v.get("titulo","")+v.get("redacao","")+v.get("jurisprudencia","")+v.get("exemplos","")).lower()
        )]
        if not artigos_items:
            st.sidebar.info("Nenhum artigo encontrado para a busca.")
    # Selector
    options = [int(k) for k, _ in artigos_items]
    if art_num not in options and options:
        art_num = options[0]
    st.sidebar.divider()
    st.sidebar.write("Seleção rápida")
    sel = st.sidebar.selectbox("Escolha o artigo", options=options, index=options.index(art_num) if options else 0)
    art_num = sel

    # --- Display ---
    art_key = str(art_num)
    art = schema["artigos"][art_key]
    st.title(f'{art.get("titulo", f"Art. {art_num}")}')
    tabs = st.tabs(["📖 Redação", "⚖️ Jurisprudência", "🛠️ Exemplos", "✏️ Edição"])

    with tabs[0]:
        if art.get("redacao"):
            st.markdown(art["redacao"])
        else:
            st.info("Sem conteúdo ainda. Cole aqui a **redação oficial** quando tiver.")
        download_button("Baixar Redação (Markdown)", (art.get("redacao","") or "").encode("utf-8"),
                        f"artigo_{art_num:03d}_redacao.md", "text/markdown")

    with tabs[1]:
        if art.get("jurisprudencia"):
            st.markdown(art["jurisprudencia"])
        else:
            st.warning("Sem jurisprudência cadastrada para este artigo.")
        download_button("Baixar Jurisprudência (Markdown)", (art.get("jurisprudencia","") or "").encode("utf-8"),
                        f"artigo_{art_num:03d}_jurisprudencia.md", "text/markdown")

    with tabs[2]:
        if art.get("exemplos"):
            st.markdown(art["exemplos"])
        else:
            st.info("Sem exemplos cadastrados. Use esta aba para registrar **casos práticos**.")
        download_button("Baixar Exemplos (Markdown)", (art.get("exemplos","") or "").encode("utf-8"),
                        f"artigo_{art_num:03d}_exemplos.md", "text/markdown")

    with tabs[3]:
        st.caption("As alterações abaixo **não** persistem no repositório. Exporte a base e suba no GitHub para salvar definitivamente.")
        redacao = st.text_area("📖 Redação oficial (Markdown)", value=art.get("redacao",""), height=200)
        jurisprudencia = st.text_area("⚖️ Jurisprudência (Markdown)", value=art.get("jurisprudencia",""), height=150)
        exemplos = st.text_area("🛠️ Exemplos práticos (Markdown)", value=art.get("exemplos",""), height=150)
        if st.button("Aplicar nesta sessão"):
            art["redacao"] = redacao
            art["jurisprudencia"] = jurisprudencia
            art["exemplos"] = exemplos
            schema["artigos"][art_key] = art
            st.success("Conteúdo atualizado nesta sessão.")
        st.divider()
        download_button("Exportar Base Atualizada (.json)", save_schema_to_bytes(schema), "lc214_base_atualizada.json", "application/json")

elif mode == "Anexos":
    total = len(schema["anexos"])
    st.sidebar.markdown(f"**Total de anexos:** {total}")
    anex_num = st.sidebar.number_input("Ir para o Anexo nº", min_value=1, max_value=total, value=1, step=1)
    anexos_items = list(schema["anexos"].items())
    if q:
        qlower = q.lower()
        anexos_items = [(k, v) for k, v in anexos_items if qlower in (v.get("titulo","")+v.get("conteudo","")).lower()]
        if not anexos_items:
            st.sidebar.info("Nenhum anexo encontrado para a busca.")
    options = [int(k) for k, _ in anexos_items]
    if anex_num not in options and options:
        anex_num = options[0]
    sel = st.sidebar.selectbox("Escolha o anexo", options=options, index=options.index(anex_num) if options else 0)
    anex_num = sel

    anex_key = str(anex_num)
    anex = schema["anexos"][anex_key]
    st.title(f'{anex.get("titulo", f"Anexo {anex_num}")}')
    tabs = st.tabs(["📄 Conteúdo", "✏️ Edição"])

    with tabs[0]:
        if anex.get("conteudo"):
            st.markdown(anex["conteudo"])
        else:
            st.info("Sem conteúdo ainda. Cole aqui o texto do **anexo** quando tiver.")
        download_button("Baixar Conteúdo (Markdown)", (anex.get("conteudo","") or "").encode("utf-8"),
                        f"anexo_{anex_num:02d}.md", "text/markdown")

    with tabs[1]:
        st.caption("As alterações abaixo **não** persistem no repositório. Exporte a base e suba no GitHub para salvar definitivamente.")
        conteudo = st.text_area("Conteúdo do anexo (Markdown)", value=enex.get("conteudo","") if (enex:=anex) else "", height=300)
        if st.button("Aplicar nesta sessão", key="apply_anexo"):
            anex["conteudo"] = conteudo
            schema["anexos"][anex_key] = anex
            st.success("Conteúdo atualizado nesta sessão.")
        st.divider()
        download_button("Exportar Base Atualizada (.json)", save_schema_to_bytes(schema), "lc214_base_atualizada.json", "application/json")
