#!/usr/bin/env python3
"""Cria a estrutura de uma nova edição do Boletim Ligia a partir do template.

Detecta automaticamente o número da próxima edição (maior edição existente + 1),
copia templates/boletim/metadata.json e texto-modelo.md, e atualiza o índice
raiz (index.json). Os placeholders (slugs, título, autor) ainda precisam ser
preenchidos à mão.

Uso:
    python3 scripts/nova_edicao.py                # próxima edição, 2 textos
    python3 scripts/nova_edicao.py --textos 3      # 3 textos placeholder
    python3 scripts/nova_edicao.py --edicao 5      # força o número da edição
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BOLETINS_DIR = REPO_ROOT / "boletins"
TEMPLATE_DIR = REPO_ROOT / "templates" / "boletim"
INDEX_JSON = REPO_ROOT / "index.json"


def proxima_edicao() -> int:
    numeros = [int(p.name) for p in BOLETINS_DIR.iterdir() if p.is_dir() and p.name.isdigit()]
    return (max(numeros) + 1) if numeros else 0


def criar_edicao(edicao: int, n_textos: int) -> Path:
    slug_edicao = f"{edicao:02d}"
    destino = BOLETINS_DIR / slug_edicao
    if destino.exists():
        raise SystemExit(f"boletins/{slug_edicao} já existe — escolha outro número com --edicao")

    destino.mkdir(parents=True)

    texto_modelo = (TEMPLATE_DIR / "texto-modelo.md").read_text(encoding="utf-8")
    slugs = [f"{i:02d}-slug-do-titulo" for i in range(1, n_textos + 1)]
    for slug in slugs:
        pasta_texto = destino / slug
        pasta_texto.mkdir()
        (pasta_texto / "texto.md").write_text(texto_modelo, encoding="utf-8")

    metadata = json.loads((TEMPLATE_DIR / "metadata.json").read_text(encoding="utf-8"))
    metadata["edicao"] = edicao
    metadata["titulo"] = f"Boletim Ligia #{edicao}"
    metadata["data_publicacao"] = date.today().isoformat()
    metadata["textos"] = slugs
    (destino / "metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return destino


def atualizar_index(edicao: int, destino: Path) -> None:
    index = json.loads(INDEX_JSON.read_text(encoding="utf-8"))
    index["boletins"].append(
        {
            "edicao": edicao,
            "path": str(destino.relative_to(REPO_ROOT)),
            "titulo": f"Boletim Ligia #{edicao}",
            "data_publicacao": date.today().isoformat(),
        }
    )
    index["boletins"].sort(key=lambda b: b["edicao"])
    INDEX_JSON.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--edicao", type=int, help="Número da edição (padrão: próximo disponível)")
    parser.add_argument("--textos", type=int, default=2, help="Quantidade de textos placeholder a criar (padrão: 2)")
    args = parser.parse_args()

    edicao = args.edicao if args.edicao is not None else proxima_edicao()
    destino = criar_edicao(edicao, args.textos)
    atualizar_index(edicao, destino)

    rel = destino.relative_to(REPO_ROOT)
    print(f"Criado {rel}/ com {args.textos} texto(s) placeholder e metadata.json.")
    print(f"index.json atualizado com a edição {edicao}.")
    print("Próximos passos: renomear as pastas de texto com um slug real, preencher")
    print("titulo/autor/corpo em cada texto.md, e ajustar metadata.json (textos, data, links).")


if __name__ == "__main__":
    main()
