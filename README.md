# Boletim Ligia

Repositório com os textos de todas as edições do **Boletim Ligia**, a newsletter
quinzenal sobre Inteligência Artificial da [Liga Acadêmica de Inteligência
Artificial da UFPE](https://github.com/ligia-ufpe). Serve dois propósitos:

1. **Arquivo histórico** dos textos de cada edição, versionado e organizado por pasta.
2. **Fonte de dados para o blogsite**, que consulta os arquivos diretamente via
   `raw.githubusercontent.com` (sem precisar de uma API própria).

## Estrutura

```
boletim/
├── index.json                    # manifesto com todas as edições
├── boletins/
│   ├── 00/
│   │   ├── metadata.json         # dados da edição + ordem dos textos + links
│   │   ├── 01-slug-do-texto/
│   │   │   └── texto.md          # frontmatter (titulo, autor, ...) + corpo em markdown
│   │   ├── 02-slug-do-texto/
│   │   │   └── texto.md
│   │   └── ...
│   └── 01/
│       └── ...
└── scripts/
    └── montar_boletim.py         # junta uma edição inteira num único .md
```

Cada edição é uma pasta em `boletins/<edicao>` (dois dígitos, ex: `00`, `01`,
`02`...). Dentro dela:

- `metadata.json` guarda o que descreve a edição como um todo: número, título,
  data de publicação, introdução/saudação (opcional), a lista de links
  interessantes do grupo de papers (opcional) e, principalmente, `textos`: a
  lista ordenada de slugs das pastas de texto daquela edição.
- Cada texto vive na sua própria pasta, com um único arquivo `texto.md`. O
  arquivo começa com um frontmatter simples (`chave: valor`) e depois o corpo
  em markdown:

  ```markdown
  ---
  titulo: "Título do texto"
  autor: "Nome do autor"
  ---

  Corpo do texto em markdown normal, com links, negrito, listas, etc.
  ```

Esse formato é **genérico de propósito**: não existe uma seção fixa tipo
"Visão Computacional" ou "NLP". Cada edição é simplesmente uma introdução
opcional + uma lista ordenada de textos de tema livre (com só título e autor)
+ uma lista opcional de links. O formato atual do boletim é de **2 a 3 textos
de tema livre por edição, somando 600 a 900 palavras no total** — mas a
estrutura suporta qualquer número de textos e qualquer combinação de campos
opcionais sem precisar mudar nada no repositório ou no script.

## Como consumir do blogsite (via raw.githubusercontent.com)

Como o repositório é público, qualquer arquivo pode ser buscado direto, sem
autenticação nem API do GitHub:

```
https://raw.githubusercontent.com/ligia-ufpe/boletim/main/index.json
https://raw.githubusercontent.com/ligia-ufpe/boletim/main/boletins/00/metadata.json
https://raw.githubusercontent.com/ligia-ufpe/boletim/main/boletins/00/01-aprendendo-sem-rotulos-dinov3-e-self-supervised-learning/texto.md
```

Fluxo sugerido para o blog:

1. Buscar `index.json` para listar as edições disponíveis.
2. Para uma edição, buscar `boletins/<edicao>/metadata.json` para pegar
   título, data, introdução, links e a ordem dos textos.
3. Para cada slug em `textos`, buscar `boletins/<edicao>/<slug>/texto.md`,
   separar o frontmatter do corpo e renderizar o markdown.

## Como adicionar uma nova edição

1. Crie a pasta `boletins/<novo-numero-com-2-digitos>/`.
2. Para cada texto, crie uma subpasta com um slug (`01-slug-do-titulo/`,
   `02-slug-do-titulo/`...) contendo um `texto.md` com `titulo` e `autor` no
   frontmatter e o corpo do texto abaixo.
3. Crie o `metadata.json` da edição (copie um existente como modelo) e liste
   os slugs em ordem no campo `textos`.
4. Adicione a edição em `index.json`.
5. Rode o script de montagem (veja abaixo) para conferir como fica o `.md`
   final antes de publicar no Substack.

## Script: juntar uma edição num único .md

`scripts/montar_boletim.py` lê o `metadata.json` de uma edição, junta a
introdução + todos os textos (na ordem certa) + a lista de links num único
arquivo markdown, pronto para colar no Substack.

```bash
# monta só a edição 00
python3 scripts/montar_boletim.py 00

# monta várias edições de uma vez
python3 scripts/montar_boletim.py 00 01

# monta todas as edições em boletins/
python3 scripts/montar_boletim.py --all

# escolhe onde salvar (padrão: ./dist)
python3 scripts/montar_boletim.py 00 -o /caminho/de/saida
```

O script não tem dependências externas (só a biblioteca padrão do Python 3).
Os arquivos gerados vão para `dist/`, que não é versionado.
