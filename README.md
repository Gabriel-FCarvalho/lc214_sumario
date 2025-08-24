# Sumário Interativo – Lei Complementar 214/2025 (FULL)

Este app Streamlit oferece um sumário interativo para navegar pelos **544 artigos** e **23 anexos** da LC 214/2025.
Os conteúdos estão inicialmente como **placeholders**. Você pode alimentar o texto oficial, jurisprudência e exemplos práticos
pela própria interface (fazendo upload de um JSON) ou editando o arquivo `data/schema.json` no repositório.

## Como usar (Cloud)
1. Publique no Streamlit Cloud apontando para este repositório.
2. No app, escolha o **Artigo** ou **Anexo** na barra lateral.
3. Use a aba **Edição** para colar a redação oficial, incluir jurisprudência e exemplos.
4. Clique em **Exportar Base (.json)** para baixar o arquivo atualizado e depois suba no GitHub para persistir.

## Estrutura de dados
- `data/schema.json` → contém todos os artigos e anexos, com campos:
  - Artigos: `titulo`, `redacao`, `jurisprudencia`, `exemplos`
  - Anexos: `titulo`, `conteudo`

## Dica
Se você já tiver o texto oficial em Markdown/HTML, cole na aba **Redação** do artigo correspondente.
