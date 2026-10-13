"""Exibe as animações (GIFs) das aulas na janela interativa do VS Code.

Uso (em uma célula #%%):
    from animacoes import mostrar_animacao
    mostrar_animacao("variavel_caixa")
"""

import base64
from pathlib import Path

PASTA = Path(__file__).parent


def encontrar_gif(nome):
    """Procura o GIF nesta pasta e, se não achar, nas pastas animacoes/ dos outros módulos.

    Isso é necessário porque a janela interativa pode ser reaproveitada entre arquivos de
    pastas diferentes: o Python guarda o primeiro pacote "animacoes" que importou e o
    reutiliza nas outras aulas.
    """
    caminho = PASTA / f"{nome}.gif"
    if caminho.exists():
        return caminho
    for outro in sorted(PASTA.parent.parent.glob(f"*/animacoes/{nome}.gif")):
        return outro
    return None


def mostrar_animacao(nome, largura=720):
    """Mostra o GIF <nome>.gif na saída da célula."""
    caminho = encontrar_gif(nome)
    if caminho is None:
        print(f"Animação não encontrada: {nome}.gif (rode gerar_gifs.py na pasta animacoes do módulo)")
        return

    try:
        from IPython import get_ipython
        from IPython.display import HTML, display
    except ImportError:
        get_ipython = None

    if get_ipython is None or get_ipython() is None:
        # Fora da janela interativa (ex.: python arquivo.py): só informa o caminho
        print(f"[animação] {caminho}")
        return

    dados = base64.b64encode(caminho.read_bytes()).decode("ascii")
    display(HTML(f'<img src="data:image/gif;base64,{dados}" width="{largura}">'))
