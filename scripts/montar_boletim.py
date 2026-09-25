#!/usr/bin/env python3
"""Monta um Boletim Ligia inteiro em um único .md, pronto para colar no Substack.

Lê boletins/<edicao>/metadata.json, junta a introdução, cada texto (na ordem
listada em "textos") e a lista de links, na ordem em que devem aparecer na
edição final.

Uso:
    python scripts/montar_boletim.py 00          # monta só a edição 00
    python scripts/montar_boletim.py 00 01       # monta várias edições
    python scripts/montar_boletim.py --all       # monta todas as edições em boletins/
    python scripts/montar_boletim.py 00 -o /tmp  # escolhe o diretório de saída
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BOLETINS_DIR = REPO_ROOT / "boletins"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "dist"


def parse_frontmatter(texto_md: str) -> tuple[dict, str]:
    """Separa o frontmatter YAML simples (chave: valor) do corpo do texto."""
    if not texto_md.startswith("---"):
        return {}, texto_md

    _, raw_front, body = texto_md.split("---", 2)
    frontmatter: dict[str, str] = {}
    for line in raw_front.strip().splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"')

    return frontmatter, body.strip()


def carregar_texto(boletim_dir: Path, slug: str) -> tuple[dict, str]:
    caminho = boletim_dir / slug / "texto.md"
    if not caminho.exists():
        raise FileNotFoundError(f"Não encontrei {caminho}")
    return parse_frontmatter(caminho.read_text(encoding="utf-8"))


def montar_edicao(boletim_dir: Path) -> str:
    metadata = json.loads((boletim_dir / "metadata.json").read_text(encoding="utf-8"))

    partes: list[str] = []
    partes.append(f"# {metadata['titulo']}")
    partes.append(f"*Publicado em {metadata['data_publicacao']}*")

    if metadata.get("introducao"):
        partes.append(metadata["introducao"])

    for slug in metadata.get("textos", []):
        frontmatter, corpo = carregar_texto(boletim_dir, slug)
        titulo = frontmatter.get("titulo", slug)
        autor = frontmatter.get("autor", "")

        partes.append(f"## {titulo}")
        if autor:
            partes.append(f"*Por {autor}*")
        partes.append(corpo)

    links = metadata.get("links", [])
    if links:
        partes.append("## Links & Papers")
        linhas_links = [
            f"- [{link['titulo']}]({link['url']})"
            + (f" (enviado por {link['enviado_por']})" if link.get("enviado_por") else "")
            for link in links
        ]
        partes.append("\n".join(linhas_links))

    return "\n\n".join(partes) + "\n"


def resolver_edicoes(args_edicoes: list[str]) -> list[Path]:
    if not BOLETINS_DIR.exists():
        sys.exit(f"Diretório não encontrado: {BOLETINS_DIR}")

    if not args_edicoes:
        return sorted(p for p in BOLETINS_DIR.iterdir() if p.is_dir())

    resolvidas = []
    for edicao in args_edicoes:
        candidata = BOLETINS_DIR / edicao.zfill(2)
        if not candidata.is_dir():
            candidata = BOLETINS_DIR / edicao
        if not candidata.is_dir():
            sys.exit(f"Edição não encontrada: {edicao}")
        resolvidas.append(candidata)
    return resolvidas


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("edicoes", nargs="*", help="Números das edições a montar (ex: 00 01). Vazio = todas.")
    parser.add_argument("--all", action="store_true", help="Monta todas as edições em boletins/")
    parser.add_argument("-o", "--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Diretório de saída dos .md montados")
    args = parser.parse_args()

    edicoes = [] if args.all else args.edicoes
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for boletim_dir in resolver_edicoes(edicoes):
        markdown = montar_edicao(boletim_dir)
        destino = output_dir / f"boletim-{boletim_dir.name}.md"
        destino.write_text(markdown, encoding="utf-8")
        print(f"Gerado {destino.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
