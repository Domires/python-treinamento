"""Gera os GIFs animados usados nas aulas desta pasta.

Execute nesta pasta:
    python gerar_gifs.py                  -> gera todas as animações
    python gerar_gifs.py casting for_lista -> gera só as informadas
    python gerar_gifs.py --aula 03        -> gera só as da aula 03

As cenas ficam nos arquivos cenas_XX.py (um por aula) e as funções de desenho
compartilhadas ficam em base.py. Os .gif são salvos nesta mesma pasta.
"""

import importlib
import sys
from pathlib import Path

from base import salvar

PASTA = Path(__file__).parent


def carregar_cenas():
    """Junta os dicionários ANIMACOES de todos os arquivos cenas_XX.py."""
    todas = {}
    for arquivo in sorted(PASTA.glob("cenas_*.py")):
        modulo = importlib.import_module(arquivo.stem)
        aula = arquivo.stem.split("_")[1]
        for nome, (funcao, total) in modulo.ANIMACOES.items():
            todas[nome] = (funcao, total, aula)
    return todas


if __name__ == "__main__":
    cenas = carregar_cenas()
    argumentos = sys.argv[1:]
    if argumentos[:1] == ["--aula"]:
        escolhidas = [nome for nome, (_, _, aula) in cenas.items() if aula == argumentos[1]]
    else:
        escolhidas = argumentos or list(cenas)
    for nome in escolhidas:
        funcao, total, _ = cenas[nome]
        salvar(nome, funcao, total)
