# Template de edição

Modelo para criar uma nova edição do Boletim Ligia. Duas formas de usar:

## Opção 1 — script (mais rápido)

```bash
python3 scripts/nova_edicao.py
```

Isso cria `boletins/<próxima-edição>/` já com `metadata.json` preenchido
(número da edição, título, data de hoje) e as pastas de texto placeholder,
prontas para você renomear e preencher. Veja `python3 scripts/nova_edicao.py --help`
para escolher o número de textos ou forçar um número de edição específico.

## Opção 2 — copiar manualmente

1. Copie esta pasta (`templates/boletim/`) para `boletins/<novo-numero-com-2-digitos>/`.
2. Para cada texto da edição, crie uma subpasta com um slug descritivo
   (`01-slug-do-titulo/`, `02-slug-do-titulo/`, ...) e copie
   `texto-modelo.md` para dentro dela como `texto.md`.
3. Preencha o `titulo` e o `autor` no frontmatter de cada `texto.md` e
   escreva o corpo do texto abaixo.
4. Ajuste o `metadata.json` da edição: número, título, data de publicação,
   introdução (ou remova o campo, se não tiver) e a lista `textos` com os
   slugs na ordem certa. O campo `links` também é opcional — remova-o se
   não houver links para essa edição.
5. Adicione a edição em `index.json`, na raiz do repositório.

### Campos opcionais no frontmatter de `texto.md`

Além de `titulo` e `autor`, você pode incluir (livremente, se fizer sentido
para o texto):

- `autor_url`: link do LinkedIn/site do autor.
- `coluna_convidado: true`: sinaliza que é um texto de convidado externo.
- `imagem`: URL de uma imagem de capa para o texto (usada como thumbnail
  na listagem e como banner na página do texto pelo blogsite).
- `fonte`: um link de referência principal do texto.

Nenhum desses é obrigatório — o `README.md` da raiz do repositório explica
a estrutura completa e como o blogsite consome os arquivos.
